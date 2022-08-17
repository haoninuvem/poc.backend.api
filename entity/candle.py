from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from entity_base import Base

class Candle(Base):

    __tablename__ = 'candle'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    symbol = Column(String, nullable=True)
    
    def __repr__(self) -> str:
        return f'''<Candle(id={self.id}, time={self.time}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, symbol={self.symbol})>'''
