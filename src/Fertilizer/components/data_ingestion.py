import os
import sys
import pandas as pd
from Fertilizer import logger
from Fertilizer.utils.common import get_size
from Fertilizer.entity.config_entity import DataIngestionConfig
from pathlib import Path
import sqlite3

class DataIngestion:
    def __init__(self, config2: DataIngestionConfig):
        self.config2 = config2

    def connect_db(self):
        try:
            conn = sqlite3.connect(self.config2.database_path)
            logger.info("database connection successfully")
            query = f'''SELECT * FROM {self.config2.table_name}'''
            df = pd.read_sql_query(query,conn)
            df.to_csv('artifacts2/data_ingestion/Fertilizer_Prediction.csv')
            logger.info('csv created successfully')

        except sqlite3.Error as e:
            print("error to connecting databse : {e}")
            return None

        
    
