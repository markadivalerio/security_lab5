import sys
import json
import ipaddress
from ipwhois import IPWhois


ip_file = 'results.csv'
new_file = 'results_whois.txt'
results = {}
whoisips = {}
errors = {}

def get_whois(ip):
    obj = IPWhois(ip)
    res = ''
    try:
        res = obj.lookup_whois(ip)
    except Exception as ex:
        res = {"error":{
            "type": type(ex).__name__,
            "args": ex.args
}}
    return '"' + ip + '": ' + json.dumps(res)

def append_to_file(newline):
    with open(new_file, 'a+') as f:
        f.write(newline)


def main():
    firstTime = True
    with open(ip_file, 'r') as f:
        line = f.readline()
        while line:
            append_to_file('{') if firstTime else append_to_file(',')
            ip = line.strip()
            whois = get_whois(ip)
            append_to_file(whois)
            line = f.readline()
            firstTime = False
        append_to_file('}')

if __name__ == "__main__":
    main()
