import json

def db_open():
    with open("database.json", "r", encoding="utf8") as db_file:
        db = json.load(db_file)
        return db

def db_write(data):
    json_data = json.dumps(data, ensure_ascii=False, indent=4) # Преобразование в JSON
    with open("database.json", "w", encoding= 'utf8') as db_file: # открытие файла на запись
        db_file.write(json_data) # сохранение