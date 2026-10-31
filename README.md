# Django starter

A [Django](https://www.djangoproject.com) app on PostgreSQL, served by gunicorn, with static files served by WhiteNoise. Each request to `/` records a visit and returns the count, which proves the database works. The admin is at `/admin/`.

## Run it locally

```sh
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
export DEBUG=1       # local only: SQLite, no SECRET_KEY needed
python manage.py migrate
python manage.py runserver
```

Then open http://localhost:8000. `GET /health` answers `ok` for health checks.

## Deploying

| Step | Command |
| --- | --- |
| Build | pip install -r requirements.txt |
| Before each release | python manage.py migrate |
| Start | gunicorn config.wsgi:application |

Database migrations run as a separate step before the new version starts, never during the build: a build has no database to talk to.

## Environment variables

| Variable | Meaning |
| --- | --- |
| `PORT` | Port to listen on. Default: 8000. |
| `SECRET_KEY` | Django's secret key. Required unless `DEBUG` is on. Use a long random value and keep it secret. |
| `ALLOWED_HOSTS` | Comma-separated host names the site answers to, e.g. `example.com`. `localhost` is always allowed. |
| `DEBUG` | `1` turns on debug mode. Off by default; never turn it on for a public site. |
| `DATABASE_URL` | PostgreSQL connection string. Required unless `DEBUG` is on (then SQLite). |

## Notes

To create an admin user: `python manage.py createsuperuser`. Dependencies are pinned in `requirements.txt`, generated from `requirements.in` with `uv pip compile requirements.in -o requirements.txt`.

## License

MIT
