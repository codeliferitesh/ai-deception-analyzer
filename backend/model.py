import joblib
import os

MODEL_PATH = "saved_model/model.pkl"
VEC_PATH = "saved_model/vectorizer.pkl"

def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VEC_PATH)
        return model, vectorizer
    except Exception:
        print("⚠️ Model not found or corrupted. Training new model...")
        import train  # auto-train
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VEC_PATH)
        return model, vectorizer

model, vectorizer = load_model()

def predict(text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0]

    return {
        "truth": float(prob[0]),
        "deception": float(prob[1])
    }