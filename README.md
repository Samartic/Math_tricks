# fifteenthree
Python code that test the affirmation that if you sum every number from 1 to 5 (inclusive) it = 5 
but also the fact that if you ad 3s between 1 and 5 and the same number of 3s after 5 it also give the sum between the first
half of the number. ex. 1353, the sum of every number between 13 and 53 give 1353.
and even if we had more 3s it will always work.

## fifteen.py 

This is the code itself. it's an infinit loop that generate the calculation. It can be cancel by ctrl+c
For each itteration it add a 3.

I start by creating the 2 part (a and b) as string throught a for loop. 
Then i join them togheter for creating n.
I use sum function pair with the range function to do the addition of the number between.
and then I compare the sum and the n number to see if the assertion is true.
I also put a time function so we can check the amount of time it took on the last itteration to do.
As we get to bigger number the program can seem to be frozen but it's not.
On my surface pro 7. 9x 3 was calculating in 330 seconds. 
I do not have a super Computer. 

## test_fifteen.py

This code is to test fifteen.py to make sure that it was doing what it should. 
  - Giving the right part a 
  - Giving the right part b
  - Merging them into n correctly
  - That sum indeed sum correctly and is not forgetting any number. 
  - Passing the right output for the "assertion" test. 

## result.txt
This is not a code but is require for the code to work. 
it's the logbook of the ittération for a better management. Even if the function itself is quite verbose, 
it's easier to manage in a text file to search for failure.
