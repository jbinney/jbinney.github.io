import urllib, json
url = "https://api.robinhood.com/midlands/tailgate/mcduckling/spot/joe%40robinhood.com/"
response = urllib.urlopen(url)
data = json.loads(response.read())
total = data.get("spot_number_total")
print data
html = '<html><body><div style="font-size: 200px; text-align: center">{:,}</div></body></html>'.format(total)
file = open("waitlist.html", "w")
file.write(html)
file.close()
