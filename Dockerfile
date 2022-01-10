FROM nikolaik/python-nodejs:python3.10-nodejs14
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN npm install pm2@latest -g

RUN apt-get update \
    && apt-get install -y curl apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev

# To fix protocol
COPY docker_app/openssl.cnf /etc/ssl/openssl.cnf

WORKDIR /app

COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system --deploy

ADD src ./src
COPY docker_app/local.py ./src/conf/settings/local.py
COPY docker_app/start.sh ./src/
COPY docker_app/start_scheduler.sh ./src/
COPY docker_app/pm2_process.json ./src/
RUN mkdir -p ./logs
RUN touch ./logs/app_sample.log

WORKDIR /app/src

ENV DJANGO_SETTINGS_MODULE="conf.settings.local"

CMD pm2-runtime start ./pm2_process.json
