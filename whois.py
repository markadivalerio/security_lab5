#!/usr/bin/env python3
import os
import sys
import json
import ipaddress
from ipwhois import IPWhois


ip_file = 'results.csv'
new_file = 'results_whois.txt'
results = {}
whoisips = {}
errors = {}

def get_whois(ip): # and ping
    obj = IPWhois(ip)
    res = {}
    try:
        res = obj.lookup_whois(ip)
        res['error_type'] = None
        res['error_args'] = None
    except Exception as ex:
        res = {"error_type": type(ex).__name__,
               "error_args": ex.args}
    response = os.system("ping -c 1 " + ip)
    res['pingable'] = bool(response == 0)
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
