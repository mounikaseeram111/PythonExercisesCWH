from win32com.client import Dispatch
import requests
import json
from newsapi import NewsApiClient

def speak(str):

    speak = Dispatch("SAPI.SpVoice")
    #speak.Speak("Hare Krishna Hare Krishna, Krishna Krishna Hare Hare , Hare Rama Hare Rama , Rama Rama Hare Hare")
    speak.Speak(str)


if __name__ == '__main__':
    # url = ("https://newsapi.org/v2/top-headlines?country=us&apiKey=b7c2b1f4fbd24158906226b73e5cc79c")
    # req = requests.get(url)
    # #print(type(req.text))
    # JsonArr = json.loads(req.text)
    # #print(JsonArr)
    # for i in range(10):
    #     speak(JsonArr['articles'][i]['description'])

    # using newApi pacakge
    newsapi = NewsApiClient(api_key='b7c2b1f4fbd24158906226b73e5cc79c')
    #sources = newsapi.get_sources()
    top_headlines = newsapi.get_top_headlines(q='covid',
                                              category='health',
                                              language='en',
                                              country='in')
    for i in range(10):
        speak(top_headlines['articles'][i]['description'])
