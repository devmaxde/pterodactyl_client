FROM openapitools/openapi-generator-cli:v6.0.0
WORKDIR /app
COPY openapi2.yaml openapi.yaml
ENTRYPOINT ["sh"]
VOLUME /app/out
ENTRYPOINT ["sh"]
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh" ,"generate", "-i","openapi.yaml","-g","python","-o","out", "--package-name", "pterodactyl_client"]
