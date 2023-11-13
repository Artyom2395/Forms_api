import json

from fastapi import FastAPI, HTTPException
from tinydb import TinyDB, Query

from crud import determine_field_type
from schemas import DynamicForm, TemplateModel

app = FastAPI()
db = TinyDB('db.json')
templates_table = db.table('_default')


# API endpoint для получения формы
@app.post('/get_form')
def get_form(form: DynamicForm):
    data = json.loads(form.model_dump_json())
    field_types = {key: determine_field_type(value) for key, value in data.items()}

    template_records = templates_table.all()
    
    for record in template_records:
        template_fields = record['fields']
        
        if all(field in data and field_types[field] == template_fields[field] for field in template_fields):
    # Если условие выполняется, возвращаем имя шаблона
            return record['name']
    # Если подходящий шаблон не найден, возвращаем типы полей
    return field_types

# API endpoint для заполнения таблицы
@app.post('/add_template')
def add_template(template: TemplateModel):
    if templates_table.search(Query().name == template.name):
        raise HTTPException(status_code=400, detail="Template already exists")
    templates_table.insert(template.model_dump())
    return {"status": "Template added"}