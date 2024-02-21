import requests

def send_sms_request():
    url = 'http://127.0.0.1:5000/receive_sms'  # Update the URL if necessary
    data = {
        'date': '2024-02-21',
        'from': '+1234567890',  # Replace with sender's number
        'id': '123456789',
        'linkId': None,
        'text': 'Hello, this is a test message.',
        'to': '+254728981298',  # Replace with recipient's number
        'networkCode': '63902'  # Replace with appropriate network code
    }

    response = requests.post(url, json=data)
    print(response.text)

