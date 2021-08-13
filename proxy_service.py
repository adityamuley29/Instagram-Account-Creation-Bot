# Config = {
#     "proxy_server" : "input your proxy server"  #213.168.210.76 sample proxy server to prevent instagram's ip ban
# }
import requests
import csv
import concurrent.futures

proxylist = []

with open ('http_proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    try:
        r = requests.get('https://httbin.org/ip',proxies={'http':proxy,'https':proxy},timeout=2)
        print(r.json(),' - working')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as exector:
    exector.map(extract,proxylist)
    print(len(proxylist))
 