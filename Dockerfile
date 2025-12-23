FROM alpine:latest
RUN apk add --no-cache \
    curl \
    bash \
    jq \
    util-linux \
    gzip \
    coreutils
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

