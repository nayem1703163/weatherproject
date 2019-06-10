from django.shortcuts import render
import requests,json
# Create your views here.
def home(request):
   
    city=request.POST.get('fname')
    url="https://api.apixu.com/v1/current.json?key=ee7a27f7341f4b3984f130912191006&q={}"
    r=requests.get(url.format(city))
    print(r.text)
    rr=json.loads(r.text)
    print(rr)
    try:
        city_weather={

            'tempkey':rr['current']['temp_c'],
            'feelslikekey':rr['current']['feelslike_c'],
            'timekey':rr['location']['localtime'],
            'windspeeddkey':rr['current']['wind_kph'],
            'iconkey':rr['current']['condition']['icon'],
            'citykey':rr['location']['name'],
            }
    except Exception:
        city_weather={
            'errorkey':rr['error']['code'],
            'errorme':rr['error']['message']
        }



    return render(request,'weatherapp/index.html',{'cityweatherkey':city_weather})

   