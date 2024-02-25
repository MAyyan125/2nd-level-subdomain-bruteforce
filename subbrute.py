# #!/usr/bin/env python3
import argparse
import subprocess

class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

def parse_arguments():
    parser = argparse.ArgumentParser(description="Automate subdomain brute-forcing on second-level domains")
    parser.add_argument("-f", "--file", help="Specify file path to bruteforce subdomains for")
    parser.add_argument("-a", "--argument", help="Specify Arguments here", type=str)
    return parser.parse_args()

def subfinder(args):
    if args.file:
        with open(args.file) as file:
            for domain in file:
                result = subprocess.run(["subfinder", "-all", f"-{args.argument}", domain.strip()], capture_output=True, text=True)
                print(Color.CYAN + result.stdout, end="")

def main():
    args = parse_arguments()
    print(f"{Color.PURPLE}Author: M. Ayyan Irfan\n{Color.RESET}")
    subfinder(args)

if __name__ == "__main__":
    main()
