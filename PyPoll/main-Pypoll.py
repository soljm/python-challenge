import os
import csv

# open and read CSV file
with open("PyPoll/Resources/election_data.csv", encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # skip header
    csv_header = next(csvfile)

    # set inital value
    total_votes = 0
    candidate_votes = {}

    # looping through each row, assigning candidate to the last column and ignoring the first two
    for _, _, candidate in csv_reader:

        # counting total votes
        total_votes += 1

        # adding names to dictionary and adding 1 to the count each time it appears
        # if not already in dictionary, add a new key and increase value/count to 1
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# make a text file and write analysis
with open("PyPoll/Analysis/output2.txt", 'w') as f:
    f.write("Election Results\n")
    f.write("------------------------------\n")
    f.write(f"Total votes: {total_votes}\n")
    f.write("------------------------------\n")

    winning_candidate = None
    
    # looping through each pair in dictionary to determine percentage vote
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        percentage = round(percentage, 3)
        f.write(f"{candidate}: {percentage}% ({votes})\n")

        # assigning value to winning_candidate
        if winning_candidate is None or votes > candidate_votes[winning_candidate]:
            winning_candidate = candidate

    f.write("------------------------------\n")
    f.write(f"Winner: {winning_candidate}\n")
    f.write("------------------------------\n")

# read text file to print to terminal
with open("PyPoll/Analysis/output2.txt", 'r') as f:
    for line in f:
        print(line)
