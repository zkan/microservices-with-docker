FROM golang:1.7.1

COPY src/main.go /go/src/main.go
RUN go build -o bin/main src/main.go

ENTRYPOINT ["bin/main"]
