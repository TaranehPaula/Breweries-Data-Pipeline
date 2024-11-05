FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY api_d.py /app/agregacao_d.py
COPY bees-440303-a4fa6e2ef5ea.json /app/bees-440303-a4fa6e2ef5ea.json

RUN pip install -r /app/requirements.txt
RUN pip install requests pandas google-cloud-bigquery google-cloud-storage

CMD ["python", "/app/agregacao_d.py"]