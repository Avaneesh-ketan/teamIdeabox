import flask
from flask import Flask, request

app = flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/submit">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f'Thank you for submitting your name: {name} and email: {email}!'

if __name__ == '__main__':
    app.run(debug=True)
