import os
import csv

file_path = "election_data.csv"
output_folder = "../Analysis"
output_file = os.path.join(output_folder, "analysis_results.txt")

total_votes = 0
candidates = {}
winner = ""
max_votes = 0

with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:

        total_votes += 1

        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(output_file, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        if votes > max_votes:
            max_votes = votes
            winner = candidate

    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

with open(output_file, 'r') as f:
    print(f.read())
