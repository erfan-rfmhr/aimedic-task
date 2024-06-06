# Documentation

---

In this file, I describe the project and how I did tasks.

### Update from Pydantic v1 to v2

I updated the project from Pydantic v1 to v2 by following the [official guide](https://docs.pydantic.dev/latest/migration/#migration-guide):

+ install bump-pydantic
    + pip install bump-pydantic
+ check differences
    + bump-pydantic --diff
+ apply changes
    + bump-pydantic --apply

---

### Add Phone Number and Last Login columns to user_account table
Using alembic, I applied a new migration automatically:
+ add fields to UserModel
+ commit changes and run pre-commit hooks if needed
+ create a revision
  + alembic revision --autogenerate -m "add phone number and last login field"
+ apply migrations
  + alembic upgrade head
