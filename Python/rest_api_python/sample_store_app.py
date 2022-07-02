# POST /store/data: {name:}
# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:,price:}
# GET /store/<string:name>/item

from flask import Flask, jsonify,render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "This is a Test Page"

app.run(port=5000)
