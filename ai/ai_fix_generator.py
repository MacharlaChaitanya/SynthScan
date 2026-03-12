def generate_fixes(results):

    fixes = []

    if "SQL Injection" in results:
        fixes.append(
            "Use parameterized queries or prepared statements to prevent SQL injection."
        )

    if "Missing Headers" in results:
        fixes.append(
            "Add security headers like Content-Security-Policy and X-Frame-Options."
        )

    if "Open Ports" in results:
        fixes.append(
            "Close unnecessary ports or restrict them using firewall rules."
        )

    if not fixes:
        fixes.append("No critical fixes required.")

    return "\n".join(fixes)