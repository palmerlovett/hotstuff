#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
exec gunicorn django_project.wsgi:application \
  --bind 127.0.0.1:8010