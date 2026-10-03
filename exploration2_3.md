### Kate Macias
### Software Engineering 1
### Fall 2026

## What is an example of code you've written that violates any of the above guidelines? Name the violation and paste in the code.

```python
def game_logic(player_1, player_2):
    '''This function requires two player inputs and returns a winner'''

    if (player_1 == "rock" and player_2 == "paper"):
        print("Computer wins!")
        turtle_C()
    elif (player_1 == "rock" and player_2 == "scissors"):
        print("Human wins!")
        turtle_H()
    elif (player_1 == "paper" and player_2 == "rock"):
        print("Human wins!")
        turtle_H()
    elif (player_1 == "paper" and player_2 == "scissors"):
        print("Computer wins!")
        turtle_C()
    elif (player_1 == "scissors" and player_2 == "rock"):
        print("Computer wins!")
        turtle_C()
    elif(player_1 == "scissors" and player_2 == "paper"):
        print("Human wins!")
        turtle_H()
    else:
        print("It's a Tie!")
        ```
### This is a really long function that is basically the whole program.

## What is another example? I know you have more than one. (ouch lol)
### I made this up. All my code is homework assignments. Where I've written specifically defined functions. 

```python
def bad_function(variable_1, variable_2, variable_3, oneMoreForFun, none_of_that_matters_its_this_one):
    if variable_1 + >= 100:
        print("thats a really big number bruh")
    if variable_3 * variable_1 >= 1:
        while variable_1 / oneMoreForFun >= 1:
            print("variable_1 / oneMoreForFun is still greater than 1")
    return none_of_that_matters_its_this_one
```
### this has way too many variables, one isn't used at all and the function doesn't do anything with the other two and returns the 4th variable. It could easily be multiple functions. It was also fun to write.
