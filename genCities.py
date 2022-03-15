import requests


alerts = requests.get("https://www.oref.org.il//Shared/Ajax/GetAlarmsHistory.aspx?lang=he&mode=3").json()
places = []
for alert in alerts:
    if (alert['data'] not in places):
        places += [alert['data']]
file = open("places.txt", 'w', encoding='utf-8')
file.write("\n".join(places))
file.close()
