cd /root/hotstuff.lastman.enterprises || exit
/root/.local/bin/uv run gunicorn django_project.wsgi:application --bind 127.0.0.1:8010