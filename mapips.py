import json
import ipaddress
from ipwhois import IPWhois


ip_file = 'results.csv'
new_file = 'results_with_others.csv'
results = {}
whoisips = {}
errors = {}

def getcidr(ip):
    obj = IPWhois(ip)
    res = None
    try:
        res = obj.lookup_whois()
    except Exception as e:
        errors[ip] = str(e)
        return

    if(ip not in whoisips):
        whoisips[ip] = []
    if(ip not in results):
        results[ip] = [ip]
    for net in res['nets']:
        if('cidr' in net and net['cidr']):
            ip_cidrs = net['cidr'].split(', ')
            for ip_cidr in net['cidr'].split(', '):
                whoisips[ip].append(ipaddress.ip_network(ip_cidr))

def checkip(ip):
    found = False
    ipobj = ipaddress.IPv4Address(ip)
    for origin_ip, cidr_list in whoisips.items():
        for cidr in cidr_list:
            if ipobj in cidr:
                results[origin_ip].append(ip)
                found = origin_ip
                break
    return found


def main():
    with open(ip_file, 'r') as fp:
        line = fp.readline()
        while line:
            ip = line.strip()
            origin_ip = checkip(ip)
            if origin_ip:
                print(ip + ' found to belong to ' + origin_ip)
            else:
                getcidr(ip)
            line = fp.readline()
    print(str(len(results)))
    jsonstr = json.dumps(results)
    f = open('results_grouping.json','w')
    f.write(jsonstr)
    f.close()

    print(str(len(errors)))
    errstr = json.dumps(errors)
    f = open('results_errors.json', 'w')
    f.write(errstr)
    f.close()

if __name__ == "__main__":
    main()
