import subprocess
import sys
import time


def install_package(package):
    print(f"Installing {package}...")
    start = time.time()
    # Change 'pip' to 'uv', 'poetry', etc. for your demo
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", package],
        capture_output=True,
        text=True,
    )
    end = time.time()
    print(result.stdout)
    print(f"Time taken to install {package}: {end - start:.2f} seconds\n")


def show_package_version(package):
    try:
        pkg = __import__(package)
        print(f"{package} version: {pkg.__version__}")
    except ImportError:
        print(f"{package} is not installed.")


if __name__ == "__main__":
    install_package("requests")
    show_package_version("requests")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    print(f"Python version: {sys.version}")
