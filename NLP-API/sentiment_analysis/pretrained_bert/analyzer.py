from transformers import pipeline

def simple_analyzer(text):
	sentimentanalyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

	# result = sentimentanalyzer("I really don't like what you did")[0]
	predictions = sentimentanalyzer(text)[0]
	return predictions['label'], predictions['score']
	


