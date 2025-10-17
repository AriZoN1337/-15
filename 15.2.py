import tkinter as tk
import requests

def get_facts():
    city = city_entry.get()
    if not city:
        result_label.config(text="Введите название города")
        return
    url = f"https://ru.wikipedia.org/api/rest_v1/page/summary/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        extract = data.get('extract', 'Информация не найдена')
        # Разобьем текст на предложения и возьмем 2 первых
        facts = extract.split('. ')[:2]
        result_label.config(text="\n\n".join(facts))
    else:
        result_label.config(text="Информация не найдена")

root = tk.Tk()
root.title("Исторические факты")

tk.Label(root, text="Введите город:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Получить факты", command=get_facts).pack()

result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack()

root.mainloop()
