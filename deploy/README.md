# Build & Deploy Guide

## Webhook @ GitLab CSUI

```shell
# TODO(addianto): Fix image name
docker run --name qodo-merge_csui \
    --detach \
    --env-file .env-config-gitlab-csui \
    --env-file .env-secrets-gitlab-csui \
    docker.io/library/alpine:latest
```