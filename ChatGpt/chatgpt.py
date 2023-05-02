'''
Demo code for interacting with GPT-3 in Python.

To run this you need to
* first visit openai.com and get an APIkey,
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell 
% python gpt.py
'''
import openai
import os
import base64
import requests
from io import BytesIO

class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self, apikey):
        ''' store the apikey in an instance variable '''
        self.apikey = apikey
        # Set up the OpenAI API client
        openai.api_key = "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" #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"
        self.image_model = "image-alpha-001"

    def getResponse(self, prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def generateImage(self, prompt):
        ''' Generate an image from the prompt '''
        result = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",
            model=self.image_model,
            response_format="url"
        )

        img = Image.open(BytesIO(requests.get(result['data'][0]['url']).content))
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return img_str
    
    def paraphrase(self,course):
        ''' Generate a paraphrase for a sentence '''
        prompt = 'genrate a paraphrase for ' + course
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        response = completion.choices[0].text
        return response 

if __name__=='Yishan':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
