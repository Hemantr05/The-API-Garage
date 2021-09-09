from absl import logging

import tensorflow as tf

import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns

def USE(text):
    response = dict()
    module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
    model = hub.load(module_url)
    messages = [text]
    message_embeddings = model(messages)
    response['sentence/text'] = text
    response['embeddings'] = message_embeddings
    return response