@echo off

cd /d "%~dp0"
cd ../

if not exist .venv (
    uv venv
)
call .venv\Scripts\activate
uv sync
uv run python -m src.backend.bot.app.main
