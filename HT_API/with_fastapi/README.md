<h2 align="center">Hindustan Times API</h2>


### Task: 
	[x] Scrap 2010’s newspaper articles data from https://www.thehindu.com/archive/
	[x] Develop a search engine such as 
		Input - Name of a person in any article (Author)
		Output - Articles about that person 
	[x] There may be N number of articles for a single person.


### Usage:

1. <b>Install requirements:</b>

    `pip install -r requirements`


2. <b>Start the server:</b>
       
    `uvicorn main:app --reload`
      
3. <b>Setting up postman:</b>

    Open postman, and enter the following url:
      
    http://127.0.0.1:8000/


- In body, select <b>form-data</b> and 
- Add <b>key</b> as <i>author_name</i>
- The corresonding value to the <i>author_name</i> key will be 
    author who's article you would want to extract


