FROM debian:latest
RUN groupadd -r smok && useradd --no-log-init -r -g smok smok
COPY smok.sh /home/smok/smok.sh
RUN chmod +x /home/smok/smok.sh
WORKDIR /home/smok
USER smok
CMD ["./smok.sh"]
