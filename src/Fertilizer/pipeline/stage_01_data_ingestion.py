from Fertilizer.config.configuration import ConfigurationManager
from Fertilizer.components.data_ingestion import DataIngestion
from Fertilizer import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config2 = ConfigurationManager()
        data_ingestion_config = config2.get_data_ingestion_config()
        data_ingestion = DataIngestion(config2=data_ingestion_config)
        data_ingestion.connect_db()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
