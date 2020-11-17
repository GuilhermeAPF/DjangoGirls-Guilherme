FROM python:3.9

WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /django
CMD ./manage.py runserver 0.0.0.0:8000