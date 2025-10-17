import tkinter as tk
import requests

API_KEY = "ваш_ключ_от_OpenWeatherMap"

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Введите название города")
        return
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        result_label.config(text=f"Погода в {city}:\n{temp}°C, {description}")
    else:
        result_label.config(text="Город не найден или ошибка API")

root = tk.Tk()
root.title("Погода")

tk.Label(root, text="Введите город:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Получить погоду", command=get_weather).pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
