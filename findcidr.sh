#! /bin/bash

while read line; do
  CIDRSTR=`whois $line | grep "CIDR"`
  CIDR=${CIDRS//CIDR:\s*/}
  printf "%s,%s" "$line" "$CIDR" 
done <results.csv > results_with_cidr.csv
