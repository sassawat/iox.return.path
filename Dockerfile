FROM python:3.8.5
RUN apt-get update -y \
    && apt-get install -y bc vim
WORKDIR /api
ADD . /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","app.py"]
