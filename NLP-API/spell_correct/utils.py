import re
import shutil
from pathlib import Path
from textblob import TextBlob
from fastapi import UploadFile
from textblob.en import Spelling        
from tempfile import NamedTemporaryFile

def correct(file):
    """Returns spell corrected text"""
    with open(file, "r") as f:
        text = f.read()
        textblb = TextBlob(text)
        corrected = textblb.correct() 
    return correct

def save_upload_file_tmp(upload_file: UploadFile, dest: str):
    """Returns temporary path for uploaded file"""
    try:
        dest = Path(dest)
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path


def train(file, trainFile):
    textToLower = ""

    with open(file,"r") as f1:                            # Open our source file
        text = f1.read()                                  # Read the file                 
        textToLower = text.lower()                        # Lower all the capital letters

    words = re.findall("[a-z]+", textToLower)             # Find all the words and place them into a list    
    oneString = " ".join(words)                           # Join them into one string

    pathToFile = trainFile                                # The path we want to store our stats file at
    spelling = Spelling(path = pathToFile)                # Connect the path to the Spelling object
    spelling.train(oneString, pathToFile)      


def train2(file, trainFile):
    pathToFile = trainFile
    spelling = Spelling(path = pathToFile)
    text = " "

    with open(file, "r") as f: 
        text = f.read()

    words = text.split()
    corrected = " "
    for i in words :
        corrected = corrected +" "+ spelling.suggest(i)[0][0] # Spell checking word by word

    return corrected        