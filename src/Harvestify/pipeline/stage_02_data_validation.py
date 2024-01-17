from Harvestify.config.configuration import ConfigurationManager
from Harvestify.components.data_validation import DataValiadtion
from Harvestify import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config1 = ConfigurationManager()
        data_validation_config = config1.get_data_validation_config()
        data_validation = DataValiadtion(config1=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
