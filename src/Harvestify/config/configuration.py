from Harvestify.constants import *
from Harvestify.utils.common import read_yaml, create_directories
from Harvestify.entity.config_entity import (DataIngestionConfig,
                                             DataValidationConfig,
                                             DataTransformationConfig,
                                             ModelTrainerConfig,
                                             ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config1 = read_yaml(config_filepath)
        self.params1 = read_yaml(params_filepath)
        self.schema1 = read_yaml(schema_filepath)

        create_directories([self.config1.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config1 = self.config1.data_ingestion

        create_directories([config1.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config1.root_dir,
            database_path=config1.database_path,
            table_name=config1.table_name,
            download_dir=config1.download_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config1 = self.config1.data_validation
        schema1 = self.schema1.COLUMNS

        create_directories([config1.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config1.root_dir,
            STATUS_FILE=config1.STATUS_FILE,
            download_dir = config1.download_dir,
            all_schema=schema1,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config1 = self.config1.data_transformation

        create_directories([config1.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config1.root_dir,
            data_path=config1.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config1 = self.config1.model_trainer
        params1 = self.params1.RandomForestClassifier
        schema1 =  self.schema1.TARGET_COLUMN

        create_directories([config1.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config1.root_dir,
            train_data_path = config1.train_data_path,
            test_data_path = config1.test_data_path,
            model_name = config1.model_name,
            n_estimators = params1.n_estimators,
            random_state = params1.random_state,
            target_column = schema1.name
            
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config1 = self.config1.model_evaluation
        params1 = self.params1.RandomForestClassifier
        schema1 =  self.schema1.TARGET_COLUMN

        create_directories([config1.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config1.root_dir,
            test_data_path=config1.test_data_path,
            model_path = config1.model_path,
            all_params=params1,
            metric_file_name = config1.metric_file_name,
            target_column = schema1.name
           
        )

        return model_evaluation_config
