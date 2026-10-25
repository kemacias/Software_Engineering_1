### Kate Macias
### Software Engineering 1
### Fall 2026

## Normally only public/external interfaces are documented, but that's not a hard-and-fast rule. When might you want to document internal interfaces?

- When multiple people might work on it or maintain it. 

## Brainstorm three advantages to writing your interface and type definitions in pseudocode as opposed to real code.

- Ideas only. no thinking about syntax
- You don't even have to had committed to a launguage yet. Its universal. 
- It is readable by almost everyone

## Why might a strong interface definition be more important when using AI?

- You're not leaving a bunch of gaps for AI to make stuff up in. Action A gets to B by doing this, and B get to C by doing this... no undescribed holes

## Looking at the ATM example, what's an example of something that can go wrong if the authorizeWithdraw() functionality violates one of its requirements or guarantees? (Choose one requirement or guarantee to examine.)

- If you stored a pin number somewhere in your code, a hacker would have the pin along with the account information.
