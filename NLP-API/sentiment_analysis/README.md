<h2 align='center'>Sentiment Analysis</h2>


### Installation:

**Clone the repository**

and move into working directory

```git clone https://github.com/Hemantr05/ML_APIs && cd sentiment_analysis```

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

```json
{
	"score": 0.9978761672973633,
 	"sentiment": "NEGATIVE",
 	"text": "I really don't like what you did"
}
```
