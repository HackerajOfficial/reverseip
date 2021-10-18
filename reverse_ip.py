import requests
import argparse

parser = argparse.ArgumentParser(description='A Python Based Reverse IP Script To Find The Domains On The Server. Coded By Hackeraj')
parser.add_argument('site', type=str, help='Site Link: raaz.info.np')
args = parser.parse_args()

def reverseiplookupsUsingHackerTarget(site):
    URL = "https://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=URL, website=site)
    r = requests.get(combo)
    counter = 0
    content = r.text
    sites = content.split("\n")

    for i in sites:
        if i:
            counter += 1

    print("Total Sites Hosting on the Server[" + str(counter) + "]")
    print(content)
# #print(dir(r)) #To know the all we can access 

reverseiplookupsUsingHackerTarget(args.site)
