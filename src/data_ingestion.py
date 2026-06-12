import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)
TEST_SIZE = 0.8

def split_data():
    try:
        logger.info("Starting data ingestion process")
        logger.info("Starting the splitting process")
        os.makedirs(RAW_DIR, exist_ok=True)
        data = pd.read_csv(RAW_FILE_PATH)
        train_data , test_data = train_test_split(data , test_size=1-TEST_SIZE, random_state=42)

        train_data.to_csv(TRAIN_FILE_PATH)
        test_data.to_csv(TEST_FILE_PATH)

        logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
        logger.info(f"Test data saved to {TEST_FILE_PATH}")
        
    except Exception as e:
        logger.error("Error while splitting data")
        raise CustomException("Failed to split data into training and test sets ", e)
    
    finally:
        logger.info("Data ingestion completed")

    
    
if __name__ == "__main__":
    split_data()
    

