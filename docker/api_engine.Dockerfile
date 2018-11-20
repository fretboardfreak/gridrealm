FROM python:3.6

# install python requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

# install gridrealm
RUN mkdir /gridrealm
COPY dist /gridrealm/

# create gridrealm_config volume
RUN mkdir /gridrealm_config
COPY docker/docker.cfg /gridrealm_config/docker.cfg

# initialize the database file on the config volume
RUN python /gridrealm/gr.py --config /gridrealm_config/docker.cfg --initdb

VOLUME /gridrealm_config

RUN mkdir /socket
VOLUME /socket

EXPOSE 8000
WORKDIR /gridrealm
ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "gunicorn_conf.py", "-b", "unix:/socket/api_engine", "uwsgi_docker:application"]
