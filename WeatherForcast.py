# key :- 6c76cb95610a3d0adad20784b3218eec
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
"""
def get_weather(city):
    weather_key = '6c76cb95610a3d0adad20784b3218eec'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params={'APPID':weather_key,'q':city,'units':'Metric'}
    response = requests.get(url,params=params)
    print(response.json())
"""

import tkinter as tk
import requests
from tkinter import ttk

HEIGHT = 500
WIDTH = 600


def get_weather(city):
    weather_key = '6c76cb95610a3d0adad20784b3218eec'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    try:
        location = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        humidity = weather['main']['humidity']

        result_text = f"Location: {location}\nConditions: {description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        label['text'] = result_text
    except Exception as e:
        label['text'] = "The retrieval of weather information\nhas encountered an unforeseen obstacle.\nWe kindly request you to\nprovide your input once more"


root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")

background_image = tk.PhotoImage(file="finalbg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Forecast", font=(
    'Courier', 15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18),
                 borderwidth=2, bg='systemTransparent')
label.place(relwidth=1, relheight=1)

root.mainloop()
