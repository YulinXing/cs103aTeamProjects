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
# 设置运行环境未开发环境
app.config.from_object(settings.DevelopmentConfig)
# 调用GPT的类，实例化一个gptAPI的对象
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'xamdjqowid%Y@*IKOJ@QHdoabdiuawn3w5'


# 首页
@app.route('/')
def index():
    ''' display a link to the general query page '''
    # 渲染模板index.html
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 如果请求方法为POST则执行下列代码
    if request.method == 'POST':
        # 获取账号
        name = request.form.get('username')
        # 获取密码
        password = request.form.get('password')
        # 判断如果账号为张三，密码为123，（这里我把账号密码写死，也可以和数据库连接变成动态）则跳转到访问中心页面
        if name == '张三' and password == '123':
            return render_template('center.html')
        else:
            return render_template('error.html')


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        # 获取输入框里面的问题内容
        question = request.form['question']
        # 通过调用GPT的方法获取返回内容，但因为需要GPT账号，故无法实现
        # answer = gptAPI.getResponse(prompt)
        answer = '对不起，您输入的内容有误，请重新输入！！！'
        # 渲染模板，并把参数传递至模板中
        return render_template('response.html', question=question, answer=answer)
    else:
        return render_template('center.html')


if __name__ == '__main__':
    # 在500这个端口启动项目
    app.run(debug=True, port=5000)
