#!/usr/bin/env python3

import json
import csv


#input_file = "results_grouping.json"
input_file = "aws/results_grouping.json"
output_file = "aws/results_grouping.csv"

def load_from_file(filename=input_file):
    data = {}
    with open(filename, 'r') as json_file:
        if ".json" in filename:
            data = json.load(json_file)
    return data

def write_to_csv(filename, fmt_data):
    if not fmt_data:
        print("no data to write to csv")
        return
    headers = list(fmt_data.values())[0].keys()
    with open(filename, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=',')
        writer.writeheader()
        for idx, row in fmt_data.items():
            writer.writerow(row)

def analyze_ip_cidr(data):
    fmt_data = {}
    print("ok")
    for ip, info in data.items():
        fmt_data[ip] = {
            'ip': ip,
            'ip_count':len(info),
            'data':info
        }
    return fmt_data

def analyze_grouping(data):
    fmt_data = {}
    for ip, info in data.items():
        fmt_data[ip] = {
            'ip': ip,
            'ip_count':len(info),
            'data':info
        }
    return fmt_data


#def analyze_whois(data):
#    fmt_data = {}
#    for ip, info in data.items():
        #fmt_data['ip'] = {
        #    'ip':
#    return fmt_data


def main():
    data = load_from_file(input_file)
    fmt_data = analyze_grouping(data)
    #fmt_data = analyze_ip_cidr(data)
    write_to_csv(output_file, fmt_data)

if __name__ == '__main__':
    main()
