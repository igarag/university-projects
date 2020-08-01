FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /home

COPY requirements.txt /home/
COPY ./entrypoint.sh /home/

RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y vim

ENTRYPOINT ["/bin/bash", "/home/entrypoint.sh"]
