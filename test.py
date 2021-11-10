import requests
URL = "http://localhost:63342/Wie_wird_bgcolor_ausgewertet/Test_html.html?_ijt=idol3lpcrgln1hmkuo8qn2sv25&_ij_reload=RELOAD_ON_SAV"
data = requests.get(URL)

print(data)

