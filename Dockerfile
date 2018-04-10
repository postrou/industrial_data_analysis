FROM ubuntu:latest
RUN apt-get update 
RUN apt-get install -y python3-pip python3-dev build-essential
COPY regression_predict.py regression_fit.py requirements.txt model.py /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
#ENTRYPOINT ["python3"]
#CMD ["app.py"]