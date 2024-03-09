import os
import csv

with open("PyPoll/Resources/election_data.csv", encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    # Set inital value
    total_votes = 0
    candidate_votes = {}

    for _, _, candidate in csv_reader:

        total_votes += 1

        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

with open("PyPoll/Analysis/output2.txt", 'w') as f:
    f.write("Election Results\n")
    f.write("------------------------------\n")
    f.write(f"Total votes: {total_votes}\n")
    f.write("------------------------------\n")

    winning_candidate = None

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        percentage = round(percentage, 3)
        f.write(f"{candidate}: {percentage}% ({votes})\n")

        if winning_candidate is None or votes > candidate_votes[winning_candidate]:
            winning_candidate = candidate

    f.write("------------------------------\n")
    f.write(f"Winner: {winning_candidate}\n")
    f.write("------------------------------\n")

with open("PyPoll/Analysis/output2.txt", 'r') as f:
    for line in f:
        print(line)
