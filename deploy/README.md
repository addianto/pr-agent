# Build & Deploy Guide

## Webhook @ GitLab CSUI

Prepare two environment variable files named `.env-config-gitlab-csui`
and `.env-secrets-gitlab-csui` in the deployment directory.
The redacted examples are available in the [`.env-config-gitlab-csui.example`](.env-config-gitlab-csui.example)
and [`.env-secrets-gitlab-csui.example`](.env-secrets-gitlab-csui.example) files.

After preparing the environment variable files, run Qodo Merge using Docker:

```shell
docker run --name "qodo-merge_gitlab-csui-webhook" \
    --detach \
    --env-file .env-config-gitlab-csui \
    --env-file .env-secrets-gitlab-csui \
    --publish "127.0.0.1:3000:3000" \
    docker.io/addianto/qodo-merge:gitlab-csui-webhook
```