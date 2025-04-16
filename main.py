
import requests

TOKEN = "7603610543:AAHZKwI6PUtIlXXrfK7NIpxApG6gM0owxac"  # O'z bot tokeningizni kiriting
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(URL)
data = response.json()  # <-- FUNKSIYA CHAQRILDI

# JSON natijani ekranga chiqarish
print(data)

if "result" in data and len(data["result"]) > 0:
    chat_id = data["result"][0]["message"]["chat"]["id"]
    print(f"Guruh chat ID: {chat_id}")
else:
    print("⚠️ Xatolik: Bot hali hech qanday xabar olmagan! Guruhga xabar yuboring va qayta urinib ko‘ring.")
