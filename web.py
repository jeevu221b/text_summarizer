import json
import os
from flask import Flask, request
from summarizer import summarizer
from dotenv import load_dotenv
import logging
from honeybadger.contrib.logger import HoneybadgerHandler
from errors import error


load_dotenv()
app = Flask(__name__)


hb_handler = HoneybadgerHandler(os.getenv("honeyBadgerApiKey"))
logger = logging.getLogger('honeybadger')
logger.addHandler(hb_handler)
logger.setLevel(logging.INFO)


@app.route('/')
def hello():
    return "<h1>Text Summarizer</h1>"


@app.route('/summarizer', methods=['POST'])
def summary():
    try:
        data = json.loads(request.data)
        logger.info(f"Method: {request.method}, Body: {data}")
        if data["text"] == "":
            return (error["EMPTY_TEXT"], 400)
        if type(data["max_length"]) != int or type(data["min_length"]) != int:
            return (error["NOT_INTEGER"], 400)
        if type(data["max_length"]) == int and type(data["min_length"]) == int:
            if data["max_length"] < 2 or data["min_length"] < 2:
                return (error["INVALID_LENGTH"], 400)

        summary = summarizer(
            data["text"], data["max_length"], data["min_length"])
        res = {
            "summary": summary
        }
        return (res, 200)
    except Exception as e:
        logger.error(e)
        message = "Enter Valid Data :)"
        return (message, 400)
