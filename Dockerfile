#Build From Alpine to Reduce Build Size
FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# Add required packages
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

# Add our code to DockerContainer Folder
ADD . /app/webapp/

# Set Working Directory

WORKDIR /app/webapp/

# Upgrade PIP
RUN pip3 install --upgrade pip
RUN pip3 install setuptools wheel requests
# Install Requirements
RUN pip3 install -r requirements.txt

# Run the web server on port 8000
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]