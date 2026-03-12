import requests


def detect_technology(target):

    technologies = []

    urls = [
        f"http://{target}",
        f"https://{target}"
    ]

    try:
        response = None

        for url in urls:
            try:
                response = requests.get(url, timeout=5)
                break
            except:
                continue

        if not response:
            return technologies

        headers = response.headers
        html = response.text.lower()

        # Detect server
        if "server" in headers:
            technologies.append(f"Server: {headers['server']}")

        # Detect PHP
        if "php" in html or "x-powered-by" in headers and "php" in headers["x-powered-by"].lower():
            technologies.append("Language: PHP")

        # Detect WordPress
        if "wp-content" in html or "wordpress" in html:
            technologies.append("Framework: WordPress")

        # Detect React
        if "react" in html:
            technologies.append("Framework: React")

        # Detect jQuery
        if "jquery" in html:
            technologies.append("Library: jQuery")

    except:
        pass

    return technologies