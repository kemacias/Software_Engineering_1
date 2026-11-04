### Kate Macias
### Software Engineering 1
### Fall 2026

## Suppose you ask an AI assistant to implement a function that transfers money between two accounts. Explain how stating invariants in your prompt changes what you can expect from the output.

Invariants intercept the "problem solving" that AI does that just creates problems that don't need to be solved. It keeps the solutions within a scope, simplier, easier to work on and verify that it's correct. 

## Does stating invariants in the design doc obviate the need for testing? Why or why not?

No. It just declares that something must always be true. It does not assert that you wrote the code correctly. 

## For each statement, label it as a constraint, assumption, NFR, or invariant, and say what would change in your AI prompt or instructions file because of the label: (a) "The service must run on the company's existing Kubernetes cluster." (b) "No two users are ever assigned the same username." (c) "Search results return in under 300ms at p95." (d) "The upstream payments API will not change its response schema this year."

a. constraint
b. invariant
c. constraint
d. constraint

## You inherit a legacy codebase with no invariant documentation, so you prompt an AI to "Discover the invariants". It lists some, and you add assertionsLinks to an external site. to make sure the invariants are always true. Running it, one of the assertions fires. This can mean two things. What are they?

You've correctly found an invariant that went undiscovered previously, or AI made up an invariant that wasn't actually an invariant. 

## You prompt an AI like so: "Write a function that removes duplicates from a list. For example, [1, 2, 2, 3] becomes [1, 2, 3]."

### Rewrite this example as an invariant.
- The output list never contains duplicates, and all elements appear in numerical order. 

### In what way could the initial prompt produce code that still allowed duplicate entries? Does your invariant fix this?
- The first prompt could miss duplicates that are not next to each other. I hope mine would fix that along with putting all the elements in order.
