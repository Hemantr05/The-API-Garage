sudo apt-get update && sudo apt-get upgrade
sudo apt install virtualenv mongo-clients
virtualenv --python=python3 crud-mongo-env
source crud-mongo-env/bin/activate
pip install -r requirements.txt
python app/main.py
