import sys

import joblib
import pandas as pd
from loguru import logger
from pydantic import BaseModel


class BatchInference(BaseModel):
    model_file: str

    def __call__(self) -> None:

        # Get Data
        logger.info("...Downloading data")
        df = pd.read_csv('https://raw.githubusercontent.com/melindaleung/Ames-Iowa-Housing-Dataset/master/data/ames%20iowa%20housing.csv')

        # load model
        logger.info("...Loading model")
        model = joblib.load(self.model_file)

        # Infer
        logger.info("...Inferring")
        y_predicted = model.predict(df)

        # dump data
        logger.info("...Dumping data")
        y_predicted.to_csv('predictions.csv', index=False)


if __name__ == '__main__':
    BatchInference(model_file=sys.argv[1])()
