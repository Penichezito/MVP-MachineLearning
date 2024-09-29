from pydantic import BaseModel
from typing import Optional, List
from model.laptop import Laptop
import json
import numpy as np

class LaptopSchema(BaseModel):
    """ Define como um novo laptop a ser inserido deve ser representado
    """
    Manufacturer: str = "Dell G15"
    Category: int = 3
    Screen: str = "Full HD"
    GPU: int = 148
    os: int = 35
    CPU_core: int = 2
    Screen_Size_inch: float = 39.685
    CPU_Frequency: float = 0.627
    RAM_GB: int = 8
    Storage_GB_SSD: float = 2.2
    Price: int = 1100

    
class LaptopViewSchema(BaseModel):
    """Define como o modelo de laptop será retornado
    """
    id: int = 1
    Manufacturer: str = "Dell"
    Category: int = 3
    Screen: str = "Full HD"
    GPU: int = 148
    os: int = 35
    CPU_core: int = 2
    Screen_Size_inch: float = 39.685
    CPU_Frequency: float = 0.627
    RAM_GB: int = 8
    Storage_GB_SSD: int = 256
    weigth_kg: float =2.2
    Price: int = 1100
    Recomendation: int= None

    
class LaptopSearchSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base na marca do Notebook.
    """
    manufacturer: str = "Dell"

class ListLaptopSchema(BaseModel):
    """Define como uma lista de laptops será representada
    """
    laptops: List[LaptopSchema]

    
class LaptopDelSchema(BaseModel):
    """Define como um laptop para deleção será representado
    """
    manufacturer: str = "Dell"
    
# Apresenta apenas os dados de um laptop   
def presentation_laptop(laptop: Laptop):
    """ Retorna uma representação do produto seguindo o schema definido em
        LaptopViewSchema.
    """    
    return {
      "id": laptop.id,
      "manufacturer": laptop.manufacturer,
      "category": laptop.category,
      "screen": laptop.screen,
      "gpu": laptop.gpu,
      "os": laptop.os,
      "cpu_core": laptop.cpu_core,
      "screen_size_inch": laptop.screen_size_inch,
      "cpu_frequency": laptop.cpu_frequency,
      "ram_gb": laptop.price,
      "storage_gb_ssd": laptop.storage_gb,
      "weight_kg": laptop.weight_kg,
      "price": laptop.price,
      "recomendation":laptop.recomendation
    }
   
    # Apresena uma lista de laptops
def presentation_laptops(laptops: List[Laptop]):
    """ Retorna uma representação de um laptop seguindo o schema definido em
        LaptopViewSchema.
  """
    result = []
    for laptop in laptops:
        result.append({
        "id": laptop.id,
        "manufacturer": laptop.manufacturer,
        "category": laptop.category,
        "screen": laptop.screen,
        "gpu": laptop.gpu,
        "os": laptop.os,
        "cpu_core": laptop.cpu_core,
        "screen_Size_inch": laptop.screen_size_inch,
        "cpu_frequency": laptop.cpu_frequency,
        "ram_gb": laptop.price,
        "storage_gb_ssd": laptop.storage_gb,
        "weight_kg": laptop.weight_kg,
        "price": laptop.price,
        "recomendation": laptop.recomendation
        })

    return {"laptops": result}