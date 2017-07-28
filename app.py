import os
# Using Flask since Python doesn't have built-in session management
from flask import Flask, session

app = Flask(__name__)

# Generate a secret random key for the session
app.secret_key = os.urandom(24)

# Define a route for the webserver
@app.route('/')
def index():
	return "hello world!"
  # file = open("index.html", "r")
  # return file.read()


if __name__ == '__main__':
	app.run( 
        host="0.0.0.0",
       port=int("80")
  )
