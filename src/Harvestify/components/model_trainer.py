import pandas as pd
import os
from Harvestify import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from Harvestify.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config1: ModelTrainerConfig):
        self.config1 = config1

    
    def train(self):
        train_data = pd.read_csv(self.config1.train_data_path)
        test_data = pd.read_csv(self.config1.test_data_path)


        train_x = train_data.drop([self.config1.target_column], axis=1)
        test_x = test_data.drop([self.config1.target_column], axis=1)
        train_y = train_data[[self.config1.target_column]]
        test_y = test_data[[self.config1.target_column]]


        RF = RandomForestClassifier(n_estimators=self.config1.n_estimators,random_state=self.config1.random_state)
        RF.fit(train_x, train_y)

        joblib.dump(RF, os.path.join(self.config1.root_dir, self.config1.model_name))

