import requests
import re
import argparse

def get_crt(domain):
    URL = "https://crt.sh/?q={domain}&output=json"
    response = requests.get(URL.format(domain=domain))
    if response.status_code == 200:
        return response.json()
    else:
        print("Error")

def parse_crt(data):
    subdomains = set()
    for item in data:
        subdomains.add(item["name_value"])
    return subdomains

def main():
    data = get_crt(domain)
    subdomains = parse_crt(data)
    for subdomain in subdomains:
        print(subdomain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get subdomains from crt.sh")
    parser.add_argument("-d", "--domain", help="Domain name")
    args = parser.parse_args()
    domain = args.domain
    data = get_crt(domain)
    subdomains = parse_crt(data)
    for subdomain in subdomains:
        print(subdomain)

