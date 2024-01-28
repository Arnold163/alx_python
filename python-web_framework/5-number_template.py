#lets on flask now
""" maybe this type of documantation?"""
from flask import Flask, render_template

#create a flask app instance
app = Flask(__name__)
""" maybe this type of documantation?"""
#define and use strict
@app.route('/', strict_slashes=False)
def hello_hbnb():
    #what else am i to document here
    return 'Hello HBNB!'
#run the flask app if script is executed 
""" maybe this type of documantation?"""

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'
#route for text
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    processed_text = text.replace('_', ' ')
    return 'C {}' .format(processed_text)

#route for Python is cool
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text='is cool'):
    processed_text = text.replace('_', ' ')
    return 'Python {}' .format(processed_text)

#route for numbers
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return '{} is a number'.format(n)

#route for template
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number_template.html', n=n)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)