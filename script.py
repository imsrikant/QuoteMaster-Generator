from sys import argv, exit
import requests

API = 'https://api.kanye.rest'

def main():
    ...

def check_argv(argv):
    if len(argv) > 2:
        exit("Pass only one argument")

    if len(argv) == 1:
        return 1

    if not argv[1].isdigit():
        exit("Enter number to print that many quotes")

    return int(argv[1])

def generate_quote(numbers=1):
    raw_quotes = []
    for _ in range(numbers):
        response = requests.get('https://api.kanye.rest')
        if response.status_code == 200:
            data = response.json()
            raw_quotes.append(data)
        else:
            exit("Failed")
    return raw_quotes
