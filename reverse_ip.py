import requests

def reverseiplookupsUsingHackerTarget(site):
    URL = "https://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=URL, website=site)
    r = requests.get(combo)
    print(r.text)
# #print(dir(r)) #To know the all we can access

site = input("URL:")
reverseiplookupsUsingHackerTarget(site)
