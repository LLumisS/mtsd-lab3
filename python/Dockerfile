FROM python:3.11.2-alpine

WORKDIR /app

RUN apk add --no-cache g++ gcc gfortran musl-dev libffi-dev openssl-dev

COPY requirements/backend.in .

RUN pip install --no-cache-dir -r backend.in

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
