import urllib.request
import re

def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.request.urlopen(base_url + symbol).read()
    content = content.decode("UTF-8")
    pattern = r'class="pr"[^>]*>[^>]*>(.*)</span>'
    m = re.search(pattern, content)
    if m:
        quote = m.group(1)
        print(symbol, quote)
    else:
        quote = 'no quote available for: ' + symbol
        print(quote)
        
get_quote("IBM")
get_quote("MS")
get_quote("XX")
get_quote("MSFT")
get_quote("ERICB")


1



