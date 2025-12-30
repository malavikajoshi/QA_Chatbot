# QA Chatbot - History Helper Bot

**QA Chatbot** is an AI-powered chatbot built using the Ollama API. It acts as a friendly and knowledgeable history assistant, answering user questions with a tone like a passionate history teacher. It also provides informative responses with dates when mentioned and admits when a question is outside its expertise.


## Features

- Answer history-related questions accurately and engagingly
- Friendly, teacher-like conversational tone
- Includes dates in responses
- Handles unknown questions gracefully
- Real-time streaming responses


## Project Structure

- `qa_chatbot.py` - Main chatbot script
- `venv/` - Virtual environment folder
- Other Python dependencies handled via `pip` (e.g., `ollama`)


## Setup & Installation (WSL)

1. **Navigate to the project folder**:

cd ~/QA_Chatbot
Activate virtual environment:

source venv/bin/activate
Install dependencies (first time or if new packages are added):

pip install --upgrade pip
pip install ollama
Run the chatbot:


python3 qa_chatbot.py
Exit virtual environment (optional):

deactivate
✅ Tip: Always activate the virtual environment before running the project to avoid module errors.

Usage
Type any history question to get answers.
Example:
You: Who was the first emperor of Rome?
