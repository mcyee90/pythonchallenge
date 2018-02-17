# ## Option 2: PyPoll

# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). 

import os
csvpath = os.path.join('raw_data', 'election_data_2.csv')


# # Method 1: Plain Reading of CSVs


# Method 2: Improved Reading using CSV module
import csv
with open(csvpath, newline='',encoding='utf-8') as csvfile:

    print ("Election Results")
    print ("-------------------------------------------------------")

    # CSV reader specifies delimiter and variable that holds contents
    # Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
    # Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # ----------------------------------------------------
    # # * The total number of votes cast      
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = list(csvreader)
    del csvreader[0]
    totalVotes = len(csvreader)
    print ("Total Votes: " + str(totalVotes))
    # ----------------------------------------------------
    # 
    # A complete list of candidates who received votes
    votes = []
    for rows in csvreader:
        votes.append(rows[2])
    candidates = list(set(votes))
    # print (candidates)
    numCandidates = len(candidates)
    # print (numCandidates)

    voteList = []
    for rows in csvreader:
        voteList.append(rows[2])
        
    voteCountDict = {}
    for vote in voteList:
        if vote in voteCountDict:
      	    voteCountDict[vote] = voteCountDict[vote] + 1
        else:
            voteCountDict[vote] = 1
    # print (voteCountDict)

    # * The total number of votes each candidate won
    # for lines in range(numCandidates):
    #     votesRec = 0
    #     # print (candidates[lines])
    #     for vote in votes:
    #         if candidates[lines] == votes:
    #             votesRec = votesRec + 1
    #     print (votesRec)
    # for lines in range(numCandidates):
        # print (lines)
        # print (votes)
        # print (candidates[lines])
        # if candidates[lines] == votes:
            # votesRec = 0
            # votesRec = votesRec + 1
        # votesRec = sum(1 if candidates[lines] == votes)
            # print (votesRec)

    # * The percentage of votes each candidate won

    percentCandidate = []
    for c, v in voteCountDict.items():
        percentage = 100.0 * v/totalVotes
        percentCandidate.append(percentage)
    # print(percentCandidate)
    winner = max(percentCandidate)
    winnerIndex = percentCandidate.index(winner)
    # print (winnerIndex)
    
    dictList = []
    for key, value in voteCountDict.items():
        dictList.append([key, value])
    
    # print (dictList)

    results = zip(dictList, percentCandidate)
    for result in results:
        print (result[0][0] + ": " + str(result[1]) + "% (" + str(result[0][1]) + ")")
       
    print ("-------------------------------------------------------")
    print ("Winner: " + dictList[winnerIndex][0])
    print ("-------------------------------------------------------")


# * The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

# Your final script must be able to handle any such similarly-structured dataset in the future 
# (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). 
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open('election.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------------------------------------\n")
    f.write("Total Votes: " + str(totalVotes) + "\n")
    results = zip(dictList, percentCandidate)
    for result in results:
        f.write(result[0][0] + ": " + str(result[1]) + "% (" + str(result[0][1]) + ")\n")
    f.write("-------------------------------------------------------\n")
    f.write("Winner: " + dictList[winnerIndex][0] + "\n")
    f.write("-------------------------------------------------------\n")