# Python projects

import requests as rt
import tkinter as tk
from tkinter import messagebox


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return  # stops the function

    url = "http://api.weatherapi.com/v1/current.json"

    # PASTE YOUR NEW KEY STRIP OF ALL EXTRA BRACKETS OR SPACES HERE
    params = {
        "key": "2bfd1e9064724d7cbd5115322262106",  # Please enter your api key here from "wetherapi.com".
        "q": city,
        "aqi": "no"
    }

    try:
        response = rt.get(url, params=params, timeout=10)

        # FIXED: Catching server restriction errors before data extraction prevents the crash
        if response.status_code != 200:
            messagebox.showerror("API Error",
                                 f"Server returned Status Code {response.status_code}.\nYour API key might still be activating or blocked.")
            return

        weather_data = response.json()

        current = weather_data["current"]
        location = weather_data["location"]

        result_title.config(text=f"{location['name']}, {location['country']}")
        temp_label.config(text=f"{current['temp_c']}°C")
        cond_label.config(text=f"Condition: {current['condition']['text']}")
        humidity_label.config(text=f"Humidity: {current['humidity']}%")

    except rt.exceptions.RequestException as err:
        messagebox.showerror("Network Error", f"Could not connect to server.\nDetails: {err}")
    except ValueError:
        # Catch unexpected string responses cleanly without throwing a system popup box
        messagebox.showerror("Format Error",
                             "Server sent back unreadable HTML web text instead of weather data numbers.")
    finally:
        print('program executed...')

# --- GUI Window Setup ---
try:
    if 'root' in locals() or 'root' in globals():
        root.destroy()
except tk.TclError:
    pass
except NameError:
    pass

root = tk.Tk()
root.title("Weather App")
root.geometry("350x400")
root.config(bg="grey15")

title_label = tk.Label(root, text="Live Weather Tracker", font=("Arial", 16, "bold"), bg="black", fg="white")
title_label.pack(pady=15)

city_entry = tk.Entry(root, font=("Arial", 14), width=20, justify="center")
city_entry.pack(pady=5)
city_entry.insert(0, "Jabalpur")

search_btn = tk.Button(
    root,
    text="Check Weather",
    font=("Arial", 11, "bold"),
    bg="sky blue",
    fg="white",
    padx=10,
    pady=5,
    command=get_weather
)
search_btn.pack(pady=10)

BACKGROUND_COLOR = "light gray"  # Options: "white", "black", "azure", "snow", etc.
TITLE_COLOR = "dark slate gray"  # Options: "navy", "black", "dim gray", etc.
TEMP_COLOR = "crimson"  # Options: "red", "dark orange", "blue", etc.
TEXT_COLOR = "dark gray"  # Python reads "gray40" as charcoal/dark gray

# Update your main window background to match
root.configure(bg=BACKGROUND_COLOR)

# Your weather app labels
result_title = tk.Label(root, text="", font=("Arial", 14, "bold"), bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
result_title.pack(pady=10)

temp_label = tk.Label(root, text="", font=("Arial", 28, "bold"), bg=BACKGROUND_COLOR, fg=TEMP_COLOR)
temp_label.pack(pady=5)

cond_label = tk.Label(root, text="", font=("Arial", 12), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
cond_label.pack(pady=2)

humidity_label = tk.Label(root, text="", font=("Arial", 12), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
humidity_label.pack(pady=2)

root.mainloop()
