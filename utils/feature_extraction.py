from urllib.parse import urlparse
import re

def extract_features(url):

    features = []

    # URL Length
    features.append(len(url))

    # HTTPS
    features.append(1 if "https" in url else 0)

    # @ Symbol
    features.append(1 if "@" in url else 0)

    # Dot Count
    features.append(url.count("."))

    # Hyphen Count
    features.append(url.count("-"))

    # Slash Count
    features.append(url.count("/"))

    # Digit Count
    features.append(sum(c.isdigit() for c in url))

    # Suspicious Words
    suspicious_words = [
        "login",
        "verify",
        "bank",
        "secure",
        "account",
        "update",
        "free",
        "bonus",
        "paypal"
    ]

    features.append(
        1 if any(word in url.lower() for word in suspicious_words) else 0
    )

    # IP Address Detection
    ip_pattern = r'\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b'

    features.append(
        1 if re.search(ip_pattern, url) else 0
    )

    # Domain Length
    domain = urlparse(url).netloc

    features.append(len(domain))

    return features