from pathlib import Path
from pycaret.regression import load_model, predict_model
import pandas as pd

def test_model_loads():
    model = load_model(str(Path("Model/pred_model")))
    assert model is not None

def test_model_predicts():
    model = load_model(str(Path("Model/pred_model")))
    sample = pd.DataFrame([{
        "age": 30, "sex": "male", "bmi": 25.0,
        "children": 1, "smoker": "no", "region": "southwest"
    }])
    result = predict_model(model, data=sample)
    assert "prediction_label" in result.columns
    assert result["prediction_label"][0] > 0