import os
from Harvestify import logger
import pandas as pd
from Harvestify.entity.config_entity import DataValidationConfig
                                    



class DataValiadtion:
    def __init__(self, config1: DataValidationConfig):
        self.config1 = config1


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config1.download_dir)
            all_cols = list(data.columns)

            all_schema = self.config1.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config1.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config1.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

