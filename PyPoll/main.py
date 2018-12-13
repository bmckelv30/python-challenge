# Import modules
import os
import csv
# Read in csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    # print(f"Header: {header}")
    votes = []
    candidate = []
    total=0
    for row in csvreader:
        # The total number of votes cast
        total=total+1
        # Compile all the votes in list
        votes.append(row[2])
        # A complete list of candidates who received votes
        if row[2] not in candidate:
            candidate.append(row[2])
    # Print out total votes
    print (f"Election results")
    print (f"----------------------------")
    print (f"Total Votes: {total}")
    print (f"----------------------------")
    # print(candidate)
    # Sort in order to obtain count
    votes.sort
    # The Print out candidate, percentage and number of votes each candidate won
    for i in range(len(candidate)):
        print(f"{str(candidate[i])}: {str(format(votes.count(candidate[i]) / total * 100,'.3f'))}% ({str(votes.count(candidate[i]))})")
    # Print out winner
    print (f"----------------------------")    
    print (f"Winner: {max(set(votes),key=votes.count)}")
    print (f"----------------------------") 

text_file = open("election_result.txt","w")
with open("election_result.txt", "w") as text_file:
    print (f"Election Results", file=text_file)
    print (f"----------------------------", file=text_file)
    print (f"Total Votes: {total}", file=text_file)
    print (f"----------------------------", file=text_file)
    for i in range(len(candidate)):
        print(f"{str(candidate[i])}: {str(format(votes.count(candidate[i]) / total * 100,'.3f'))}% ({str(votes.count(candidate[i]))})", file=text_file)
    print (f"----------------------------", file=text_file)
    print (f"Winner: {max(set(votes),key=votes.count)}", file=text_file)
    print (f"----------------------------", file=text_file)
text_file.close()