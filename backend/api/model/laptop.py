from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Laptop(Base):
    __tablename__ = "laptops"

    id = Column(Integer, primary_key=True)
    manufacturer = Column("Manufacturer", String(50))
    category = Column("Category", Integer)
    screen = Column("Screen", Integer)
    gpu = Column("GPU", Integer)
    os = Column("OS", Integer)
    cpu_core = Column("Cpu Core", Integer)
    screen_size_inch = Column("Screen Size inch", Float)
    cpu_frequency = Column("CPU Frequency", Float)
    ram_gb = Column("RAM_GB", Integer)
    storage_gb = Column("Storage GB", Integer)
    weight_kg = Column("Weight kg", Float)
    price = Column("Price", Integer)
    recomendation = Column("Recomendation", Integer, nullable=True)
    date_insertion = Column(DateTime, default=datetime.now())
    
    
    def __init__(self, manufacturer:int, category:int, screen:int, gpu:int,
                 os:int, cpu_core:int, screen_size_inch:float, 
                 cpu_frequency:float, ram_gb:int, storage_gb:int, weight_kg: float,
                 price:int, recomendation:int,
                 date_insertion:Union[DateTime, None] = None):
        """
        Cria um Laptop

        Arguments:
        Manufacturer: marca do laptop
            category: categoria a que pertece o laptop
            screen:top de tela
            os: pressão sanguínea
            cpu_core: espessura da pele
            screen_size_inch: tamanho da tela
            cpu_frequency: frequencia de velocidade de processamento da cpu
            ram_gb: quantidade de memoria ram
            storage_gb: armazenamento em gb do laptop
            weight_kg: peso do laptop
            price:preço do laptop
            recomendation: Classficação Binária de recomendação onde (0 = "Não", 1 = "Sim")
            date_insertion: data de quando o laptop foi inserido à base
        """
        self.manufacturer = manufacturer
        self.category = category
        self.screen = screen
        self.gpu = gpu
        self.os = os
        self.cpu_core =cpu_core
        self.screen_size_inch = screen_size_inch
        self.cpu_frequency = cpu_frequency
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.weight_kg = weight_kg
        self.price = price
        self.recomendation = recomendation
        self.date_insertion = date_insertion

        # se não for informada, será o data exata da inserção no banco
        if date_insertion:
            self.data_insertion = date_insertion