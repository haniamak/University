FROM gcc AS builder
WORKDIR /zadanie3
COPY main.c .
RUN gcc main.c -o programhello

FROM debian:latest
COPY --from=builder zadanie3/programhello /usr/local/bin/hello
ENTRYPOINT ["hello"]

