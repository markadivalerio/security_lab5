#!/usr/bin/env python3

import json
import csv


#input_file = "results_grouping.json"
input_file = "results.csv"
output_file = "analyze_results_everything.csv"

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
        for idx, row in data.items():
            writer.writerow(row)

def analyze_ip_cidr(data):
    fmt_data = {}
    print("ok")
    for ip, info in data.items():
        fmt_data[ip] = {
            'ip': ip,
            'ip_count':len(info)
            'data':info
        }
    return fmt_data


def analyze_whois(data):
    fmt_data = {}
    for ip, info in data.items():
        #fmt_data['ip'] = {
        #    'ip':
    return fmt_data


def main():
    data = load_from_file(input_file)
    fmt_data = analyze_ip_cidr(data)
    write_to_csv(filename=output_file, data=fmt_data)

if __name__ == '__main__':
    main()
