### Kate Macias
### Software Engineering 1
### Fall 2026

## 1. How does a Technical Design Document differ from a Functional Spec? Who (or what) is the intended consumer of each?
### the functional spec is a document that describes how the appication works from the outside in a way that stakeholders can understand. The Technical Design Document is the details of how the application works on the inside in a way that developers understand. 

## 2. Why is a good Design Doc even more critical in the age of LLMs?
### Because LLM's go off into the weeds really quickly if you don't set up good parameters for it. (it likes to learn, it can't help it). good documents mean less tokens used to prompt and that equals less money spent. 

## 3. Explain the difference between a constraint and a design decision.
### Constraints are things like laws, client needs and regulations that need to be followed in the application. Design decisions are things that can change throughout the developement process. 

## 4. "Each store delivers within a fixed radius (about 5 miles)." Is this more of a constraint or an assumption? Why?
### This is a constraint. Its a hard boundry that the application needs to account for because of policy. 

## 5. Why would we create additional component diagrams that "drill down" into a single box? What does that gain us?
### This reveals the subcomponents and how to split up the work in a way where all the pieces fit together. 

## 6. Explain why redundancy and conflicting requirements are especially risky when an LLM is a reader of the document
### Conflicting requirements totally confuse LLM's and there's no rhyme or reason to which requirement they might pick. Redundancy is similar where it probably won't detect that information differs in two different places.
