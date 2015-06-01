# phonenote for Robert (734) 234-0043
# https://stormy-taiga-7073.herokuapp.com
from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

 
# @app.route("/handle-key", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def phone_note():
    """Greet Robert and record his message."""

    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say("Hello Robert. Record your message after the tone. Press any key to finish recording.")
    # Play an mp3 NOT WORKING, HTTP ERRORS
    # resp.play("phonenote_Robert.mp3")
    # maxLength 3600 = one hour
    resp.record(maxLength="3600", action="/handle-recording", finishOnKey="")
    return str(resp)

@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
 
    resp = twilio.twiml.Response()
    resp.say("Thank you. Goodbye.")
    # Play an mp3 NOT WORKING, HTTP ERRORS
    # resp.play("phonenote_Robert_goodbye.mp3")

    return str(resp)
  
if __name__ == "__main__":
    app.run(debug=True)

####################################################################
# NOTES ############################################################
####################################################################

# https://www.twilio.com/labs/twimlets/voicemail

# https://www.twilio.com/docs/quickstart/python/twiml/record-caller-leave-message