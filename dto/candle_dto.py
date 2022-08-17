# {
#     "_raw": {
#       "t": "2022-05-02T04:00:00Z",
#       "o": 156.65,
#       "h": 158.23,
#       "l": 153.27,
#       "c": 157.96,
#       "v": 122281905,
#       "n": 1145056,
#       "vw": 156.036188
#     }
#   }

from pydantic import Field, BaseModel

class CandleDto(BaseModel):

    open: float = Field(description="Open price")
    high: float = Field(description="High price")
    low: float = Field(description="Low price")
    close: float = Field(description="Close price")
    volume: float = Field(description="Volume")
    timestamp: str = Field(description="Timestamp")
    symbol: str = Field(description="Symbol")
