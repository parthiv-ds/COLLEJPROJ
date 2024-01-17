from Fertilizer.config.configuration import ConfigurationManager
from Fertilizer.components.model_trainer import ModelTrainer
from Fertilizer import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config2 = ConfigurationManager()
        model_trainer_config = config2.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config2=model_trainer_config)
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
