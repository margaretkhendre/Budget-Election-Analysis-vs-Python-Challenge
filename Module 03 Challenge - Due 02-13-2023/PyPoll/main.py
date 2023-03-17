#import the csc and modules
import os 
import csv

#load data to read survey data
input_file = os.path.join("Resources", "election_data.csv")

#output file location for the survey analysis
output_file= os.path.join("Election Results Analysis.txt")

#variables 
total_votes= 0 # variables that holds the total number of votes
candidates= [] # list that holds the candidates in the survey 
candidate_votes= {} # dictionary that will hold the votes each candidate receives
winning_count= 0 # holds the winning count
winning_candidate = "" # variable to hold the winning candidate

#read the csv file
with open(input_file) as surveyData:
    #create the csv reader
    csvreader = csv.reader(surveyData)

    #read the header
    header = next(csvreader)

    #rows will be lists 
        #index 0 is the ballot id 
        #index 1 is the county
        #index 2 is the candidate
    
    # for each row
    for row in csvreader:
        # add on to the total votes
        total_votes += 1 #same as total _votes = total_votes +1

        #check to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            # if the candidate is not in the list, add the candidate to the list 
            candidates.append(row[2])

            # add the value to the dictionary as well
            #("key": value)
            #start the count at 1 for the votes
            candidate_votes[row[2]] = 1

        else:
            # the candidate is in the list of candidates
            # add a vote to that candidate count
            candidate_votes[row[2]]+= 1

#print(candidate_votes)
candidate_output = ""
for candidates in candidate_votes:
    #get the vote count and percentage of votes
    votes= candidate_votes.get(candidates)
    vote_pct= (float(votes) / float(total_votes)) * 100.00
    vote_totals= float(votes) 

    #compare votes to winning count
    if votes > winning_count:
        # update the votes to be the new winning count
        winning_count = votes
        #update the winning candidate
        winning_candidate = candidates

    #winning candidate output
    winning_candidate= f"{winning_candidate}\n"

    # percentages with totals output
    candidate_output += f"\t {candidates}: {vote_pct:.3f}% , ({vote_totals})\n"
    #print(candidate_output)

#create an output variable to hold the  output
output= (
    f"\n\n Election Results\n"
    f"-----------------------------------------\n"
    f"\t Total Votes: {total_votes:,} \n" #separate by thousands
    f"-----------------------------------------\n"
    f"{candidate_output} \n"
    f"-----------------------------------------\n"
    f"\t  Winner: {winning_candidate}"

)

print(output)

#print the results and export the data to the text file 
with open(output_file, "w") as text_file:
    #write the output to the fil
    text_file.write(output)