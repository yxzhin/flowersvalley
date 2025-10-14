@echo off

cd /d "%~dp0"
cd ../

if not exist .venv (
    uv venv
)
call .venv\Scripts\activate
uv sync
uv run alembic upgrade head
uv run uvicorn src.backend.server.app.main:app --host 0.0.0.0 --port 8000 --reload
