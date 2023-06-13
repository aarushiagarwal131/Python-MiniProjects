import win32com.client as wincom
import requests
import json

city = input("Enter the name of the city\n")


def fun(url):
    r = requests.get(url)
    print(r.text)
    dic = json.loads(r.text)
    w = dic["current"]["temperature"]
    return w


if __name__ == '__main__':
    tinyurl = f"http://api.weatherstack.com/current?access_key=e140c3001f16bb472c8301d43fb83587&query={city}"
    speaker = wincom.Dispatch("SAPI.SpVoice")
    speaker.Speak(f"The current temperature in {city} is {fun(tinyurl)} degrees")
    
