# APICurlCustomIP
A lightweight Streamlit web app that allows you to test API endpoints using a curl command — securely executed inside a Docker container. It supports DNS resolution, optional IP overrides, and provides clean output feedback directly in the browser UI.


🚀 Features
Run curl commands in a sandboxed Docker environment.

Automatically resolve DNS to IP addresses if the IP is not provided.

Clean and intuitive Streamlit-based UI.

Clear separation of stdout and stderr responses.

Timeout and error handling built-in for safe execution.


🏗️ Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/<your-username>/api-curl-tester.git
cd api-curl-tester
2. Build the Docker Image
The app expects a Docker image named curl-hosts that can accept parameters for IP, DNS, and curl command.

You can create a simple Dockerfile like below:

text
FROM curlimages/curl:latest
ENTRYPOINT ["sh", "-c"]
Then build it:

bash
docker build -t curl-hosts .
3. Install Python Dependencies
bash
pip install streamlit
(Optionally, you may include requirements.txt with streamlit as a dependency.)

4. Run the App
bash
streamlit run app.py