FROM golang:1.20.2 AS builder

WORKDIR /app

COPY . .

RUN CGO_ENABLED=0 go build -o build/fizzbuzz

FROM gcr.io/distroless/static-debian11

COPY --from=builder /app/build/fizzbuzz /

COPY --from=builder /app/templates/index.html /templates/

CMD ["/fizzbuzz", "serve"]
