
# coding: utf-8

# In[15]:


import json #pass python dictionary to JSON object
import os   #allow to use OS functionality within your code
import requests #library of flash are run in heroku

from flask import Flask    #flask is a micro web framework for python -> 
#it is mircro because it is not depmd on the complex library or other frame work
#provide tools or web library to implement web application
from flask import request
from flask import make_response

#create an instance of flask
app = Flask(__name__)

#when webhook is hit, the 'decorator' will call fucntion that we need
#@app.route('/webhook', methods=['POST'])

#MIME Types คือมาตรฐานการสื่อสารของเอกสาร มีไว้สำหรับระบุให้ Web Browser รู้ว่าไฟล์ที่กำลังติดต่อสื่อสารกับ Server นั้นคือไฟล์รูปแบบใด เช่นไฟล์ text ไฟล์รูปภาพ ไฟล์วิดิโอ เป็นต้น
#webhook น่าจะเป็นตัวที่คอยเชื่อมต่อ appl เรากับ service เพื่อคอยแจ้งเตือยว่ามีอะไรใหม่เกิดขึ้น
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    
    
    res = makeResponse(req) #query the OpenWhether API -> construct response -> send to Dialogflow
    res = json.dumps(res, indent=4)          
    r = make_response(res)  #make_response -> format the data from OpenWhether in the form that Dialog flow understand
    r.headers['Content-Type']='application/json' #JSON format return to Dialog flow
    return r
    
def makeResponse(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameter.get("date")
  
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=981f641dada50e4ea04b036fa1671772')
    json_object = r.json()
    whether = json_object['list']
    for i in range(0,30):
        if date in whether[i]['dt_txt']:
            condition = weather[i]['whether'][0]['description']
        
    speech = "The forcase for "+city+" for "+daye+" is "
    return {"speech": speech,
           "displayText": speech,
           "source": "apiai-whether-webhook"}


if __name__ == '__main__': #condition to get the flash app to run
    port = int(os.getenv('PORT', 5000)) #default port with flask
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0') #to have server available externally, so dialog flow will hit it with post requestst
    

