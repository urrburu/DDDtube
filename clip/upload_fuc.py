import requests


url = 'https://api.twitch.tv/kraken/clips/'
headers = { 'Accept': 'application/vnd.twitchtv.v5+json', 'Client-ID': 'gsu4z8hkdn2xlqgbyye6rzogo3t5o5'}
def get_data(clipID):
    return requests.get(url=url+clipID, headers=headers).json()




def urlCut(add):
    urllist = str(add).split("/")
    if "?" in urllist[-1]:
        urllist = urllist[-1].split("?")
        return urllist[0]
    else:
        return urllist[-1]


