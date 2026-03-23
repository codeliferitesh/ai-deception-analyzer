import subprocess
import webbrowser
import time
import os
import sys

# Paths
BACKEND_DIR = os.path.join(os.getcwd(), "backend")
FRONTEND_FILE = os.path.join(os.getcwd(), "frontend", "index.html")

def start_backend():
    print("🚀 Starting FastAPI backend...")

    if sys.platform == "win32":
        return subprocess.Popen(
            ["cmd", "/c", "uvicorn main:app --reload"],
            cwd=BACKEND_DIR
        )
    else:
        return subprocess.Popen(
            ["uvicorn", "main:app", "--reload"],
            cwd=BACKEND_DIR
        )

def open_frontend():
    print("🌐 Opening frontend...")
    webbrowser.open(f"file://{FRONTEND_FILE}")

def main():
    backend_process = start_backend()

    # Wait for server to start
    time.sleep(3)

    open_frontend()

    print("\n✅ Project is running!")
    print("👉 Backend: http://127.0.0.1:8000")
    print("👉 Frontend opened in browser")

    try:
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        backend_process.terminate()

if __name__ == "__main__":
    main()