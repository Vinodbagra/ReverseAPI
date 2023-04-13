from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_string():
   input_string = request.json.get('input_string')
   reversed_string = input_string[::-1]
   return {'reversed_string': reversed_string}

if __name__ == '__main__':
    app.run(debug=False)