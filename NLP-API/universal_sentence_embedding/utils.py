# from absl import logging
import logging
import tensorflow as tf

import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns
logging.basicConfig(filename='compile.log', level=logging.DEBUG)

def USE(text):
    response = dict()
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model = hub.load(module_url)
    logging.info('Loaded USE module')
    messages = [text]
    message_embeddings = model(messages)
    logging.info(f'successfully generated embeddings of length {len(message_embeddings)}')
    response['sentence/text'] = text
    response['embeddings'] = message_embeddings
    return response