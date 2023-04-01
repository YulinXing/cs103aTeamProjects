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
# import you own gpt file and create an instance in the form below 
from gpt import GPT
import os

app = Flask(__name__)
g = GPT((os.environ.get('APIKEY')))

@app.route('/')
@app.route('/<name>')
def home(name='Tim'):
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1 style="font-family:verdana">GPT Web App</h1>
        <ul>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('about', name=name)}">About</a>
            </li>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('team', name=name)}">Team</a>
            </li>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('index', name=name)}">Index</a>
            </li>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('form', name=name)}">Form</a>
            </li>
        </ul>
    '''

@app.route('/about')
def about():
    ''' display the about page '''
    print('processing /about route')
    name = request.args.get('name')
    if name=='Tim':
        return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <p style="font-family:verdana; font-size:25px">Can generating an image according to your prompt</p>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</a>
        '''
    elif name=='Chris':
        return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <p style="font-family:verdana;; font-size:25px">Can paraphrase texts according to your prompt</p>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</a>
        '''
    elif name=='Matthew':
        return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <p style="font-family:verdana;; font-size:25px; word-wrap: break-word">Created a GPT Web App to correct the spelling, grammar, and punctuation of a user inputted prompt</p>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</a>
        '''
    elif name=='Tingwei':
        return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <p style="font-family:verdana;; font-size:25px; word-wrap: break-word">Created the website frame(About, Team and Index pages) and wrote the <strong>getEconomyOutlook</strong> method</p>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</a>
        '''
    else:
         return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <p style="font-size:25px">This is a simple web application that uses OpenAI's GPT API to generate text based on user prompts.</p>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</a>
        '''


@app.route('/team')
def team():
    ''' display the team page '''
    print('processing /team route')
    name = request.args.get('name')
    return f'''
        <h1>About our team</h1>
        <ul>
            <p style="font-family:verdana; font-size:25px">This is Team 28's CA01.</p>
            <p style="font-family:verdana; font-size:25px">This is a Web app using Flask which uses promot engineering to generate useful reponses.</p>
            <p style="font-family:verdana; font-size:25px; word-wrap: break-word">Motivation: gpt-based webapps using prompt engineering have already started to appear and this assignment is meant to learn how to write such apps, as well as gaining experience using git for a team project.</p>
        </ul>
        <ul>
            <p style="font-family:verdana;font-size:25px">Tim Xing(Captain)</p>
            <p style="font-family:verdana;font-size:25px">Chris Liang</p>
            <p style="font-family:verdana;font-size:25px">Matthew Yue</p>
            <p style="font-family:verdana;font-size:25px">Yishan Gao</p>
            <p style="font-family:verdana;font-size:25px">Tingwei Pu</p>
        </ul>
        <a style="font-family:verdana;font-size:20px" href="{url_for('home', name=name)}">Back to main</a>
    '''

@app.route('/index')
def index():
    ''' display the team-members page '''
    print('processing /team route')
    name = request.args.get('name')
    return f'''
        <h1 style="font-family:verdana">Pages of our members</h1>
        <ul>
            <li><a style="font-family:verdana;font-size:25px" href="{url_for('home', name='Tim')}">Tim</a></li>
            <li><a style="font-family:verdana;font-size:25px" href="{url_for('home', name='Chris')}">Chris</a></li>
            <li><a style="font-family:verdana;font-size:25px" href="{url_for('home', name='Matthew')}">Matthew</a></li>
            <li><a style="font-family:verdana;font-size:25px" href="{url_for('home', name='Tingwei')}">Tingwei</a></li>
        </ul>
        <a style="font-family:verdana;font-size:20px" href="{url_for('home', name=name)}">Back to main</a>
    '''


@app.route('/form', methods=['GET', 'POST'])
def form():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    name = request.args.get('name')
    if request.method == 'POST':
        prompt = request.form['prompt']
        if name == 'Tim':
            image_data = g.generateImage(prompt)
            response = f'<img src="data:image/png;base64,{image_data}"/>'
        elif name == 'Chris':
            response = g.paraphrase(prompt)
        elif name == 'Matthew':
            response = g.editString(prompt, "fix grammar, spelling, punctuation")
        elif name == 'Tingwei':
            response = g.getEconomyOutlook(prompt)
        else:
            response = 'Error: Invalid name'
        return f'''
        <h1 style="font-family:verdana">GPT Web App</h1>
        <pre style="font-size:20px">Your prompt is "{prompt}"</pre>
        <hr>
        <pre style="font-size:20px">Here is the answer: </pre>
        <p style="font-family:verdana; font-size:30px; word-wrap: break-word">{response}</p>
        <p><a style="font-family:verdana;font-size:20px" href={url_for('form', name=name)}>Make another query</a>
        <br><a style="font-family:verdana;font-size:20px" href="{url_for('home', name=name)}">Back to main</a></p>
        '''
    else:
        return '''
        <h1 style="font-family:verdana">GPT Web App</h1>
        <p style="font-family:verdana;font-size:20px">Enter your query below</p>
        <form method="post">
            <textarea name="prompt"></textarea>
            <p style="font-family:Courier New;font-size:30px"><input type=submit value="Get response">
        </form>
        '''
    
if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)