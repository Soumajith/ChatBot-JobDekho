# AskMeAnything Bot

## Introduction

AskMeAnything Bot is a simple yet powerful chatbot application that allows users to interact and get responses to their queries. This application uses a Flask backend to serve a trained NLP model which generates responses to user inputs. 

## Features

- **Interactive Chat Interface**: A user-friendly chat interface powered by React.
- **NLP Model Integration**: Uses a trained NLP model to generate responses to user queries.
- **Flask Backend**: A robust backend service to handle API requests and responses.
- **CORS Enabled**: Cross-Origin Resource Sharing enabled to handle requests from different origins.
- **Error Handling**: Graceful error handling for better user experience.

## Usage

1. **Open the Chatbot**: Click on the chatbot icon to open the chat window.
2. **Send a Message**: Type your message in the input field and hit "Send".
3. **Get a Response**: The bot will respond to your message using the trained NLP model.

## How to Run

### Prerequisites

- Python 3.x
- Flask

## Installation Procedure

### Backend Setup (Flask)

#### For Windows

1. **Clone the Repository**

   Open Command Prompt or PowerShell and run:

   ```bash
   git clone https://github.com/yourusername/askmeanything-bot.git
   cd askmeanything-bot/backend
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Server**

   ```bash
   set FLASK_APP=app.py
   flask run
   ```

   The server will start on `http://127.0.0.1:5000`.

#### For macOS

1. **Clone the Repository**

   Open Terminal and run:

   ```bash
   git clone https://github.com/yourusername/askmeanything-bot.git
   cd askmeanything-bot/backend
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Server**

   ```bash
   export FLASK_APP=app.py
   flask run
   ```

   The server will start on `http://127.0.0.1:5000`.

### Integration

Ensure that your Flask backend is running and accessible. The React app will send requests to the Flask server to get responses for user inputs.

## Additional Information

- **Flask App**: The Flask application handles incoming POST requests to the `/predict` endpoint, processes the input using the trained NLP model, and returns the predicted response. 

Feel free to contribute to this project by opening issues or submitting pull requests📍.
