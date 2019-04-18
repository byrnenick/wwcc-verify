from flask import Flask, jsonify, request
from wwcc_vic_verify import verify, testing

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello world"

@app.route('/victoria/', methods=['POST', 'GET'])
def victoria():
	
	lastname = request.args.get("lastname")
	cardnumber = request.args.get("cardnumber")

	try:
		result = verify(cardnumber, lastname)
		return jsonify(result)
	except:
		return "Something went wrong"


@app.route('/test/', methods=['POST', 'GET'])
def test():

	lastname = request.args.get("lastname")
	cardnumber = "1573624A-01"

	try:
		result = testing(cardnumber, lastname)
		return jsonify(result)
	except: 
		response = {
			"message" : "Verify function failing",
			"lastname" : lastname,
			"cardnumber" : cardnumber
		}
		return jsonify(response)
	


#demo data, 1573624A-01