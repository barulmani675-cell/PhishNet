from urllib.parse import urlparse

def extract_features(url):

    features = []

    # URL Length
    features.append(len(url))

    # HTTPS Check
    features.append(1 if "https" in url else 0)

    # @ Symbol Check
    features.append(1 if "@" in url else 0)

    # Dot Count
    features.append(url.count("."))

    return features