import vt
import requests

# https://developers.virustotal.com/reference/url-info
url_id = vt.url_id("https://centraldigital.cattelecom.com")
url = "https://www.virustotal.com/api/v3/urls/" + url_id

headers = {
    "accept": "application/json",
    "x-apikey": "a1c249cc58928d253b323571273fad720d45c73497d696b6a75df7c5064285fd"
}

response = requests.get(url, headers=headers)

print(response.text)

# https://virustotal.github.io/vt-py/quickstart.html
client = vt.Client("a1c249cc58928d253b323571273fad720d45c73497d696b6a75df7c5064285fd")

url_id = vt.url_id("https://dg.th/")    # aHR0cHM6Ly9kZy50aC8 
url = client.get_object("/urls/{}", url_id)
print(url_id)

print(url.last_analysis_stats)

analysis = client.scan_url('https://dg.th/')
print(analysis)

client.close()
