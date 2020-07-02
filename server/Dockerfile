FROM python:3.7

RUN mkdir -p /usr/src/server/
RUN mkdir -p /usr/src/server/src/

COPY  /server/. /usr/src/server/
COPY /src/. /usr/src/server/src/
WORKDIR /usr/src/

ARG PORT=9900

EXPOSE ${PORT}

RUN pip install tensorflow==1.14.0 Keras==2.2.5 networkx matplotlib requests Flask seaborn
ENTRYPOINT [ "python", "server/server.py", "--alg=nns", "--state-size=64", "--agent-tasks=5", "--model-type=ours" ,"--actor-type=fc", "--first-layer=1024", "--second-layer=512", "--third-layer=256", "--seq-size=5", "--load=0", "--load-path=''", "--nodes=4", "--host=0.0.0.0", "--port=9900", "--model-name=''"]
