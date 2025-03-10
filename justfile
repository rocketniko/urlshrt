default:
    just --list


# run with fastapi
dev:
    uv run fastapi dev --host 127.0.0.1 main.py


# run a shell with all the dependencies
shell:
    uv run bash
