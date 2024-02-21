from flask import request
from app import app
from send_sms import send_sms
from receive_sms import receive_sms
from flask import jsonify

@app.route('/')
def index():
    # Example home page route
    return "Welcome to my SMS app!"

@app.route('/send_sms')
def send_sms_route():
    send_sms_instance = send_sms()
    send_sms_instance.sending()
    return "SMS sent!"

@app.route('/receive_sms', methods=['POST'])
def receive_sms_route():
    data = request.get_json(force=True)
    if data:
        receive_sms_instance = receive_sms(data)
        response = receive_sms_instance.process_message()
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid JSON payload'}), 400



@app.route('/fetch_messages')
def fetch_messages():
    try:
        # Define the Africa's Talking API endpoint and your credentials
        FETCH_MESSAGES_URL = "https://api.africastalking.com/version1/user?username=eve_mso"
        USERNAME = "eve_mso"
        API_KEY = "838ca732de22718f677c45bc820f9ae5eb5387b6328689ee90fa4e07ee6f2279"

        # Make GET request to fetch messages
        response = request.get(FETCH_MESSAGES_URL, params={'username': USERNAME, 'apiKey': API_KEY, 'lastReceivedId': 0})
        response_data = response.json()

        # Check if messages are fetched successfully
        if 'SMSMessageData' in response_data:
            messages = response_data['SMSMessageData']['Messages']
            # Process fetched messages as needed
            return jsonify({'messages': messages}), 200
        else:
            return jsonify({'error': 'Failed to fetch messages'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
