import requests
import json
from dotenv import load_dotenv

print("|чтоб выйти напишите '/exit'|")
while True:
	city = input("Введите город:")
	api = "d7c04b2ac6cc63d9d53ac2c9888fc215"
	url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric&lang=ru"

	try:
		if city.lower() == "/exit":
			print("досвидания :)")
			break
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			print("___________________")
			print(f"результаты города '{city}' показывают:")
			print(f"температура: {data['main']['temp']}°C")
			print(f"Ветер: {data['wind']['speed']} м/с")
			print(f"Влажность: {data['main']['humidity']}%")
			print("___________________")
		else:
			print("|ошибочка| :< 'Попробуйте написать правильнее?'")
			pass

	except requests.exceptions.ConnectionError:
		print("Нет интернета! Проверьте подключение.")
	except requests.exceptions.Timeout:
		print("Сервер не отвечает. Попробуйте позже.")
	except Exception as e:
		print(f"Неожиданная ошибка: {e}")