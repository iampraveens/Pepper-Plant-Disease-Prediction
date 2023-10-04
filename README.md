# Pepper Plant Disease Prediction <img src="https://cdn-icons-png.flaticon.com/512/3631/3631976.png" alt="Car Price Prediction" width="50" height="50">

This Pepper Plant Disease Prediction project combines the power of machine learning and user-friendly design to address a real-world problem in agriculture, making it a valuable tool for farmers, gardeners, and anyone interested in plant health.

## Application
Deployed the model on streamlit cloud(temp) [Streamlit App](https://pepper-plant-disease-prediction.streamlit.app/) [Sample Images](https://drive.google.com/drive/folders/17NGHLB_uW6mQmOWxbqmSeFynrHpTcF0m?usp=sharing)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

This project is a Pepper Plant Disease Prediction web application built using Streamlit and TensorFlow/Keras. It allows users to upload an image of a pepper plant leaf, and the model will predict whether the plant is affected by bacteria or if it's healthy.

## Features

- Predicts pepper plant disease based on uploaded images.
- Provides visual feedback with color-coded results (red for affected by bacteria, green for healthy).
- Easy-to-use web interface.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/iampraveens/Pepper-Plant-Disease-Prediction.git
```
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```
3. Run the application

```bash
streamlit run app.py
```

### Usage

1. After running the application, you will see an option to upload an image of a pepper plant leaf.
2. Upload the image you want to analyze.
3. Click the "Predict Disease" button.
4. The application will display the prediction result - whether the plant is affected by bacteria or if it's healthy.

## Dockerized Web App
You can also deploy the Car Price Prediction web application using Docker. Build the Docker image and run the container:
```bash
docker build -t your_docker_username/health-research-tool-app .
```
- To build a docker image.

```bash
docker run -d -p 8501:8501 your_docker_username/health-research-tool-app
```
- To run as a container.

Access the web app at `http://localhost:8501` or `your_ip_address:8501` in your web browser.
Else if you want to access my pre-built container, here is the code below to pull from docker hub(Public).
```bash
docker pull iampraveens/health-research-tool-app:latest
```

## License 
This project is licensed under the MIT License - see the [License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) file for details.
