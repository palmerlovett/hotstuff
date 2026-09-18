
cd /root/ghc-publication || exit
/root/.local/bin/uv run gunicorn django_project.wsgi:application --bind 127.0.0.1:80