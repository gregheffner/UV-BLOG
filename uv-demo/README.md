# uv-demo

This folder demonstrates running a simple Flask API server using UV's script management.

## Setup & Run

1. No need to manually create a virtual environment or install dependencies!
2. Just run:
   ```sh
   uv run api_server.py
   ```

UV will automatically create an isolated environment, install dependencies (from inline metadata), and run the script.

The server will start on port 5000. Visit [http://localhost:5000](http://localhost:5000) to see the response.
