from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    print("Connecting to the matrix or smthing ...")
    env = os.getenv("ENV_FILE", "False").lower() in ("true")
    if not env:
        print("Connection to the matrix (.env) failed, check the .env file")
        return

    print("Connection to the matrix successful")
    print()

    mode = os.getenv("MATRIX_MODE", "development")
    if mode in ("development", "production"):
        print(f"Mode : {mode}")
    else:
        print(f"invalid MATRIX_MODE: {mode}")
    api = os.getenv("API_KEY", "ERROR missing api_key")
    print("API key : ", end="")
    print(api)
    matrix_mode = os.getenv("MATRIX_MODE", False)
    print(f"matrix mode enabled: {matrix_mode}")
    data_base = os.getenv("DATABASE_URL", "NO URL PROVIDED")
    print(f"Data_base URL : {data_base}")
    log = os.getenv("LOG_LEVEL", "Idk what should be default")
    print(f"Log level: {log}")
    zion = os.getenv("ZION_ENDPOINT", "offline")
    print(f"Zion connection: {zion}")


if __name__ == "__main__":
    main()
