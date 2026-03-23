def emotion(text):
    t = text.lower()

    if any(w in t for w in ["happy","great","love"]):
        return "Positive 😊"
    elif any(w in t for w in ["sad","bad","hate"]):
        return "Negative 😞"
    elif "angry" in t:
        return "Angry 😠"
    return "Neutral 😐"