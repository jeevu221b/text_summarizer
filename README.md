
## Overview

Abstract Summarizer API is a simple flask app with a POST endpoint which accepts input text, maximum and minimum summary length in the request. These params are then passed through a function that uses the T5 (Text-To-Text Transfer Transformer) model from the Hugging Face Transformers library which generates a condensed summary. The summarization process involves encoding the input text, generating the summary, and decoding the output to obtain the final summarized text.


## Libraries Used:

Transformers: Utilized for its T5 model architecture, enabling advanced text summarization capabilities.

Flask: Used to create a RESTful API, facilitating interaction with the summarization functionality via HTTP requests.

Honeybadger: Incorporated for error monitoring and tracking within the API application, ensuring robustness.

Torch: Dependency of the transformers library, utilized for neural network computations.

Sentencepiece: Utilized as a subword tokenizer by the T5 model for tokenization.


## Installation

$ pip install requirements.txt

$ flask --app app_name run

    * Running on http://127.0.0.1:5000/