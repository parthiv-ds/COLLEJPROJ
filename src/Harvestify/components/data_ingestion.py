import os
import sys
import pandas as pd
from Harvestify import logger
from Harvestify.utils.common import get_size
from Harvestify.entity.config_entity import DataIngestionConfig
from pathlib import Path
import sqlite3

class DataIngestion:
    def __init__(self, config1: DataIngestionConfig):
        self.config1 = config1

    def connect_db(self):
        try:
            conn = sqlite3.connect(self.config1.database_path)
            logger.info("database connection successfully")
            query = f'''SELECT * FROM {self.config1.table_name}'''
            df = pd.read_sql_query(query,conn)
            df.to_csv('artifacts1/data_ingestion/crop_recommandation.csv')
            logger.info('csv created successfully')

        except sqlite3.Error as e:
            print("error to connecting databse : {e}")
            return None

        
    
