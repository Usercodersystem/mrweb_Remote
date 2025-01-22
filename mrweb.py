from requests import get,post
from json import loads
from urllib.parse import urlencode

def test():
  return "mrweb remote library"

def ai(text,urlencode=True):
  txt=urlencode({"text":text})
  return get(f"http://api4dev.ir/ai/?{txt}").text
