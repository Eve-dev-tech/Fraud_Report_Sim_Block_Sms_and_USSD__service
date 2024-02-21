import africastalking

class send_sms():
    def __init__(self):
        # Initialize Africa's Talking
        africastalking.initialize(
            username='eve_mso',
            api_key='838ca732de22718f677c45bc820f9ae5eb5387b6328689ee90fa4e07ee6f2279'
        )
        self.sms = africastalking.SMS

    def sending(self):
        # Set the numbers in international format
        recipients = ["+254728981298"]  # Replace with recipient's number
        # Set your message
        message = "Hey AT Ninja!"
        # Set your shortCode or senderId
        sender = "56536"  # Your short code
        try:
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')
send_sms_instance = send_sms()
send_sms_instance.sending()
