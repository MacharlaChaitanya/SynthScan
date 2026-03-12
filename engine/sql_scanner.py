import requests


def scan_sql_injection(target):

    payload = "' OR '1'='1"

    test_urls = [
        f"http://{target}/?id={payload}",
        f"https://{target}/?id={payload}"
    ]

    error_signatures = [
        "sql syntax",
        "mysql",
        "syntax error",
        "warning",
        "unterminated",
        "odbc",
        "database error"
    ]

    for url in test_urls:

        try:
            response = requests.get(url, timeout=5)

            content = response.text.lower()

            for error in error_signatures:
                if error in content:
                    return True

        except:
            pass

    return False