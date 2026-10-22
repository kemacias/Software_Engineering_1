### Kate Macias
### Software Engineering 1
### Fall 2026


## A vendor releases v2 of their API and renames several fields. Explain how wrapping the API affects the cost of adapting to this change.

-a wrapper makes it easy to change an API without having to change anything else

## Why does wrapping an external API make unit testing easier? Name at least two specific problems it helps you avoid.

- lower cost and side effects, since testing is easier all around
- you can use fake data for testing. this also makes testing results repeatable

## Explain what an anti-corruption layer is and why a vendor's data model might be a problem if it spreads through your codebase.

- this keeps you in control of your code when vendors make changes on their side. It stops their changes leaking through your work

## A teammate proposes wrapping a small, stable API that is called from exactly one place in your code. Under what reasoning might you push back, and what conditions would change your mind?

- A single API call in one place is sort of wrapped by itself since it only needs updating in one place. However, if there was ANY chance of making the call in other places (why not just be ready for that) I'd opt to wrap it.
