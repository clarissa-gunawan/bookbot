FROM python:alpine3.20

COPY main.py main.py

COPY books/ books/

ENTRYPOINT ["python", "main.py"]