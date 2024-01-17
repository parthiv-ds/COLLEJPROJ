import os
import pandas as pd
from Fertilizer import logger
from sklearn import metrics
from Fertilizer.utils.common import save_json
import joblib
from Fertilizer.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config2: ModelEvaluationConfig):
        self.config2 = config2

    
    def eval_metrics(self,actual, pred):
        '''
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
        '''
        acc=metrics.accuracy_score(actual,pred)
        return acc
    


    def save_results(self):

        test_data = pd.read_csv(self.config2.test_data_path)
        model = joblib.load(self.config2.model_path)

        test_x = test_data.drop([self.config2.target_column], axis=1)
        test_y = test_data[[self.config2.target_column]]
        
        predicted_labels = model.predict(test_x)

        #(rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

        (acc) = self.eval_metrics(test_y, predicted_labels)
        
        # Saving metrics as local
        scores = {"accuracy" : acc}
        logger.info(scores)
        save_json(path=Path(self.config2.metric_file_name), data=scores)



