import requests


def scan_xss(target):

    payload = "<script>alert('XSS')</script>"

    test_urls = [
        f"http://{target}/?q={payload}",
        f"https://{target}/?q={payload}"
    ]

    for url in test_urls:

        try:
            response = requests.get(url, timeout=5)

            if payload in response.text:
                return True

        except:
            pass

    return False