from flask import Flask, jsonify, request
# import pickle as pck

app = Flask(__name__)
@app.route('/', methods=['POST'])
def results():
    data = request.get_json(force=True)
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=9000, debug=True)