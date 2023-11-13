from pydantic import BaseModel
from typing import Dict

# Класс запроса с динамическими атрибутами
class DynamicForm(BaseModel):
    class Config:
        extra = "allow"
        
class TemplateModel(BaseModel):
    name: str
    fields: Dict[str, str]