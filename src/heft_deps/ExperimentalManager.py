from src.heft_deps.resource_manager import Resource, Node
from src.heft_deps.resource_manager import Estimator
from src.heft_deps.resource_manager import ResourceManager
import numpy as np


class ModelTimeEstimator(Estimator):
    """
    Transfer time between 2 nodes in one blade = transfer_nodes, otherwise = transfer_blades
    """

    def __init__(self, bandwidth=10):
        self.bandwidth = bandwidth  # MB /sec

    # #get estimated time of running the task on the node
    def estimate_runtime(self, task, node):
        result = task.runtime / np.sqrt(node.flops / 8)
        return result

    ## estimate transfer time between node1 and node2 for data generated by the task
    def estimate_transfer_time(self, node1, node2, task1, task2):

        if node1 == node2:
            res = 0.0
        else:
            transfer_time = 0
            for filename, file in task2.input_files.items():
                if filename in task1.output_files:
                    transfer_time += (file.size / 1024 / 1024 / self.bandwidth)  # data to MB and divide to MB/sec
            res = transfer_time
        return res


class ExperimentResourceManager(ResourceManager):

    def __init__(self, resources):
        self.resources = resources
        self.resources_map = {res.name: res for res in self.resources}
        self._name_to_node = None

    def node(self, node):
        if isinstance(node, Node):
            result = [nd for nd in self.resources_map[node.resource.name].nodes if nd.name == node.name]
        else:
            name = node
            result = [nd for nd in self.get_nodes() if nd.name == name]

        if len(result) == 0:
            return None
        return result[0]

    def resource(self, resource):
        return self.res_by_id(resource)

    ##get all resources in the system
    def get_resources(self):
        return self.resources

    def get_live_resources(self):
        resources = self.get_resources()
        result = set()
        for res in resources:
            if res.state != 'down':
                result.add(res)
        return result

    def get_live_nodes(self):
        resources = [res for res in self.get_resources() if res.state != 'down']
        result = set()
        for resource in resources:
            for node in resource.nodes:
                if node.state != "down":
                    result.add(node)
        return result

    def get_all_nodes(self):
        result = set()
        for res in self.resources:
            for node in res.nodes:
                result.add(node)
        return result

    def change_performance(self, node, performance):
        ##TODO: rethink it
        self.resources[node.resource][node].flops = performance

    def byName(self, name):
        if self._name_to_node is None:
            self._name_to_node = {n.name: n for n in self.get_nodes()}
        return self._name_to_node.get(name, None)

    def res_by_id(self, id):
        name = id.name if isinstance(id, Resource) else id
        return self.resources_map[name]

    def get_res_by_name(self, name):
        """
        find resource from resource list by name
        """
        for res in self.resources:
            if res.name == name:
                return res
        return None

    def get_node_by_name(self, name):
        """
        find node in all resources by name
        """
        for res in self.resources:
            for node in res.nodes:
                if node.name == name:
                    return node
        return None
