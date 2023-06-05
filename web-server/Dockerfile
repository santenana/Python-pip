FROM python:3.8

WORKDIR /appweb
COPY requirements.txt /appweb/requirements.txt

RUN  pip install --no-cache-dir --upgrade -r /appweb/requirements.txt

COPY . /appweb

CMD ["uvicorn","main:appweb","--host","0.0.0.0","--port","80"]
