FROM python:3.10.11

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip -r install --timeout 300000 /tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 3000

CMD ["streamlit", "run", 'main.py', "server.port=8501"] 

