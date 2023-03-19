'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request, redirect, url_for, Flask, render_template

import settings
from chatgpt import GPT
import os

app = Flask(__name__)
# 设
app.config.from_object(settings.DevelopmentConfig)
# 
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'xamdjqowid%Y@*IKOJ@QHdoabdiuawn3w5'


# frontpage
@app.route('/')
def index():
    ''' display a link to the general query page '''
    # 
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # run if post
    if request.method == 'POST':
        # acess acount
        name = request.form.get('username')
        # acess password
        password = request.form.get('password')
        # Determine account password
        if name == 'jane doe' and password == '123':
            return render_template('center.html')
        else:
            return render_template('error.html')


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        # acess the question
        question = request.form['question']
        answer = 'Sorry, reenter again'
        return render_template('response.html', question=question, answer=answer)
    else:
        return render_template('center.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
