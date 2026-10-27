import json
def show_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        file.write("hello")
        
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)
        
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []