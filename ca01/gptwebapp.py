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
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a> <p>
        <a href="{url_for('About')}">About</a> <p>
        <a href="{url_for('team')}">Team</a> <p>
        <a href="{url_for('indexpage')}">Index</a> <p>
        <a href="{url_for('formpage')}">Form Page</a> <p>    
    '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a> <p>
        <a href="/">Main page</a > <p>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        <a href="/">Main page</a > <p>
        '''
    
    
@app.route('/About')
def About():
    print('processing / route')
    return f'''
        <h1>About</h1>
        <p>This is Team 28's CA01. </p >
        <p> This is a Web app using Flask which uses promot engineering to generate useful reponses. </p >
        <p> Motivation: gpt-based webapps using prompt engineering have already
          started to appear and 
          this assignment is meant to learn how to write such apps 
          as well as gaining experience using git for a team project. <p>

        <!--enter links to other pages here-->
        <br>
        <a href="/">Main page</a >
    '''
    
@app.route('/team')
def team():
    print('processing / route')
    return f'''
        <h1>Team Page</h1>
        <p>Team 28</p >
        <li>Tim Xing(Captain) </li>
        <li>Chris Liang </li>
        <li>Matthew Yue </li>
        <li>Yishan Gao </li>
        <li>Tingwei Pu: I created the website frame(about, team and index pages) 
            and wrote the <strong>getEconomyOutlook</strong> method. </li>
        <br>
        <a href="/">Main page</a >
    '''


@app.route('/indexpage')
def indexpage():
    print('processing / route')
    return f'''
        <h1>Index Page</h1>
        <p>Team 28</p >
        <li>Tim Xing(Captain) </li>
        <li>Chris Liang </li>
        <li>Matthew Yue </li>
        <li>Yishan Gao </li>
        <li>Tingwei Pu: <a href="{url_for('getEconomyOutlook')}"> Get the Economy Outlook</a> <p>  </li>
        <br>
        <a href="/">Main page</a >
        '''

@app.route('/formpage')
def formpage():
    print('processing / route')
    return f'''
        <h1>Form Page</h1>
        <p>Team 28</p >
        <li>Tim Xing(Captain) </li>
        <li>Chris Liang </li>
        <li>Matthew Yue </li>
        <li>Yishan Gao </li>
        <li>Tingwei Pu:  <a href="{url_for('getEconomyOutlook')}"> </li>
        <br>
        <a href="/">Main page</a >
    '''


#Author: Tingwei Pu 
# To generate the the economy outlook of a country 
@app.route('/indexpage/getEconomyOutlook', methods=['GET', 'POST'])
def getEconomyOutlook():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getEconomyOutlook(prompt)
        return f'''
        <h1>Economy Outlook Analysis from ChatGPT </h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        <pre style="border:thin solid black; white-space: pre-wrap;">{answer}</pre>
        <p>
        <a href=' '> Make another query</a >
        <br> <p>
        <a href="/">Main page</a > <p>
        '''
    else:
        return '''
        <h1>Generate the Economy Outlook</h1>
        Enter which country's current economic outlook you want to analyze:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    

@app.route('/formpage/getEconomyOutlook')
def show_result(result):
    result_url = url_for('show_result')
    return f'The processed result is: {result}'




if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)