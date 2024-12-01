FROM python:alpine3.20

COPY main.py main.py

COPY books/ books/

CMD ["python", "main.py"]