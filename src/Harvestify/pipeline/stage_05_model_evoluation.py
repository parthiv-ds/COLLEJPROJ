from Harvestify.config.configuration import ConfigurationManager
from Harvestify.components.model_evoluation import ModelEvaluation
from Harvestify import logger


STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config1 = ConfigurationManager()
        model_evaluation_config = config1.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config1=model_evaluation_config)
        model_evaluation_config.save_results()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
