default:
    just --list


# run locally in development mode
dev:
    uv run fastapi dev --host 127.0.0.1 main.py

# run locally
run:
    uv run fastapi run --host localhost:8080 main.py

# run a shell with all the dependencies
shell:
    uv run bash

# update or generate requirements.txt
update-requirements:
    # needed by heroku
    uv pip freeze > requirements.txt

# deploy to Heroku
deploy:
    # heroku create urlshrt
    heroku git:remote -a urlshrt
    #heroku config:set POSTGRES_URL="$POSTGRES_URL" --app urlshrt
    git push heroku main
