## Application Description:
This Flask application that allows users to
1) Add authors to a Supabase Database
2) Retrieve the first eight books published by an author using the Open Library API.
3) View an author and their associated book titles and year first published by clicking on the author name in the dropdown.
This application is containerised using Docker and deployed via Render.

### Github repository URL:
https://github.com/ValUni1/Group3Project.git

### Github Zipped repository:


### Live Application URL:
https://group3project-0mpb.onrender.com

### Setup:
1) Clone the repository
2) Create virtual environment
3) Install requirements

### Environment Variables:
Create a `.env` file with:
- API_KEY=your_api_key
- DATABASE_URL=your_database_url

### DockerFile
- Dockerfile instructions in Dockerfile

### Make/Run Commands
The app will be available through Render URL
But you can run with docker too

### CI/CD Overview
This project is hosted on GitHub and deployed through Render.
When code is pushed to the main branch, Render automatically rebuilds
and redeploys the application. The project also uses Supabase for its database.

### Endpoints
GET /:
- Main dashboard page
- Displays authors and allows selection
- Shows books for selected author

POST /add:
- Adds a new author to the database
- Requires form data: name

GET /author_books
- Returns the first eight books for the selected author

GET /health
- Health check endpoint
- Returns : {"status": "Ok"}

GET /ready:
- Checks database connectivity
- Returns: {"Status": "Ready"}
or error if DB is unavailable

### Demo Steps:
1) Open the Render deployed URL
2) Add new author using the form
3) Select author from the dropdown list
4) View first 8 books published retrieved from the Open Library API

### References:
- GeeksforGeeks (2026) Branching strategies in git, GeeksforGeeks. Available at: https://www.geeksforgeeks.org/git/branching-strategies-in-git/ (Accessed: 01 April 2026). 
- Testing flask applications (no date) Testing Flask Applications - Flask Documentation (3.1.x). Available at: https://flask.palletsprojects.com/en/stable/testing/ (Accessed: 02 April 2026). 
- user1899891 et al. (2013) How do I auto submit a dropdown when a value is selected other than the first value?, Stack Overflow. Available at: https://stackoverflow.com/questions/19086737/how-do-i-auto-submit-a-dropdown-when-a-value-is-selected-other-than-the-first-va (Accessed: 02 April 2026). 
- W3schools.com (no date) HTML form action Attribute. Available at: https://www.w3schools.com/tags/att_form_action.asp (Accessed: 02 April 2026). 
- zyshara et al. (2018) How to mock psycopg2 cursor object?, Stack Overflow. Available at: https://stackoverflow.com/questions/35143055/how-to-mock-psycopg2-cursor-object (Accessed: 02 April 2026). 




