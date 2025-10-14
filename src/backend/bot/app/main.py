from ...utils import StructuredLogger


def main() -> None:
    StructuredLogger.setup()
    StructuredLogger.info("[BOT] initialized successfully!! :tada:")


if __name__ == "__main__":
    main()
