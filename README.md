## This project shows the how to work with GitHub Actions using Docker.
## Dockerized Flask App with CI/CD 🚀

This repository contains a simple Flask web application that returns "Hello World!" at the root endpoint (/).
It is fully Dockerized and includes a GitHub Actions CI/CD pipeline that:

 1. Runs automated tests with pytest

 2. Builds a Docker image

 3. Pushes the image to DockerHub

### 🛠️ Tech Stack

 1. Flask
 – Lightweight Python web framework

 2. Pytest
 – Testing framework

 3. Docker
 – Containerization

 4. GitHub Actions
 – CI/CD automation

### 📂 Project Structure
```
.
├── .github/workflows/cicd.yml   # GitHub Actions CI/CD pipeline
├── app.py                        # Flask application
├── test_app.py                   # Pytest file for testing
├── DockerFile                     # Dockerfile to build the app image
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

### ▶️ Running the App Locally
1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

2. Create a virtual environment & install dependencies
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run the Flask app
`python app.py`


Visit 👉 `http://localhost:5000`

### Expected output:
`Hello World!`

### 🧪 Running Tests
Run unit tests using pytest:

### pytest
#### 🐳 Running with Docker
1. Build Docker image
`docker build -t flasktest-app .`

2. Run container
`docker run -p 5000:5000 flasktest-app`

Now visit 👉 `http://localhost:5000`

###⚡ CI/CD with GitHub Actions

The workflow defined in `.github/workflows/cicd.yml` will:

  1. Run tests (pytest) on every push/PR to main

  2. Build a Docker image if tests pass

  3. Push the image to DockerHub

### 🔑 DockerHub Authentication

Add the following GitHub Secrets to your repository:
```
DOCKER_USERNAME → Your DockerHub username

DOCKER_PASSWORD → Your DockerHub access token/password
```

### 📦 DockerHub Image

Once the pipeline runs successfully, the image will be available at:

`docker pull <your-dockerhub-username>/flasktest-app:latest`

✅ Example API Response
`curl http://127.0.0.1:5000/`

