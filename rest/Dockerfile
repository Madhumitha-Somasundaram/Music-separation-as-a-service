

FROM python:3.11-slim

WORKDIR /app
COPY rest-server.py ./

RUN pip3 install flask redis minio requests
RUN pip3 install python-dotenv

EXPOSE 5000
CMD ["python", "rest-server.py"]
