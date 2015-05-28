from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

 
@app.route("/handle-key", methods=['GET', 'POST'])
def phone_note():
    """Greet Robert and record his message."""

    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say("Hello Robert. Record your message after the tone.")
    resp.record(maxLength="300", action="/handle-recording")
    return str(resp) 
 
@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
    recording_url = request.values.get("RecordingUrl", None)
    resp = twilio.twiml.Response()
    resp.say("Thank you. Goodbye.")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)