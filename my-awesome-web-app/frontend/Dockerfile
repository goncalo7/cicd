FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 8111
ENTRYPOINT ["python"]
CMD ["frontend.py"]
