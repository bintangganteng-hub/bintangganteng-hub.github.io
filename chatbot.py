import random
import urllib.request
import json

def sapaan():
    sapaan = ["Halo!", "Hai!", "Selamat datang!", "Apa kabar?"]
    return random.choice(sapaan)

def get_weather(city):
    try:
        # Ganti dengan API key Anda jika diperlukan
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=AIzaSyDIF622TSXxQWdfCmdHZEZI4M3mMffGf-c"
        with urllib.request.urlopen(api_url) as url:
            data = json.loads(url.read().decode())
            if data["cod"] == 200:
                description = data["weather"][0]["description"]
                temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
                return f"Cuaca di {city}: {description}, suhu: {temperature:.2f} °C"
            else:
                return "Kota tidak ditemukan."
    except Exception as e:
        print(e)
        return "Maaf, terjadi kesalahan saat mengambil data cuaca."

def respon_pertanyaan(pertanyaan):
    pertanyaan = pertanyaan.lower()
    if "nama kamu siapa" in pertanyaan:
        return "Saya adalah chatbot sederhana."
    elif "apa kabar" in pertanyaan:
        return "Saya baik-baik saja, terima kasih sudah bertanya!"
    elif "terima kasih" in pertanyaan:
        return "Sama-sama!"
    elif "selamat tinggal" in pertanyaan:
        return "Sampai jumpa lagi!"
    elif "cuaca di" in pertanyaan:
        city = pertanyaan.split("cuaca di ")[1]
        return get_weather(city)
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda."

def main():
    print(sapaan())
    while True:
        pertanyaan = input("Anda: ")
        if pertanyaan.lower() == "berhenti":
            print("Chatbot: Sampai jumpa!")
            break
        else:
            jawaban = respon_pertanyaan(pertanyaan)
            print("Chatbot:", jawaban)

if __name__ == "__main__":
    main()
