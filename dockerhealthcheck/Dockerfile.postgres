FROM mysql:5.7

COPY docker-healthcheck /usr/local/bin/

HEALTHCHECK CMD ["sh", "docker-healthcheck.sh"]
