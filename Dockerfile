FROM python:3

COPY echo-server.py /

EXPOSE 65432
ENTRYPOINT ["python", "echo-server.py"]
