## Application Description:
This Flask application that allows users to
1) Add authors to a Supabase Database
2) Retrieve the first seven books published by an author using the Library API.
3) View a author and their associated books by clicking on the author name in the dropdown.
This application is containerised using Docker and deployed via Render.

### Github repository URL:


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
- Returns al authors with their books

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
3) Select author from the list
4) View books retrieved from the Library API



