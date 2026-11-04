### Kate Macias
### Software Engineering 1
### Fall 2026

## A function takes input data, computes values for a report, and prints the report. How is this a violation of SRP?

- The function that does 3 different things. Thats destined to be a problem. Make that 3 functions. 

## By coding it this way, how have we reduced the flexibility of our software? What can we no longer easily do? nHow would you apply SRP to fix it?

- Its really difficult to test when you have a bunch of super dynamic fuctions with lots of arguments and do lots of things. You're making your life (and everyone else's) harder for no reason. No Bueno. 

##nLook at [https://github.com/beejjorgensen/trn-4.0-test77/blob/main/src/art.c#L91] this function do_article().

## Estimate how long it would take you (and you can assume you're a C expert) to explain what this function does. Keep scrolling. Yes, it's that big. Do you think this is a SRP violation?

- If  I'm the expert, how smart is the person I'm explaining it to? I'd guess 12 hours to 12 years depending on the person recieving the information.  

## Exactly how hosed would you be if you were tasked with refactoring this code?

- Pretty freaking hosed. I'd nuke and start over. 

¯\_(ツ)_/¯

Have you ever violated SRP in your code?

Yes. We all have. Since I already know the answer, there's no need to tell me. 😊
