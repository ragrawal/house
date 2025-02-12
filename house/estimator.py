from typing import Self

import numpy as np
import numpy.typing as npt
import pandas as pd
import pandera as pa
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

from house.schema import HouseData, HousePredictionData


class HousePredictionModel:

  @pa.check_types
  def transform(self, raw_x: HouseData) -> pd.DataFrame:
    x = pd.DataFrame()
    x.loc[:, 'LotFrontage'] = raw_x['LotFrontage'].fillna(self.mean_frontage)
    x.loc[:, 'LotArea'] = np.log1p(raw_x['LotArea'])
    x.loc[:, 'YearBuilt'] = 2024 - raw_x['YearBuilt'].astype(int)
    x.loc[:, 'SaleType'] = self.sale_type_encoder.transform(raw_x['SaleType'])
    return x

  @pa.check_types
  def fit(self, raw_x: HouseData, raw_y: HousePredictionData) -> Self:
    self.sale_type_encoder = LabelEncoder().fit(raw_x['SaleType'])
    self.mean_frontage = raw_x['LotFrontage'].mean()
    self.model = LinearRegression()
    self.model.fit(self.transform(raw_x), raw_y)
    return self

  @pa.check_types
  def predict(self, raw_x: HouseData) -> HousePredictionData:
    price = self.model.predict(self.transform(raw_x))
    return HousePredictionData.validate(
      pd.DataFrame({
        'price': price,
        'is_valid': (price > 0),
        'info': None
      })
    )
