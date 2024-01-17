from Harvestify.config.configuration import ConfigurationManager
from Harvestify.components.model_trainer import ModelTrainer
from Harvestify import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config1 = ConfigurationManager()
        model_trainer_config = config1.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config1=model_trainer_config)
        model_trainer_config.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
