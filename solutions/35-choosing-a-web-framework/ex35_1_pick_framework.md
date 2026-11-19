# Exercise 35-1: Pick a framework (answer)

1. **FastAPI.** Pydantic models give you validated, typed requests and
   responses, and the OpenAPI docs at `/docs` are generated from the same type
   hints, so they can't drift out of date. Lesson 37 turns that schema into
   TypeScript types for the React app.
2. **Django.** It ships with the ORM, migrations, authentication and the admin
   site. The admin gives non-developers screens to edit records with almost no
   code, which would take weeks to build by hand on FastAPI or Flask.
3. **Flask.** Add the endpoints to the existing app. Rewriting a working
   service to switch frameworks is rarely worth it. If the service grows a lot
   later, that's the time to talk about a migration.

The general rule: FastAPI for new JSON APIs, Django when you want the batteries
(admin, auth, ORM) included, and whatever is already there for existing code.
