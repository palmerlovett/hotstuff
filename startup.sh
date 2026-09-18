#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
exec gunicorn django_project.wsgi:application --bind "0.0.0.0:${PORT:-3000}"