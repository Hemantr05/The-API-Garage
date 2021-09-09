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


module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print ("module %s loaded" % module_url)
def embed(message):
  return model(message)

def USE(text):
    response = dict()
    logging.info('Loaded USE module')
    messages = [text]
    message_embeddings = embed(messages)
    logging.info(f'successfully generated embeddings of length {len(message_embeddings)}')
    response['sentence/text'] = text
    response['embeddings'] = message_embeddings
    return response

# Semantic Textual Similarity Task Example
def plot_similarity(labels, features, rotation):
  corr = np.inner(features, features)
  sns.set(font_scale=1.2)
  g = sns.heatmap(
      corr,
      xticklabels=labels,
      yticklabels=labels,
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
  g.set_xticklabels(labels, rotation=rotation)
  g.set_title("Semantic Textual Similarity")

def run_and_plot(messages_):
  message_embeddings_ = embed(messages_)
  plot_similarity(messages_, message_embeddings_, 90)

## Similarity Visualized
# Here we show the similarity in a heat map. 
# The final graph is a 9x9 matrix where each entry `[i, j]` is colored based on the inner product 
# of the encodings for sentence `i` and `j`.
if __name__ == '__main__':
    messages = [
        # Smartphones
        "I like my phone",
        "My phone is not good.",
        "Your cellphone looks great.",

        # Weather
        "Will it snow tomorrow?",
        "Recently a lot of hurricanes have hit the US",
        "Global warming is real",

        # Food and health
        "An apple a day, keeps the doctors away",
        "Eating strawberries is healthy",
        "Is paleo better than keto?",

        # Asking about age
        "How old are you?",
        "what is your age?",
    ]

    run_and_plot(messages)