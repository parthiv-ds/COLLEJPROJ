import pandas as pd
import os
from Fertilizer import logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from collections import Counter
import joblib
from Fertilizer.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config2: ModelTrainerConfig):
        self.config2 = config2

    
    def train(self):
        train_data = pd.read_csv(self.config2.train_data_path)
        test_data = pd.read_csv(self.config2.test_data_path)


        train_x = train_data.drop([self.config2.target_column], axis=1)
        test_x = test_data.drop([self.config2.target_column], axis=1)
        train_y = train_data[[self.config2.target_column]]
        test_y = test_data[[self.config2.target_column]]


        RF = RandomForestClassifier(random_state=self.config2.random_state)
        RF.fit(train_x, train_y)

        params = {
            'n_estimators':[200,300,320],
            'max_depth':[2,3,4,5,6],
            'min_samples_split':[2,5]
        }
        
        grid_rand = GridSearchCV(RF,params,cv=3,verbose=3,n_jobs=-1)

        grid_rand.fit(train_x,train_y)

        joblib.dump(grid_rand, os.path.join(self.config2.root_dir, self.config2.model_name))

