FROM python:3.13.0rc1-bookworm 

ENV PYTHONUNBUFFERED=1

WORKDIR /api

RUN pip install django django-cors-headers djangorestframework djangorestframework-simplejwt 

COPY . .

EXPOSE 8000