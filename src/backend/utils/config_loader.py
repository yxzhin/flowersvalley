from pathlib import Path


class ConfigLoader:
    BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent

    @staticmethod
    def import_env() -> None:
        try:
            from dotenv import load_dotenv
        except Exception:
            print("Starting without .env")
            return

        env_file = ConfigLoader.BASE_PATH / ".env"
        print(f"Loading environment variables from {env_file}")
        if not env_file.exists():
            print(f"File {env_file} not found. Skipping loading environment variables.")
            return
        load_dotenv(dotenv_path=env_file)
