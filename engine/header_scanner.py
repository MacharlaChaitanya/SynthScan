import requests


def scan_security_headers(target):

    headers_to_check = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Referrer-Policy"
    ]

    missing_headers = []

    urls = [
        f"http://{target}",
        f"https://{target}"
    ]

    for url in urls:

        try:
            response = requests.get(url, timeout=5)

            for header in headers_to_check:
                if header not in response.headers:
                    missing_headers.append(header)

            break

        except:
            pass

    return missing_headers