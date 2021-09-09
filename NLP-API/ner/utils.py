
from transformers import pipeline

def bert_coll03(text):
    # text = 'Hi, my name is Hemant and I live in Bangalore, India. I work at this cool company called Glib.ai' # @param {type: "string"}
    json_response = dict()
    nlp_bert_lg = pipeline('ner', 
                        model = "dbmdz/bert-large-cased-finetuned-conll03-english",
                        tokenizer = "dbmdz/bert-large-cased-finetuned-conll03-english",
                        grouped_entities=True,
                        )
    response = nlp_bert_lg(text)
    json_response['result'] = response
    return json_response