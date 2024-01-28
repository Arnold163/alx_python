#lets on flask now
from flask import Flask

#create a flask app instance
app = Flask(__name__)

#define and use strict
@app.route('/', strict_slashes=False)
def hello_hbnb():
    #what else am i to document here
    return 'Hello HBNB!'
#run the flask app if script is executed 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)