class receive_sms():
    def __init__(self, data):
        self.date = data.get('date')
        self.sender = data.get('from')
        self.message_id = data.get('id')
        self.link_id = data.get('linkId')
        self.message = data.get('text')
        self.recipient = data.get('to')
        self.network_code = data.get('networkCode')

    def process_message(self):
        if self.message.lower() =="Hello":
            return {"response": "Welcome to Mpesa SecureSim Service!"}
        else:
            return{"Kimekuramba": "Invalid message!"}

        