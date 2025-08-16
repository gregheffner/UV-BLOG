
# uv-demo

This folder demonstrates running a simple Flask API server using UV.

## Setup & Run

1. Initialize the project (creates a requirements file):
   ```sh
   uv init
   ```
2. Add Flask as a dependency:
   ```sh
   uv add flask
   ```
3. Run the API server:
   ```sh
   uv run api_server.py
   ```

UV will automatically create an isolated environment, install dependencies, and run the script.

The server will start on port 5000. Visit [http://localhost:5000](http://localhost:5000) to see the response.
