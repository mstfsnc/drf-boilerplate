FROM python:3.7-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install --upgrade pip && pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
