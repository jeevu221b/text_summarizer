import json
import os
from flask import Flask, request
from summarizer import summarizer
from dotenv import load_dotenv
import logging
from honeybadger.contrib.logger import HoneybadgerHandler

load_dotenv()
app = Flask(__name__)


hb_handler = HoneybadgerHandler(os.getenv("honeyBadgerApiKey"))
logger = logging.getLogger('honeybadger')
logger.addHandler(hb_handler)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/summarizer', methods=['POST'])
def summary():
    try:
        data = json.loads(request.data)
        print(data["text"], data["max_length"], data["min_length"])
        summary = summarizer(
            data["text"], data["max_length"], data["min_length"])
        res = {
            "message": "Summarized text:",
            "summary": summary
        }
        return (res, 200)
    except Exception as e:
        logger.error(e)
        message = "Enter Valid Data :)"
        return (message, 400)
