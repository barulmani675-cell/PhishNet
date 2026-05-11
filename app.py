from flask import Flask, render_template, request
import re
import time
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url'].lower()

    time.sleep(2)

    suspicious_keywords = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "paypal",
        "bonus",
        "free",
        "account"
    ]

    phishing_score = 0
        # Suspicious domains
    blacklist = [
        "paypal-login",
        "free-bonus",
        "secure-bank",
        "verify-account",
        "crypto-win",
        "lottery",
        "gift-card"
    ]

    # Dangerous TLDs
    dangerous_tlds = [
        ".xyz",
        ".tk",
        ".ru",
        ".top",
        ".gq"
    ]

    # Check suspicious words
    for word in suspicious_keywords:
        if word in url:
            phishing_score += 1

    # Check @ symbol
    if "@" in url:
        phishing_score += 1

    # Check IP address
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    if re.search(ip_pattern, url):
        phishing_score += 1

    # Check URL length
    if len(url) > 75:
        phishing_score += 1
            # Check blacklist words
    for item in blacklist:
        if item in url:
            phishing_score += 2

    # Check dangerous domains
    for tld in dangerous_tlds:
        if tld in url:
            phishing_score += 1

    # Final prediction
        # Final prediction
    if phishing_score >= 2:

        confidence = min(95, 60 + phishing_score * 10)

        result = f"⚠️ Phishing Website Detected ({confidence}% Dangerous)"

    else:

        confidence = max(85, 95 - phishing_score * 5)

        result = f"✅ Legitimate Website ({confidence}% Safe)"

    return render_template(
        'index.html',
        prediction_text=result
    )


if __name__ == "__main__":
    app.run(debug=True)