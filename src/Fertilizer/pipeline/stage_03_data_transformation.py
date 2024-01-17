from Fertilizer.config.configuration import ConfigurationManager
from Fertilizer.components.data_transformation import DataTransformation
from Fertilizer import logger
from pathlib import Path
import pandas as pd


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts2/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config2 = ConfigurationManager()
                data_transformation_config = config2.get_data_transformation_config()
                data_transformation = DataTransformation(config2=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)
