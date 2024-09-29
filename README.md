# User-Profile Installation Guide

## Installation Methods

### Method 1: Using Python Virtual Environment

1. Update package list and install Python 3.12 venv:
   ```
   sudo apt update
   sudo apt install python3.12-venv
   ```

2. Create and activate a Python virtual environment:
   ```
   python3 -m venv pj1
   source pj1/bin/activate
   ```

3. Install required packages and launch the backend service:
   ```
   pip3 install -r requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8002
   ```

4. Alternatively, use tmux to run the service in the background:
   ```
   tmux attach -t B
   source pj1/bin/activate
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8002
   ```

### Method 2: Using Docker

1. Install Docker:
   ```
   sudo apt install docker.io
   ```

2. Build the Docker image:
   ```
   sudo docker build -t matching-service .
   ```

3. Run the Docker container:
   ```
   sudo docker run -d -p 8002:8002 matching-service
   ```
4. Restart Docker 
   ```
   sudo service docker stop
   sudo service docker start
   ```

Choose the method that best suits your needs and environment.