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
