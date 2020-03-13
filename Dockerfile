FROM python:3.6

MAINTAINER Rutger Drubbel

RUN pip install requests 

COPY send_file.py

CMD ["python3.6", send_file.py]
