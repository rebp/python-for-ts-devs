# Exercise 10.3-3: Review a migration (answer)

A rename can appear as a drop and an add, which could discard existing data.
Review the generated operations, constraints, indexes, data migration and
downgrade; replace the candidate with a safe rename when appropriate. Commit
before sending the response so a failed commit is reported as an error rather
than a successful response.
