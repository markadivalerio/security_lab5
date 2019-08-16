import json
import csv


input_file = "results_grouping.json"
output_file = "analyze_cidr_grouping.csv"

def load_from_file(filename=input_file):
    data = {}
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def write_to_csv(filename=output_file, headers=['ip','data'], data={}):
    with open(filename, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter=',')
        writer.writeheader()
        for ip, info in data.items():
            row = {
                'ip':ip,
                'data':info,
                'ip_count':len(info)
            }
            writer.writerow(row)


def main():
    data = load_from_file(input_file)
    write_to_csv(filename=output_file, headers=['ip','data','ip_count'], data=data)

if __name__ == '__main__':
    main()
