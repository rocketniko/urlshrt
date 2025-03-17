`urlshrt` is a URL shortener service.

Architecture:
	Python FastAPI service with Postgres database.

Features:
 - create short url
 - redirect to url

Deployment:
 - local
 - heroku

Environment variables:
	POSTGRES_URL: configured postgres database URL (tested with neon.tech)
