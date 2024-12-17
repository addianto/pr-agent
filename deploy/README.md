# Build & Deploy Guide

## Webhook @ GitLab CSUI

```shell
docker run --name qodo-merge_gitlab-csui-webhook \
    --detach \
    --env-file .env-config-gitlab-csui \
    --env-file .env-secrets-gitlab-csui \
    docker.io/addianto/qodo-merge:gitlab-csui-webhook
```