# Python-Challenge
From Module 3: Python from the Data Analytics Boot Camp by Monash University.

By implementing skills learnt throughout the module, an attempt at the challenge has been submitted here.

## Contents
- The resource CSV files given
- `.py` files containing codes for each part
- `.txt` files with the output

## Explanations
### PyBank
A `For Loop` was used to loop through each row, which had been split into two variables: *date* and *profit*. Total months was calculated by counting the rows, while net profit was the sum of all the profits. 

An `If Loop` was used to find the profit of the first month and last month on the list to calculate average change. Another `If Loop` was used to calculate the profit between each month. An `or` condition was used to assign value to the greatest increase in profit and the greatest decrease in profit as the code goes through each row. After which, the profit of the previous month was reset for calculation of the next month profits. 

The average change was calculated using the following formula:

    Average change = (Final profit - Initial profit) / (Total months - 1)

This would take the total change over the period and average it over 86 months where 85 changes in profit happened.

The output was printed to a `.txt` file. This file was then opened and read to print the lines in the file to the terminal. 

### PyPoll
A `For Loop` was also used for this task, assigning only the third column to the variable *candidate* as it was the only necessary data column.

A `dictionary` was implemented to keep track of the different candidates. First the code checks if the candidate is already in the dictionary, if they are, it adds one to the counter, which is the value assigned to the key (the candidate's name). If there is no matching name, the code is designed to add the name as a new key, assigning it an initial value of zero and adding one to the counter. 

A `.txt` file was created and the output was written. In the text file, the total votes per candidate and the total percentage was also calculated.

A `For Loop` was used to loop through each pair of *candidates-votes* to find the percentage for each pair. A conditional `If Loop` was used to assign the winning candidate. 

Same with PyBank, the text file was opened and read to print the outputs into the terminal.

## Credits
Credits to my friend, NT, who gave me these ideas to make my code more concise:
- Adding the path to file in the `with open` line
- Destructuring the line in the `for` line and the `_` used to assign variables to values not needed
- Assigning value was `None` rather than `0`
- Writing in text file first then printing to terminal by reading said file (so that it is not repititive and less time consuming)
- This particular line of code: `candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1`
- Using `.items()` to loop through the pairs/tuples