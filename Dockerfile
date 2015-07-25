FROM python:3.4.3

MAINTAINER David OK <david.ok8@gmail.com>

ADD . /home/injila_service
WORKDIR /home/injila_service
RUN pip install -r requirements.txt

CMD ["python", "-u", "app.py"]
