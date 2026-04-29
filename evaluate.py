import sys
from pathlib import Path

THRESHOLD        = 0.70
IMPROVEMENT_MARGIN = 0.01
METRICS_PATH     = Path("metrics.txt")
BASELINE_PATH    = Path("baseline_score.txt")

def evaluate():
    new_score = float(METRICS_PATH.read_text().strip())
    print(f"New model R²: {new_score:.4f}")

    if BASELINE_PATH.exists():
        baseline = float(BASELINE_PATH.read_text().strip())
        print(f"Baseline R²:  {baseline:.4f}")
    else:
        baseline = 0.0
        print("No baseline found — accepting new model.")

    if new_score < THRESHOLD:
        print(f"❌ FAILED: {new_score:.4f} below threshold {THRESHOLD}")
        sys.exit(1)

    if new_score < baseline - IMPROVEMENT_MARGIN:
        print(f"❌ FAILED: New model worse than baseline")
        sys.exit(1)

    BASELINE_PATH.write_text(str(new_score))
    print("✅ Model approved for deployment")

if __name__ == "__main__":
    evaluate()