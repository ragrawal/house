import pandera as pa
from pandera import DataFrameModel
from pandera.typing import Series


class HouseData(pa.DataFrameModel):
  LotFrontage: Series[float] = pa.Field(nullable=True, coerce=True)
  LotArea: Series[float] = pa.Field(nullable=True, coerce=True)
  YearBuilt: Series[int] = pa.Field(description="Year built. Have to prior 2024", lt=2024, coerce=True)
  SaleType: Series[str] = pa.Field(description = "Sale type", nullable=False, coerce=True)

  class Config:
      to_format = "dict"
      to_format_kwargs = {"orient": 'records'}
      from_format = "dict"
  


class HousePredictionData(pa.DataFrameModel):
  price: Series[float] = pa.Field(description="Predicted price", nullable=False, coerce=True)
  is_valid: Series[bool] = pa.Field(description="Is the prediction valid", nullable=False, coerce=True)
  info: Series[str] = pa.Field(
    description="Additional information", 
    nullable=True, 
    coerce=True
  )

  class Config:
    to_format = "dict"
    to_format_kwargs = {"orient": "records"}


