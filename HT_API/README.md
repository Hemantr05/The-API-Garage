<h3 align="center">Hindustan Times API</h3>


### Task: 
	[x] Scrap 2010’s newspaper articles data from https://www.thehindu.com/archive/
	[x] Develop a search engine such as 
		Input - Name of a person in any article (Author)
		Output - Articles about that person 
	[x] There may be N number of articles for a single person.


### Usage:

   Start the server:
      ```
      $ python get_article.py
      ```

   Open postman, and type the following url:
      ```
      http://0.0.0.0:5000/
      ```
   In body, 
   1. Select <b>form-data</b> and 
   2. Add <b>key</b> as <i>author_name</i>
   3. The corresonding value to the <i>author_name</i> key will be 
      author who's article you would want to extract



