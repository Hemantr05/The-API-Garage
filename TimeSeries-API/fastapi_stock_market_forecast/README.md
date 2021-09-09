<h3 align="center"> Stock market forecase with FastAPI</h3>

## How to run:

    $ uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000

Then, in a new terminal window, use curl to test the endpoint:

    $ curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"ticker":"MSFT"}' \
    http://localhost:8000/predict

Or, 

Type 0.0.0.0:8000/docs# on the browser 

and for documentation, type: 0.0.0.0:8000/redocs


### With Docker

1. Build and tag the Docker image:

    ```sh
    $ docker build -t fastapi-prophet .
    ```

1. Spin up the container:

    ```sh
    $ docker run --name fastapi-ml -e PORT=8008 -p 8008:8008 -d fastapi-prophet:latest
    ```

1. Train the model:

    ```sh
    $ docker exec -it fastapi-ml python

    >>> from model import train, predict, convert
    >>> train()
    ```

1. Test:

    ```sh
    $ curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"ticker":"MSFT"}' \
      http://localhost:8000/predict
    ```

### Without Docker

1. Create and activate a virtual environment:

    ```sh
    $ virtualenv --python=python3 smforecast-env && source smforecast-env/bin/activate
    ```

1. Install the requirements:

    ```sh
    (smforecast)$ pip install -r requirements.txt
    ```

1. Train the model:

    train() by default trains "MSFT"

    ```sh
    (smforecast)$ python

    >>> from model import train, predict, convert
    >>> train()
    >>> train("GOOG")
    >>> train("AAPL")
    ```

1. Run the app:

    ```sh
    (smforecast)$ uvicorn main:app --reload --workers 1 --host 127.0.0.1 --port 8000
    ```

1. Test:

    ```sh
    $ curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"ticker":"MSFT"}' \
      http://localhost:8008/predict
    ```
