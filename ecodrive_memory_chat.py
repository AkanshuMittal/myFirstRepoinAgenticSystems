import json 
import os 

HISTORY_FILE = "ecodrive_chat_history.json"

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
        
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def append_turn(history, user_text, bot_text):
    history.append({"role": "user", "content": user_text})
    history.append({"role": "assistant", "content": bot_text})
    save_history(history)
    return history

def mock_rag_answer(full_question):
    text = full_question.lower()
    if "2022" in text and "revenue" in text:
        return "EcoDrive revenue in 2022 was 12.4 billion dollars."
    if "2023" in text and ("revenue" in text or "2022" in text):
        return "EcoDrive revenue in 2023 was 14.1 billion dollars."
    return "I need more context about which metric and year you mean."

def chat_once(user_message, history):
    # Build full_question
    lines = []
    for turn in history:
        lines.append(f"{turn['role']}: {turn['content']}")
    lines.append(f"user: {user_message}")
    full_question = "\n".join(lines)

    try:
        bot_reply = mock_rag_answer(full_question)
    except:
        bot_reply = "Search is unavailable right now. Please try again in a minute."

    append_turn(history, user_message, bot_reply)
    return bot_reply


def main():
    # Delete JSON file if exists
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

    history = load_history()

    # Turn 1
    msg1 = "What was EcoDrive revenue in 2022?"
    reply1 = chat_once(msg1, history)
    print("Turn 1:", reply1)

    # Reload history
    history = load_history()

    # Turn 2
    msg2 = "And in 2023?"
    reply2 = chat_once(msg2, history)
    print("Turn 2:", reply2)


if __name__ == "__main__":
    main()