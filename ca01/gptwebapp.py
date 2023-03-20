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
def home(name='Chris'):
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1 style="font-family:verdana">GPT Web App</h1>
        <ul>
            <li>
                <a style="font-family:verdana;font-size:30px" href=" 'about', name=name)}">About</ a>
            </li>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('team', name=name)}">Team</ a>
            </li>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('index', name=name)}">Index</ a>
            </li>
            <li>
                <a style="font-family:verdana;font-size:30px" href="{url_for('form', name=name)}">Form</ a>
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
                <pre style="font-size:25px">This is a simple web application that uses OpenAI's GPT API to generate text based on user prompts.
                <br>My program can generating an image according to your prompt</pre>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</ a>
        '''
    elif name == 'Chris':
        return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <pre style="font-size:25px">This is a simple web application that uses OpenAI's GPT API to generate text based on user prompts.
                <br>My program can paraphrase texts according to your prompt</pre>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</ a>
        '''
    else:
         return f'''
            <h1 style="font-family:verdana">About My Web App</h1>
            <ul>  
                <pre style="font-size:25px">This is a simple web application that uses OpenAI's GPT API to generate text based on user prompts.</pre>
            </ul>
            <a style="font-family:verdana;font-size:20px" href="{url_for('home',name=name)}">Back to main</ a>
        '''


@app.route('/team')
def team():
    ''' display the team page '''
    print('processing /team route')
    name = request.args.get('name')
    return f'''
        <h1 style="font-family:verdana">Team 28</h1>
        <ul>
            <p style="font-family:Courier New;font-size:25px">Tim Xing</p >
            <ul>
                <li><p style=d"font-family:Courier New;font-size:20px">Captain, made a GPT Web App that can generate an image according to the prompt</p ></li>
            </ul>
            <p style="font-family:Courier New;font-size:25px">Chris Liang</p >
            <ul>
                <li><p style=d"font-family:Courier New;font-size:20px">Made a GPT Web App that can paraphrase texts according to the prompt</p ></li>
            </ul>
            <p style="font-family:Courier New;font-size:25px">Matthew Yue</p >
            <p style="font-family:Courier New;font-size:25px">Yishan Gao</p >
            <p style="font-family:Courier New;font-size:25px">Tingwei Pu</p >
        </ul>
        <a style="font-family:verdana;font-size:20px" href="{url_for('home', name=name)}">Back to main</ a>
    '''

@app.route('/index')
def index():
    ''' display the team-members page '''
    print('processing /team route')
    name = request.args.get('name')
    return f'''
        <h1 style="font-family:verdana">Pages of our members</h1>
        <ul>
            <li><a style="font-family:Courier New;font-size:20px" href="{url_for('home', name='Tim')}">Tim</ a></li>
            <li><a style="font-family:Courier New;font-size:20px" href="{url_for('home', name='Chris')}">Chris</ a></li>
        </ul>
        <a style="font-family:verdana;font-size:20px" href="{url_for('home', name=name)}">Back to main</ a>
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
            response = f'< img src="data:image/png;base64,{image_data}"/>'
        elif name == 'Chris':
            response = g.recipe(prompt)
        else:
            response = 'Error: Invalid name'
        return f'''
        <h1 style="font-family:verdana">GPT Web App</h1>
        <pre style="font-size:20px">Your prompt is "{prompt}"</pre>
        <hr>
        <pre style="font-size:20px">Here is the answer</pre>
        {response}
        <p><a style="font-family:verdana;font-size:20px" href={url_for('form', name=name)}>Make another query</ a>
        <br><a style="font-family:verdana;font-size:20px" href="{url_for('home', name=name)}">Back to main</ a></p >
        '''
    else:
        return '''
        <h1 style="font-family:verdana">GPT Web App</h1>
        <p style="font-family:verdana;font-size:20px">Enter your query below</p >
        <form method="post">
            <textarea name="prompt"></textarea>
            <p style="font-family:Courier New;font-size:30px"><input type=submit value="Get response">
        </form>
        '''

if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)
    