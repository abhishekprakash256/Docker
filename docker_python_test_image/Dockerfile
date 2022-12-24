FROM ubuntu:latest

RUN apt-get update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY print.py ./

CMD ["python3","./print.py"]