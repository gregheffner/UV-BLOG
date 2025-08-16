# pip-demo

This folder demonstrates running a simple Flask API server using pip and venv.

## Setup & Run

1. Create a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the API server:
   ```sh
   python api_server.py
   ```

The server will start on port 5000. Visit [http://localhost:5000](http://localhost:5000) to see the response.
