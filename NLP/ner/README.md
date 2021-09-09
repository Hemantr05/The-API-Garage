<h2 align='center'>Named Entity Recognition</h2>


### Installation:

**Clone the repository**

and move into working directory

```git clone https://github.com/Hemantr05/ML_APIs && cd ner```

**Install requirements**

```pip install -r requirements.txt```

### Start server:

1. **Using uvicorn:**

    ```uvicorn main:app --reload --host 127.0.0.1 --port 8000```

2. **Using hypercorn:**

    ```hypercorn main:app --reload```

### Usage:
    
**Swagger UI:**

Open http://127.0.0.1:8000/docs in your browser



### Response:

1. Simple Analyzer:

```
{
	'result': 
		[
			{
				'end': 21,
				'entity_group': 'PER',
				'score': 0.994477,
				'start': 15,
				'word': 'Hemant'
			},
			{	'end': 45,
				'entity_group': 'LOC',
				'score': 0.9993967,
				'start': 36,
				'word': 'Bangalore'
			},
			{	'end': 52,
				'entity_group': 'LOC',
				'score': 0.9995802,
				'start': 47,
				'word': 'India'
			},
			{	'end': 96,
				'entity_group': 'ORG',
				'score': 0.7549327,
				'start': 89,
				'word': 'Glib. ai'
			}
		]
}
```
