from Fertilizer.config.configuration import ConfigurationManager
from Fertilizer.components.data_validation import DataValiadtion
from Fertilizer import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config2 = ConfigurationManager()
        data_validation_config = config2.get_data_validation_config()
        data_validation = DataValiadtion(config2=data_validation_config)
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
