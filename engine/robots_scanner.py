import requests


def scan_robots(target):

    urls = [
        f"http://{target}/robots.txt",
        f"https://{target}/robots.txt"
    ]

    paths = []

    for url in urls:
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:

                lines = response.text.split("\n")

                for line in lines:
                    if "Disallow:" in line:
                        path = line.split(":")[1].strip()
                        paths.append(path)

                break

        except:
            pass

    return paths