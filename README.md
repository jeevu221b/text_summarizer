
## Overview

Abstract Summarizer API is a simple flask app with a POST endpoint which accepts input text, maximum and minimum summary lengths as input in the body of the request and then passes these params thritough a function that uses the T5 model architecture to create the summary which then is returned in the response body.

## Libraries Used:

transformers: Utilized for its T5 model architecture, enabling advanced text summarization capabilities.

Flask: Used to create a RESTful API, facilitating interaction with the summarization functionality via HTTP requests.

honeybadger: Incorporated for error monitoring and tracking within the API application, ensuring robustness.

torch: Dependency of the transformers library, utilized for neural network computations.

sentencepiece: Utilized as a subword tokenizer by the T5 model for tokenization.


## Installation

$ pip install requirements.txt

$ flask --app app_name run

    * Running on http://127.0.0.1:5000/

## How to Use

    The way to use vary from use method