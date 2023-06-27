FROM python:3.9-buster 

# install nginx
RUN apt-get update && apt-get nstall nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-availabble/default
RUN ln -sf /dev

# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# ADD . /app

# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r requirements.txt

# COPY . /app/
