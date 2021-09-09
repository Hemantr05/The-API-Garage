from transformers import TapasTokenizer, TapasForQuestionAnswering
import pandas as pd
import re
import torch
# print(torch.__version__)

model_name = 'google/tapas-base-finetuned-wtq'
model = TapasForQuestionAnswering.from_pretrained(model_name)
tokenizer = TapasTokenizer.from_pretrained(model_name)

id2aggregation = {0: "NONE", 1: "SUM", 2: "AVERAGE", 3:"COUNT", 4: "*"}

def get_unique_words_from_df(df):
    tokens = []
    for col in df.columns:
        tokens += col.split()
        for c in df[col]:
            if type(c) == str and len(c) > 0:
                tokens += c.split()
    tokens = [t.lower() for t in tokens]
    tokens = [re.sub(r'[^A-Za-z0-9 ]+', '', t) for t in tokens]
    tokens = list(set(tokens))
    return tokens

def get_best_table(dfs,dfs_tokens,query):
    dfs_scores = []
    query_tokens = query.lower().split()
    query_tokens = [re.sub(r'[^A-Za-z0-9 ]+', '', t) for t in query_tokens]
    query_tokens = [t for t in query_tokens if t not in filter_list]
    print(query_tokens)
    for df,tokens in zip(dfs,dfs_tokens):
        total = 0
        score = 0
        for qt in query_tokens:
            if qt in tokens:
                score += 1
            total += 1
        
        if total > 0:
            dfs_scores.append(score/total)
        else:
            dfs_scores.append(0)
    
    max_score = max(dfs_scores)
    if max_score > 0:
        idx = dfs_scores.index(max_score)
        return idx
    else:
        return None


def answers(df, queries)
    df_tokens = get_unique_words_from_df(df)

    q_idxs = []
    for q in queries:
        idx = get_best_table(dfs,dfs_tokens,q)
        if idx is not None:
            q_idxs.append(idx)
        else:
            q_idxs.append(None)

    unanswered_queries = []
    qmap = {}
    for idx, qidx in enumerate(q_idxs):
        if qidx == None:
            unanswered_queries.append(queries[idx])
        else:
            if qidx not in qmap:
                qmap[qidx] = []
            qmap[qidx].append(queries[idx])




if __name__ == '__main__':
    df = pd.read_csv('/content/XboxOne_GameSales.csv', encoding = "ISO-8859-1")
    queries = [
        "What is the name of the first actor?", 
        "How many movies has George Clooney played in?", 
        "What is the total number of movies?",
        "Who is the Chairman of Google?",
        "What was the total revenue in 2017",
        "Gross Margin in 2018?",
        "What genre is Grand Theft Auto V",
        "Who is the Publisher of MineCraft"
    ]