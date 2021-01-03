FROM python:3.7

RUN apt-get update && apt-get -y install libjpeg-dev && apt-get install tesseract-ocr tesseract-ocr-por -y

ARG MODE
ARG PORT
ARG VERSION

ADD / /app

WORKDIR app
RUN ls -l

# Python dependencies
RUN pip --no-cache-dir --trusted-host pypi.python.org install -r /app/requirements.txt

EXPOSE $PORT

RUN ls -l

RUN rm -rf /tmp/* /var/tmp/* /app/notebook/*

CMD python -u main.py --port $PORT --version $VERSION