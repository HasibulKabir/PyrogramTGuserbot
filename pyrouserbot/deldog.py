import requests, json
def haste(TEXT):
      url = "https://del.dog/documents"
      r = requests.post(url, data=TEXT.encode("UTF-8")).json()
      url = f"https://del.dog/{r['key']}"
      print(url)
      return url

def paste(TEXT):
      url = "https://del.dog/documents"
      r = requests.post(url, data=str(TEXT)).json()
      url = f"https://del.dog/{r['key']}"
      print(url)
      return url
