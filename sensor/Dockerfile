FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y --no-install-recommends gettext && apt-get clean

WORKDIR /app

USER $MOD_WSGI_USER:$MOD_WSGI_GROUP

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .
##This bolerplate can be avoided using base images.

CMD ["python", "sensor.py"]