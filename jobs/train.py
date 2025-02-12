import joblib
import pandas as pd
from loguru import logger
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from house.estimator import HousePredictionModel


class SubOptimalModelError(Exception):
    pass

class Train:

    def __call__(self) -> None:
        # Step 1: Get Data -- 
        # todo: pull database from BigQuery or feature store
        logger.info("...Downloading data")
        df = pd.read_csv('https://raw.githubusercontent.com/melindaleung/Ames-Iowa-Housing-Dataset/master/data/ames%20iowa%20housing.csv')

        # Train Model
        logger.info("...Training model")
        df_train, df_eval = train_test_split(df, test_size=0.1)
        model = HousePredictionModel()
        model.fit(df_train, df_train['SalePrice'])

        # Evaluate Model
        logger.info("...Evaluating model")
        y_predicted = model.predict(df_eval)
        score = mean_absolute_error(df_eval['SalePrice'], y_predicted['price'])
        if score > 1E8:
            raise SubOptimalModelError(f"Model did not converge. MAE = {score}")

        # Serialize Model
        # todo: push model to model registry
        logger.info("...Serializing model")
        joblib.dump(model, 'model.pkl')


if __name__ == '__main__':
    Train()()
