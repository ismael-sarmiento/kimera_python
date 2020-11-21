# sqlacodegen mysql://root:Maximus.Ismael.1993@localhost:3306/world
# coding: utf-8
from sqlalchemy import CHAR, Column, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

MetadataWorld = MetaData(schema="world")
BaseWorld = declarative_base(metadata=MetadataWorld)


class Sample(BaseWorld):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True)
    name = Column(CHAR)

# class Country(BaseWorld):
#     __tablename__ = 'country'
#
#     Code = Column(CHAR(3), primary_key=True, server_default=text("''"))
#     Name = Column(CHAR(52), nullable=False, server_default=text("''"))
#     Continent = Column(Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'),
#                        nullable=False, server_default=text("'Asia'"))
#     Region = Column(CHAR(26), nullable=False, server_default=text("''"))
#     SurfaceArea = Column(Float(10), nullable=False, server_default=text("'0.00'"))
#     IndepYear = Column(SmallInteger)
#     Population = Column(Integer, nullable=False, server_default=text("'0'"))
#     LifeExpectancy = Column(Float(3))
#     GNP = Column(Float(10))
#     GNPOld = Column(Float(10))
#     LocalName = Column(CHAR(45), nullable=False, server_default=text("''"))
#     GovernmentForm = Column(CHAR(45), nullable=False, server_default=text("''"))
#     HeadOfState = Column(CHAR(60))
#     Capital = Column(Integer)
#     Code2 = Column(CHAR(2), nullable=False, server_default=text("''"))
#
#
# class City(BaseWorld):
#     __tablename__ = 'city'
#
#     ID = Column(Integer, primary_key=True)
#     Name = Column(CHAR(35), nullable=False, server_default=text("''"))
#     CountryCode = Column(ForeignKey('country.Code'), nullable=False, index=True, server_default=text("''"))
#     District = Column(CHAR(20), nullable=False, server_default=text("''"))
#     Population = Column(Integer, nullable=False, server_default=text("'0'"))
#
#     country = relationship('Country')
#
#
# class Countrylanguage(BaseWorld):
#     __tablename__ = 'countrylanguage'
#
#     CountryCode = Column(ForeignKey('country.Code'), primary_key=True, nullable=False, index=True,
#                          server_default=text("''"))
#     Language = Column(CHAR(30), primary_key=True, nullable=False, server_default=text("''"))
#     IsOfficial = Column(Enum('T', 'F'), nullable=False, server_default=text("'F'"))
#     Percentage = Column(Float(4), nullable=False, server_default=text("'0.0'"))
#
#     country = relationship('Country')
