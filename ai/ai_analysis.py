def ai_security_analysis(results):

    analysis = []

    if "SQL Injection" in results:
        analysis.append(
            "The application appears vulnerable to SQL Injection which may allow attackers to access database data."
        )

    if "Missing Headers" in results:
        analysis.append(
            "Missing security headers may expose the application to clickjacking and XSS attacks."
        )

    if "Open Ports" in results:
        analysis.append(
            "Open ports indicate exposed services that could increase the attack surface."
        )

    if not analysis:
        analysis.append("No major vulnerabilities detected.")

    return "\n".join(analysis)