# phonenote for Robert (734) 234-0043
from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

 
# @app.route("/handle-key", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def phone_note():
    """Greet Robert and record his message."""

    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say("Hello Robert. Record your message after the tone.")
    resp.record(maxLength="300", action="/handle-recording")
    resp.say("Thank you. Goodbye.")
    return str(resp) 
  
if __name__ == "__main__":
    app.run(debug=True)

####################################################################
# NOTES ############################################################
####################################################################

# https://www.twilio.com/labs/twimlets/voicemail

# https://www.twilio.com/docs/quickstart/python/twiml/record-caller-leave-message