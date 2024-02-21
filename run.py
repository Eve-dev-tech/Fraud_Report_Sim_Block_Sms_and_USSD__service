from app import app
import os
from send_sms_request import send_sms_request
if __name__ == "__main__":
    app.run(debug=True, port = os.environ.get("5000"))


#call the send_sms_request function
send_sms_request()