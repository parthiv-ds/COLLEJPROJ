from Harvestify.config.configuration import ConfigurationManager
from Harvestify.components.data_transformatio import DataTransformation
from Harvestify import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts1/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config1 = ConfigurationManager()
                data_transformation_config = config1.get_data_transformation_config()
                data_transformation = DataTransformation(config1=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)
