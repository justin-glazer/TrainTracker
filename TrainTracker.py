import requests

station = input("Enter Station Name: ")
words = station.split()
url = ""

if len(words) == 2:
    url = "https://www.njtransit.com/dv-to/" + words[0] + "%20" + words[1]
elif len(words) == 3:
    url = "https://www.njtransit.com/dv-to/" + words[0] + "%20" + words[1] + "%20" + words[2]
elif len(words) == 4:
    url = "https://www.njtransit.com/dv-to/" + words[0] + "%20" + words[1] + "%20" + words[2] + "%20" + words[3]
else: #only wayne route 23
    url = "https://www.njtransit.com/dv-to/Wayne%2FRoute%2023%20Transit%20Center%20Rail%20Station"

response = requests.get(url)
html_content = response.text
str = html_content.index("class=\"d-block ff-secondary--bold flex-grow-1 h2 mb-0\"")
print(html_content[str+84:str+92])