FROM python:3.8-slim
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app
CMD [ "python","helo.py" ]
