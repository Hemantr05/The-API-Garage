FROM python:3.8

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD hypercorn main:app --reload
# CMD uvicorn main:app --reload --workers 1 --host 127.0.0.1 --port 8000