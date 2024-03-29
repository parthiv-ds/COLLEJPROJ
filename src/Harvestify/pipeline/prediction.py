import joblib 
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline1:
    def __init__(self):
        self.model = joblib.load(Path('artifacts1/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction