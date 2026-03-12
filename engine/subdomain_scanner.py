import socket
from concurrent.futures import ThreadPoolExecutor


def check_subdomain(domain, sub):

    subdomain = f"{sub}.{domain}"

    try:
        socket.gethostbyname(subdomain)
        return subdomain

    except:
        return None


def scan_subdomains(domain, wordlist):

    found = []

    with open(wordlist, "r") as f:
        subs = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=50) as executor:

        results = executor.map(lambda s: check_subdomain(domain, s), subs)

        for result in results:
            if result:
                found.append(result)

    return found