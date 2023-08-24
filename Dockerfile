FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip unoconv libreoffice

RUN pip3 install Flask

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]