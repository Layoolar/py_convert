FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN pip3 install Flask

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]