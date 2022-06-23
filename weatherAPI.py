# Reading and Printing Temperature of a given name using API.

import requests
# import validateByOTP
# validateByOTP.getOTPAndValidate()
print((city := input("Enter City Name to find temperature:")), eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e6b7427f8bf97526adf2869093c7509c&units=metric").text)['main']['temp'])
