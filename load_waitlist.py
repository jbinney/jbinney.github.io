import urllib, json
url = "https://api.robinhood.com/midlands/tailgate/mcduckling/spot/joe%40robinhood.com/"
response = urllib.urlopen(url)
data = json.loads(response.read())
total = data.get("spot_number_total")
print data
html = '<html><body style="font-size: 200px; display: flex; align-items: center; justify-content: center"><div>{:,}</div></body></html>'.format(total)
file = open("waitlist.html", "w")
file.write(html)
file.close()
