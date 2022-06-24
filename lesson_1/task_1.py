#from urllib.parse import urlparse as urlp
def domain_name(url):
    if "//" in url:
       url = url.split("//")[1].split(".")
    else: 
       url = url.split(".")
    #url = urlp(url).hostname.split(".") 
    domain = url[1] if url[0] == "www" else url[0]
    return domain

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

