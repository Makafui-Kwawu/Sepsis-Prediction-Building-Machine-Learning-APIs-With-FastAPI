FROM python:3.10.11

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip -r install --timeout 300000 /tmp/requirements.txt

COPY .. /app

WORKDIR /app

EXPOSE 80

CMD ["uvicorn", "api:app", '--host', "0.0.0.0", "--port", "80"] 