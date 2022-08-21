#b
from flask import Flask,request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():

    return request.form



app.run(host="0.0.0.0",debug=True,port=80)
