FROM python:3.7

RUN mkdir -p /usr/src/client/
RUN mkdir -p /usr/src/client/src
RUN mkdir -p /usr/src/resources
RUN mkdir -p /usr/src/results

COPY  /client/. /usr/src/client/
COPY /src/. /usr/src/client/src/
COPY /resources/. /usr/src/resources/

WORKDIR /usr/src/

RUN pip install tensorflow==1.14.0 Keras==2.2.5 networkx matplotlib requests Flask seaborn
ENTRYPOINT [ "python", "client/episode.py", "--alg=nns", "--host=0.0.0.0", "--port=9900", "--seq-size=5", "--wfs-name=Montage_25", "--num-episodes=1", "--actor-type=fc", "--model-type=ours", "--run-name=Montage_25", "--save=0", "--plot-csvs=0", "--is-test=0", "--logger=1"]
