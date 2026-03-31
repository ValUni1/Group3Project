## Toolchain Critique

- This project uses Flask, Supabase, the Open Library API,
Docker, GitHub, and Render. Overall, the toolchain worked
, but it also highlighted some challenges
####
- Flask was easy to use and suitable for building small
web applications since it allowed quick development of routes and features.
####
- Supabase simplified database setup by providing a hosted SQL service, but it
introduced risks of relying on an external service and potential billing costs.
There is also a risk of exposing database credentials if the environment variables
are not handled correctly. But we mitigated these risk with
.gitignore.
####
- The Open Library API worked well for retrieving data, but it also creates a 
dependency on a third-party service. If the API is unavailable or slow, the application
might fail. We mitigated this with retry/backoff responses.
####
- Docker helped with consistency between environments, but it added 
complexity which was hard to understand.
####
- Github was affective for version control, but there is a risk of accidentally
committing sensitive data, which we mitigated with .gitignore.
####
- Render made deployment simple by integrating with GitHub, but when first deploying it
we had issues with dependencies (missing requirement for an import) which required us to 
make sure everything was consistent and dependencies clearly defined

