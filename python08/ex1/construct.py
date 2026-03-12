import sys
import site


def main():
    if ({sys.base_prefix} == {sys.prefix}):
        print("Matrix status : You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Version : {sys.version}")
        print("Virtual Environmnet: None detected")
        print()

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print("To enter the construct, run:")
        print("python -m venv matrix_env\nsource matrix_env/bin/activate # "
              "On Unix\nmatrix_env\nScripts\nactivate # On Windows")
        print()

        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Environment Path: {sys.prefix}")
        print()

        print("SUCCESS: You're in an isolated environment!\nSafe to install "
              "packages without affecting the global system")

        print(f"Package installation path: {site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
