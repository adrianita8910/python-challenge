import os
import csv

#Path to collect the data
election_csv = os.path.join("..", "Resources", "election_data.csv")

#Specify an output folder
output_path = os.path.join("Elections_Results.txt")


#Open and read the csv file
with open (election_csv, newline="") as csvFile:

    # Split the data with delimiters
    csvreader = csv.reader(csvFile, delimiter=",")

    #Skip the header row
    csv_header = next(csvFile)
    #print(f"Header:{csv_header}")

    #Define
    totalVotesCount = 0
    votes = []
    candidateCount = []
    uniqueCandidates = []
    percent = []

    for row in csvFile:
        #Total number of votes
        totalVotesCount += 1

        #Append unique names to the candidates list
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

        #Make a list of all the votes
        votes.append(row[2])

    # Loop for populate candidatesCount with each vote
    for candidate in uniqueCandidates:
        candidateCount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalVotesCount*100,3))

    #Find the winner 
    winner = uniqueCandidates[candidateCount.index(max(candidateCount))]

#Print Results
print("Elections Results")
print("----------------------------")
print(f"Total votes: {totalVotesCount}")
print("----------------------------")
for count in range(len(uniqueCandidates)):
        print(f'{uniqueCandidates[count]}: {percent[count]}% {candidateCount[count]}')
print("----------------------------")
print(f"Winner: {winner}") 

#Export the file to the text file
with open(output_path, "w") as textFile:
    textFile.write("Elections Results")
    textFile.write("----------------------------")
    textFile.write(f"Total votes: {totalVotesCount}")
    textFile.write("----------------------------")
    for count in range(len(uniqueCandidates)):
        textFile.write(f'{uniqueCandidates[count]}: {percent[count]}% {candidateCount[count]}')
    textFile.write("----------------------------")
    textFile.write(f"Winner: {winner}") 


