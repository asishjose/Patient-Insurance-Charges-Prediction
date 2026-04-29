import pandas as pd
from pycaret.regression import setup, compare_models, save_model, pull
from pathlib import Path

DATA_PATH  = Path("data/insurance.csv")
MODEL_PATH = Path("Model/pred_model")
METRICS_PATH = Path("metrics.txt")

def train():
    df = pd.read_csv(DATA_PATH)

    # PyCaret setup — matches how pred_model was originally trained
    setup(
        data=df,
        target="expenses",
        session_id=42,
        verbose=False
    )

    best_model = compare_models(verbose=False)

    # Save R² score
    results = pull()
    r2 = results.iloc[0]["R2"]
    print(f"Best model R²: {r2:.4f}")

    METRICS_PATH.write_text(str(r2))
    save_model(best_model, str(MODEL_PATH))
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()