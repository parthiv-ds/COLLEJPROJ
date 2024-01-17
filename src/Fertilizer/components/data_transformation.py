import os
from Fertilizer import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from Fertilizer.entity.config_entity import DataTransformationConfig
import joblib

class DataTransformation:
    def __init__(self, config2: DataTransformationConfig):
        self.config2 = config2

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config2.data_path)
        data = data.drop(columns=['Unnamed: 0'],axis=1)

        le = LabelEncoder()

        data['soil']= le.fit_transform(data['soil'])
        soil_dict = dict(zip(le.classes_,le.transform(le.classes_)))
        joblib.dump(soil_dict,os.path.join(self.config2.root_dir,self.config2.soil_name))

        data['crop']= le.fit_transform(data['crop'])
        crop_dict = dict(zip(le.classes_,le.transform(le.classes_)))
        joblib.dump(crop_dict,os.path.join(self.config2.root_dir,self.config2.crop_name))

        data['Fertilizer']= le.fit_transform(data['Fertilizer'])
        fert_dict = dict(zip(le.classes_,le.transform(le.classes_)))
        joblib.dump(fert_dict,os.path.join(self.config2.root_dir,self.config2.Fertilizer_name))
        
        
        logger.info(crop_dict)
        logger.info(fert_dict)
        logger.info(soil_dict)
        
        

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config2.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config2.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
      
        
        
        