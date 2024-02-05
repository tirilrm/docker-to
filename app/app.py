from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Assuming the first service is running on localhost:5000
FIRST_SERVICE_URL = 'http://book-from.f0hqangcezgveahu.eastus.azurecontainer.io:5000'

@app.route('/')
def home():
	return """
	<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Book Request</title>
	<style>
	body, html {
		height: 100%;
		margin: 0;
		display: flex;
		justify-content: center;
		align-items: center;
		background-color: #b08dc9;
	}
	h1 {
		font-family: comic sans;
		color: #ffffff;
		text-shadow: 2px 2px 4px #000000;
		font-size: 48px;
	}
	</style>
	</head>
	<body>
	<h1>Get Any Book</h1>
	</body>
	</html>
	"""

@app.route("/retrieve_book", methods=['GET'])
def retrieve_book():
    title = request.args.get('title')
    genre = request.args.get('genre')

    if title:
        endpoint = '/get_book'
        params = {'title': title}
    elif genre:
        endpoint = '/get_books_by_genre'
        params = {'genre': genre}
    else:
        return jsonify({'message': 'Please specify a title or genre for searching.'}), 400

    try:
        response = requests.get(FIRST_SERVICE_URL + endpoint, params=params)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e), 'message': 'Could not retrieve book data'}), 500

    return jsonify(response.json())

if __name__ == "__main__":
    # Ensure this runs on a different port than the first Flask app
    app.run(port=5002, debug=True, host='0.0.0.0')
"""
@app.route("/retrieve_book")
def retrieve_book():
    title = request.args.get('title')
    if title:
        try:
            response = requests.get(f"{FIRST_SERVICE_URL}/get_book", params={'title': title})
            response.raise_for_status()  # This will raise an HTTPError if an unsuccessful status code is returned
            return jsonify(response.json())
        except requests.exceptions.RequestException as e:
            return jsonify({
                'message': 'Could not retrieve book data',
                'error': str(e)
            }), 500
    else:
        return jsonify({'message': 'Title parameter is required'}), 400

if __name__ == "__main__":
    app.run(port=5002, debug=True)"""
