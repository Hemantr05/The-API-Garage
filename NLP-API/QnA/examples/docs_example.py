from transformers import TapasTokenizer, TapasForQuestionAnswering
import pandas as pd

model_name = 'google/tapas-base-finetuned-wtq'
model = TapasForQuestionAnswering.from_pretrained(model_name)
tokenizer = TapasTokenizer.from_pretrained(model_name)

data = {'Actors': ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"], 'Number of movies': ["87", "53", "69"]}
queries = ["What is the name of the first actor?", "How many movies has George Clooney played in?", "What is the total number of movies?"]
table = pd.DataFrame.from_dict(data)
inputs = tokenizer(table=table, queries=queries, padding='max_length', return_tensors="pt")
outputs = model(**inputs)
predicted_answer_coordinates, predicted_aggregation_indices = tokenizer.convert_logits_to_predictions(
        inputs,
        outputs.logits.detach(),
        outputs.logits_aggregation.detach()
)

# let's print out the results:
id2aggregation = {0: "NONE", 1: "SUM", 2: "AVERAGE", 3:"COUNT"}
aggregation_predictions_string = [id2aggregation[x] for x in predicted_aggregation_indices]

answers = []
for coordinates in predicted_answer_coordinates:
  if len(coordinates) == 1:
    # only a single cell:
    answers.append(table.iat[coordinates[0]])
  else:
    # multiple cells
    cell_values = []
    for coordinate in coordinates:
       cell_values.append(table.iat[coordinate])
    answers.append(", ".join(cell_values))

display(table)
print("")
for query, answer, predicted_agg in zip(queries, answers, aggregation_predictions_string):
  print(query)
  if predicted_agg == "NONE":
    print("Predicted answer: " + answer)
  else:
    print("Predicted answer: " + predicted_agg + " > " + answer)
