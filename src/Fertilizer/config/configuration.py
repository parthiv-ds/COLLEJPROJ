from Fertilizer.constants import *
from Fertilizer.utils.common import read_yaml, create_directories
from Fertilizer.entity.config_entity import (DataIngestionConfig,
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

        self.config2 = read_yaml(config_filepath)
        self.params2 = read_yaml(params_filepath)
        self.schema2 = read_yaml(schema_filepath)

        create_directories([self.config2.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config2 = self.config2.data_ingestion

        create_directories([config2.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config2.root_dir,
            database_path=config2.database_path,
            table_name=config2.table_name,
            download_dir=config2.download_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config2 = self.config2.data_validation
        schema2 = self.schema2.COLUMNS

        create_directories([config2.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config2.root_dir,
            STATUS_FILE=config2.STATUS_FILE,
            download_dir = config2.download_dir,
            all_schema=schema2,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config2 = self.config2.data_transformation

        create_directories([config2.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config2.root_dir,
            data_path=config2.data_path,
            soil_name=config2.soil_name,
            crop_name=config2.crop_name,
            Fertilizer_name=config2.Fertilizer_name,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config2 = self.config2.model_trainer
        params2 = self.params2.RandomForestClassifier
        schema2 =  self.schema2.TARGET_COLUMN

        create_directories([config2.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config2.root_dir,
            train_data_path = config2.train_data_path,
            test_data_path = config2.test_data_path,
            model_name = config2.model_name,
            random_state = params2.random_state,
            target_column = schema2.name,
            
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config2 = self.config2.model_evaluation
        params2 = self.params2.RandomForestClassifier
        schema2 =  self.schema2.TARGET_COLUMN
        

        create_directories([config2.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config2.root_dir,
            test_data_path=config2.test_data_path,
            model_path = config2.model_path,
            all_params=params2,
            metric_file_name = config2.metric_file_name,
            target_column = schema2.name
           
        )

        return model_evaluation_config

