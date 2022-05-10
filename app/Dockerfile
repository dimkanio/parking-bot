# Этап, на котором выполняются подготовительные действия
FROM python:3.9-slim as builder

# Настроить и активировать виртуальную среду
ENV VIRTUAL_ENV "/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update  \
    && apt-get -y install libpq-dev gcc libc-dev\
    && pip3 install psycopg2-binary \
    && pip3 install aioschedule \
    && pip3 install wheel

COPY ./app/requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Финальный этап
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update  \
    && apt-get -y install libpq-dev gcc libc-dev\
    && pip3 install psycopg2-binary \
    && pip3 install aioschedule \
    && pip3 install wheel

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip3 install --no-cache /wheels/*

COPY ./app/y2parkingbot.py .
COPY ./app/src/ ./src

CMD ["python3", "-u", "y2parkingbot.py"]
