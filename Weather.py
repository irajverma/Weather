import requests
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from PIL import Image, ImageTk  # Import PIL for image handling

def get_location(city_name):
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city_name)  # Use the city name provided by the user
        print(location)  # Debugging line
        return location.latitude, location.longitude
    except Exception as e:
        print(f"Error: {e}")  # Debugging line
        messagebox.showerror("Error", f"Unable to detect location: {e}")
        return None, None

def get_weather(latitude, longitude):
    api_key = ""  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data["name"]
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"].capitalize()
            return city, temperature, weather
        else:
            messagebox.showerror("Error", f"Unable to retrieve weather data: {data.get('message', 'Unknown error')}")
            return None, None, None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None, None, None

def show_weather():
    city_name = city_entry.get()  # Get the city name from the entry widget
    latitude, longitude = get_location(city_name)

    if latitude is not None and longitude is not None:
        city, temperature, weather = get_weather(latitude, longitude)

        if city and temperature and weather:
            weather_label.config(text=f"City: {city}\nTemperature: {temperature}°C\nCondition: {weather}")

# GUI setup
app = tk.Tk()
app.title("Weather Forecast")
app.geometry("400x400")
app.configure(bg="#e0f7fa")  # Light cyan background

# Load and set background image
# Uncomment the following lines if you have a background image
# Load and set background image
# Uncomment the following lines if you have a background image
background_image = Image.open("D:\python_project\internship\snowy.jpg")  # Replace with your image path
background_image = background_image.resize((400, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title Label
title_label = tk.Label(app, text="Weather Forecast", font=("Helvetica", 20, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10)

# City Entry Frame
entry_frame = tk.Frame(app, bg="#e0f7fa")
entry_frame.pack(pady=10)

city_label = tk.Label(entry_frame, text="Enter City Name:", font=("Helvetica", 14), bg="#e0f7fa", fg="#00796b")
city_label.pack(side=tk.LEFT, padx=5)

city_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=15)
city_entry.pack(side=tk.LEFT, padx=5)

# Weather Information Label
weather_label = tk.Label(app, text="Weather information will appear here.", font=("Helvetica", 14), justify="center", bg="#e0f7fa", fg="#00796b")
weather_label.pack(pady=20)

# Refresh Button
refresh_button = tk.Button(app, text="Get Weather", command=show_weather, font=("Helvetica", 14), bg="#4db6ac", fg="white", activebackground="#00796b")
refresh_button.pack(pady=20)

app.mainloop()
