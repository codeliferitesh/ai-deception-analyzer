import json
import datetime
from backend.model import predict
from backend.utils import emotion

HISTORY_FILE = "history.json"

def save_history(entry):
    try:
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)


def show_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)

        if not data:
            print("⚠️ No history found")
            return

        print("\n📜 HISTORY:")
        for i, item in enumerate(data, 1):
            print(f"\n{i}. Text: {item['text']}")
            print(f"   Truth: {item['truth']}")
            print(f"   Deception: {item['deception']}")
            print(f"   Emotion: {item['emotion']}")
            print(f"   Time: {item['time']}")

    except:
        print("⚠️ No history file found")


def analyze_text():
    text = input("\n📝 Enter text: ").strip()

    if not text:
        print("❌ Empty input!")
        return

    result = predict(text)
    emo = emotion(text)

    print("\n🔍 RESULT:")
    print(f"Truth Probability     : {result['truth']:.2f}")
    print(f"Deception Probability: {result['deception']:.2f}")
    print(f"Emotion              : {emo}")

    entry = {
        "text": text,
        "truth": result["truth"],
        "deception": result["deception"],
        "emotion": emo,
        "time": str(datetime.datetime.now())
    }

    save_history(entry)


def help_menu():
    print("""
📖 AVAILABLE COMMANDS:
1. analyze  → Analyze text
2. history  → View past results
3. help     → Show commands
4. exit     → Exit program
""")


def start_cli():
    print("""
🧠 AI DECEPTION ANALYZER (CLI VERSION)
-------------------------------------
Type 'help' to see commands
""")

    while True:
        cmd = input("\n👉 Enter command: ").strip().lower()

        if cmd == "analyze":
            analyze_text()

        elif cmd == "history":
            show_history()

        elif cmd == "help":
            help_menu()

        elif cmd == "exit":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid command! Type 'help'")