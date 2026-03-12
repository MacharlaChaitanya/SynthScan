import requests
from concurrent.futures import ThreadPoolExecutor


def check_directory(target, directory):

    urls = [
        f"http://{target}/{directory}",
        f"https://{target}/{directory}"
    ]

    for url in urls:
        try:
            response = requests.get(url, timeout=5)

            if response.status_code < 400:
                return url

        except:
            pass

    return None


def scan_directories(target, wordlist):

    found_directories = []

    with open(wordlist, "r") as f:
        directories = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=30) as executor:

        results = executor.map(lambda d: check_directory(target, d), directories)

        for result in results:
            if result:
                found_directories.append(result)

    return found_directories
