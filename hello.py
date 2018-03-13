from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

def send_simple_message(email):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxf5408fd6870549fc863e18d26f946d68.mailgun.org/messages",
	    auth=("api", "key-71bfe116b9dac75bd114d13e77e7e349"),
	    data={"from": "Jenny <mailgun@sandboxf5408fd6870549fc863e18d26f946d68.mailgun.org>",
	          "to": [email], 
	          "subject":"Hello",
	          "text": "Check 1!"})


@app.route("/")
def hello():
	return "Hello World again"

@app.route("/qq/<name>")
def hello_someone(name):
	return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def ghfghfh():
	form_data = request.form
	print form_data["email"]
	print form_data["your_name"]
	send_simple_message(form_data["email"])
	return "<h1>Hi</h1><p> I am edu</p>"

app.run(debug=True)