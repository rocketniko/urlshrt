default:
    just --list


# run with fastapi
dev:
    uv run fastapi dev --host 127.0.0.1 main.py

run:
    uv run fastapi run --host localhost:8080 main.py

# run a shell with all the dependencies
shell:
    uv run bash

update-requirements:
    # needed by heroku
    uv pip freeze > requirements.txt

deploy:
    # heroku create urlshrt
    heroku git:remote -a urlshrt
    git push heroku main
