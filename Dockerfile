FROM python:3.10

WORKDIR /code
COPY requirements.txt ./app
COPY . .


RUN apt-get update \
    && apt-get install -yyq netcat

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

COPY entrypoint.sh .
ENTRYPOINT [ "./entrypoint.sh" ]
