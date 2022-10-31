from flask import Flask, request
import urllib.request
import asyncio
import datetime
import time
import logging
import json

logfile = 'mediaapp.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile,\
    level=logging.DEBUG)

app = Flask(__name__)

"""
#@app.route("/test")
#def social_network_activityTest():
#    # TODO: your code here
#    json_response = {}
#    return json_response
"""


@app.route("/")
async def social_network_activity():
    """
    Using async and await
    Changelog

    Routes, error handlers, before request, after request,
    and teardown functions can all be coroutine functions
    if Flask is installed with the async extra (pip install flask[async]).
    This allows views to be defined with async def and use await.

    @app.route("/get-data")
    async def get_data():
        data = await async_db_query(...)
        return jsonify(data)
    """
    userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
    try:
        userAgentX = request.headers.get('User-Agent')
        #print("userAgentX: %s"%(userAgentX))
        userAgent = userAgentX
    except Exception as e:
        logging.error('social_network_activity: %s'%(e))

    json_response = {}
    try:
        json_response = await getInfo(userAgent)
        return json_response
    except Exception as e:
        #raise
        logging.error("social_network_activity: %s"%(e))
        #print("social_network_activity Exception: ", e)
    #print(json_response)
    return json_response


@app.route("/testapi")
def social_network_activityX():
    """
    Using async on Windows on Python 3.8

    Python 3.8 has a bug related to asyncio on Windows.
    If you encounter something like ValueError: set_wakeup_fd only works in main thread,
    please upgrade to Python 3.9.

    """
    userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
    try:
        userAgentX = request.headers.get('User-Agent')
        #print("userAgentX: %s"%(userAgentX))
        userAgent = userAgentX
    except Exception as e:
        logging.error('social_network_activityX: %s'%(e))

    json_response = {}
    urlTwitter = 'https://takehome.io/twitter'
    urlFacebook = 'https://takehome.io/facebook'
    urlInstagram = 'https://takehome.io/instagram'
    try:
        status = 'online'
        infoTwitter, info1 = getDataX(urlTwitter, userAgent, 'twitter')
        infoFacebook, info2 = getDataX(urlFacebook, userAgent,  'facebook')
        infoInstagram, info3 = getDataX(urlInstagram, userAgent, 'instagram')
        infoTime = dbTimeX()
        if((info1 == 'offline') | (info2 == 'offline') | (info3 == 'offline')):
            status = 'Instagram: %s, Facebook: %s, Twitter: %s'%(info3, info2, info1)
        json_response = {"instagram": len(infoInstagram), "facebook": len(infoFacebook), "twitter": len(infoTwitter), "time": infoTime, "status": status }
        return json_response
    except Exception as e:
        #raise
        logging.error("social_network_activityX: %s"%(e))
    #print(json_response)
    return json_response

async def getData(urlAPI, userAgent, network='twitter'):
    data = []
    status = 'online'
    try:
        """
        Some websites 1 dislike being browsed by programs,
        or send different versions to different browsers
        2. By default urllib identifies itself as
        Python-urllib/x.y (where x and y are the major and
        minor version numbers of the Python release,
        e.g. Python-urllib/2.5),
        which may confuse the site, or just plain not work.
        The way a browser identifies itself is through the User-Agent header
        3. When you create a Request object you can pass a dictionary of headers in.

        Exception:  HTTP Error 403: Forbidden
        403: ('Forbidden',
          'Request forbidden -- authorization will not help'),

        Solved....
        """
        #print("userAgent: %s"%(userAgent))
        req = urllib.request.Request(urlAPI)
        req.add_header('User-Agent', userAgent)
        with urllib.request.urlopen(req) as f:
            data = f.read()
        data = json.loads(data)
    except Exception as e:
        data = await dataInfo(network)
        status = 'offline'
        logging.error("getData: %s, %s"%(network, e))
        #print("getData Exception: ", e)
        #raise
    return data, status

def getDataX(urlAPI, userAgent, network='twitter'):
    data = []
    status = 'online'
    try:
        #print("userAgent: %s"%(userAgent))
        req = urllib.request.Request(urlAPI)
        req.add_header('User-Agent', userAgent)
        with urllib.request.urlopen(req) as f:
            data = f.read()
        data = json.loads(data)
    except Exception as e:
        data = dataInfoX(network)
        status = 'offline'
        logging.error("getDataX: %s, %s"%(network, e))
        #print("getDataX Exception: ", e)
        #raise
    return data, status


async def dataInfo(info):
    #
    try:
        infoTweet = [{"username":"@GuyEndoreKaiser","tweet":"If you live to be 100, you should make up some fake reason why, just to mess with people... like claim you ate a pinecone every single day."},
        {"username":"@mikeleffingwell","tweet":"STOP TELLING ME YOUR NEWBORN'S WEIGHT AND LENGTH I DON'T KNOW WHAT TO DO WITH THAT INFORMATION."}]
        infoFacebook = [{"name":"Some Friend","status":"Here's some photos of my holiday. Look how much more fun I'm having than you are!"},
        {"name":"Drama Pig","status":"I am in a hospital. I will not tell you anything about why I am here."}]
        infoInstagram = [{"username":"hipster1","picture":"food"},
        {"username":"hipster2","picture":"coffee"},
        {"username":"hipster3","picture":"coffee"},
        {"username":"hipster4","picture":"food"},
        {"username":"hipster5","picture":"this one is of a cat"}]
        #
        if(info == 'instagram'):
            return infoInstagram
        if(info == 'facebook'):
            return infoFacebook
        if(info == 'twitter'):
           return infoTweet
        #
    except Exception as e:
        #raise
        logging.error("dataInfo: %s"%(e))
        #print("dataInfo Exception: ", e)
    #
    return {}

def dataInfoX(info):
    #
    json_response = {}
    try:
        infoTweet = [{"username":"@GuyEndoreKaiser","tweet":"If you live to be 100, you should make up some fake reason why, just to mess with people... like claim you ate a pinecone every single day."},
        {"username":"@mikeleffingwell","tweet":"STOP TELLING ME YOUR NEWBORN'S WEIGHT AND LENGTH I DON'T KNOW WHAT TO DO WITH THAT INFORMATION."}]
        infoFacebook = [{"name":"Some Friend","status":"Here's some photos of my holiday. Look how much more fun I'm having than you are!"},
        {"name":"Drama Pig","status":"I am in a hospital. I will not tell you anything about why I am here."}]
        infoInstagram = [{"username":"hipster1","picture":"food"},
        {"username":"hipster2","picture":"coffee"},
        {"username":"hipster3","picture":"coffee"},
        {"username":"hipster4","picture":"food"},
        {"username":"hipster5","picture":"this one is of a cat"}]
        #
        json_response = {"instagram": len(infoInstagram), "facebook": len(infoFacebook), "twitter": len(infoTweet) }
        if(info == 'instagram'):
            return infoInstagram
        if(info == 'facebook'):
            return infoFacebook
        if(info == 'twitter'):
           return infoTweet
        #
    except Exception as e:
        #raise
        logging.error("dataInfoX: %s"%(e))
        #print("dataInfoX Exception: ", e)
    #
    return json_response

def dbTimeX():
    now = datetime.datetime.now()
    return now

async def dbTime():
    now = datetime.datetime.now()
    return now

async def getInfo(userAgent, info=False):
    json_response = {}
    urlTwitter = 'https://takehome.io/twitter'
    urlFacebook = 'https://takehome.io/facebook'
    urlInstagram = 'https://takehome.io/instagram'
    try:
        status = 'online'
        timeM = dbTime()
        dataTwitter = getData(urlTwitter, userAgent, 'twitter')
        dataFacebook = getData(urlFacebook, userAgent, 'facebook')
        dataInstagram = getData(urlInstagram, userAgent, 'instagram')
        infoTwitter, info1 = await dataTwitter
        infoFacebook, info2 = await dataFacebook
        infoInstagram, info3 = await dataInstagram
        infoTime = await timeM
        if((info1 == 'offline') | (info2 == 'offline') | (info3 == 'offline')):
            status = 'Instagram: %s, Facebook: %s, Twitter: %s'%(info3, info2, info1)
        json_response = {"instagram": len(infoInstagram), "facebook": len(infoFacebook), "twitter": len(infoTwitter), "time": infoTime, "status": status }
        if(info):
            print("getInfo : %s"%(json_response))
            logging.info('infoInstagram: %s\n, infoFacebook: %s\n, infoTwitter: %s\n'%(infoInstagram, infoFacebook, infoTwitter))
        return json_response
    except Exception as e:
        #raise
        #print("getInfo Exception: %s"%(e))
        logging.error("getInfo Exception: %s"%(e))
    #print(json_response)
    return json_response

async def apiTest(arg):
    try:
        userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
        data = await getInfo(userAgent, True)
        timeM = await dbTime()
        logging.info("apiTest: %s, %s"%(data, timeM))
        print("apiTest: %s, %s"%(data, timeM))
    except Exception as e:
        logging.error("apiTest: %s"%(e))

if __name__ == '__main__':
    try:
        asyncio.run(apiTest('testing123'))
        app.run(port=8000, debug=True)
        #asyncio.run(apiTest())
    except Exception as e:
        logging.error('ifNameMain: %s, time: %s'%(e, dbTimeX()))
        print("ifNameMain Exception: %s, time: %s"%(e, dbTimeX()))
