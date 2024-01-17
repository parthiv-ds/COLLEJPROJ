import joblib 
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline2:
    def __init__(self):
        self.model = joblib.load(Path('artifacts2/model_trainer/model2.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction