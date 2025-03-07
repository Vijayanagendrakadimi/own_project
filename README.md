# My Python Project

This project is a simple web application that includes a basic login page. It is built using Python and Flask, and it is containerized using Docker. Below are the details for setting up and running the application.

## Project Structure

```
my-python-project
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── templates
│   │   └── login.html
│   └── static
│       └── styles.css
├── Dockerfile
├── buildspec.yml
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.x
- Flask
- Docker (for containerization)

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-python-project
   ```

2. **Install dependencies:**
   It is recommended to create a virtual environment before installing the dependencies.
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can run the application locally using:
   ```
   python app/main.py
   ```

4. **Access the login page:**
   Open your web browser and go to `http://127.0.0.1:5000/login`.

## Docker Instructions

To build and run the Docker container, use the following commands:

1. **Build the Docker image:**
   ```
   docker build -t my-python-project .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 5000:5000 my-python-project
   ```

## AWS CodeBuild

This project includes a `buildspec.yml` file for AWS CodeBuild. It defines the build process for deploying the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.