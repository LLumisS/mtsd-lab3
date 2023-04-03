FROM golang:1.20.2

WORKDIR /app

COPY . .

RUN go mod download

RUN go build -o build/fizzbuzz

CMD ["./build/fizzbuzz", "serve"]
