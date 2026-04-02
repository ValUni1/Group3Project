### Context Diagram:
- Con
### Integration Points:
- con

### Branching Model:
- We decided to employ a simple approach in regards to our branching model. We employed Trunk Based Development (GeeksforGeeks, 2026) branching strategy with master as the main branch. For each major feature we would create a new branch with a suitable name and code the new feature there. For example, when creating the health code we created a new branch called /health and coded the health route there. 
- This branching model suited our purposes as we were a small group with three members and the minimised merge complexity helped us understand the various changes or updates that were being implemented. For each new feature or update we created a pull request to integrate the feature branch back into the master. Throughout the course of the project we had a total of 22 pull requests opened and merged into the master once checked.
- An example of a pull request is the pull request for the retry/backoff feature. We included a brief description in each pull request which in this case was "Retry and backoff created for api and database". 
- Every branch was required to pass Continuous Integration (CI) status checks before merging. This meant that the master branch was protected and remained in a continuously deployable state. A different member than the group member who made the pull request had to confirm and merge the feature branch further protecting the master branch.
- This simple branching model encouraged small frequent commit which helped to reduce merge conflicts. The trunk which in our case was the master branch remained continuously releasable and was protected.

### Pipeline Design:
- The Continuous Integration/Continuous Deployment pipeline was created through the workflow file in our .github directory. The pipeline is triggered automatically every time code is pushed and everytime there is a pull request. This ensures that code isn't merged into the master without first passing all checks, helping to protect the master branch. This also helps to catch issues earlier and prevents potential problems. On GitHub you can see the workflow running in GitHub Actions as a green tick.
- The pipeline is made up of several stages of code that complete different actions. The code is checked out to set up the environment and Python 3.11 is installed and dependencies are installed from the requirements.txt file. A pull request cannot be merged into master branch until this check passes.
- Render which is the platform we are using to deploy our code/project, redeploys the live application once a pull request has been merged as it is linked to the GitHub repository of our project.
- Our .env file information such as DATABASE_URL and API were inputted into Render's environment settings so that our project can be deployed.
