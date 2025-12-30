import ollama

# --- 1. Setup: Model Name ---
MODEL_NAME = "llama3"  
# Change this if you've pulled a different model (e.g. 'mistral', 'gemma', etc.)

# --- 2. System Prompt / Persona ---
SYSTEM_PROMPT = """
You are 'History Helper,' a friendly and knowledgeable assistant specializing in history.
Your goal is to answer user questions accurately and engagingly.
- Your tone should be like a passionate history teacher.
- When you mention a date, always include the year.
- If you don't know the answer to a question, you must say
  "That's a fascinating question, but it's outside my area of historical expertise."
"""

conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("---History Helper Bot (Ollama Version)---")
print("Ask me any history question! Type 'exit' to end the chat.\n")

# --- 3. Chat Loop ---
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Farewell! May your future be as interesting as the past.")
        break

    # Add user message to history
    conversation_history.append({"role": "user", "content": user_input})

    try:
        # Send conversation to Ollama and get response
        stream = ollama.chat(
            model=MODEL_NAME,
            messages=conversation_history,
            stream=True
        )

        full_response = ""
        for chunk in stream:
            # Each chunk is a dict with keys like {"message": {"role": "assistant", "content": "..."}}
            if "message" in chunk and "content" in chunk["message"]:
                text = chunk["message"]["content"]
                print(text, end="", flush=True)
                full_response += text

        print("\n")  # Add newline after full response
        conversation_history.append({"role": "assistant", "content": full_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        conversation_history.pop()


###How to Run QA Chatbot Project (WSL)
# Open terminal and navigate to project folder:
# cd ~/QA_Chatbot


# Activate virtual environment:
# source venv/bin/activate

# Install dependencies (first time only or if new packages are added):
# pip install --upgrade pip
# pip install ollama


# Run the chatbot script:
# python3 qa_chatbot.py

# Exit virtual environment (optional):
# deactivate
# ✅ Tip: Always activate venv before running the project to avoid module errors.