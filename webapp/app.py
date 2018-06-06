from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/hello/<name>')
def hello_there(name):
    from datetime import datetime
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # You normally use templates instead of inline HTML, as discussed later in the tutorial
    html_content = "<html><head><title>Hello, Flask</title></head><body>"
    html_content += "<strong>Hello there, " + name + "!</strong>. It's " + formatted_now
    html_content += "</body></html>"

    return html_content