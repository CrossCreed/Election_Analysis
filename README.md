# Election_Analysis
## Overview of Election Audit with Python:

### Purpose
___
The purpose of this project was to further analyze the Module data and present the following voting information to the election commission:
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

Once finished, we will have visibility over:
* The total number of votes cast in the election
* The candidates who ran and how many votes each one of them received
* The vote percentage spread per candidate
* Overall winner

The data for the project is taken from the **election_results.csv** file provided in **Module 3** for python.

### Election-Audit Results
___
Below is a screenshot of the output from the script of this project presenting the results of this challenge:

![image](https://user-images.githubusercontent.com/89520192/134829212-1b362ab9-9de9-41b0-aa21-38cda32e3943.png)

A total of 369,711 votes were cast in this congressional election spread among the three counties in the precint: 

Arapahoe, Denver and Jefferson

![image](https://user-images.githubusercontent.com/89520192/134830111-2b1141c0-fe7f-4c35-a59e-b3736427f09c.png)

* Denver county received 82.8% of the vote (306,055 votes). 
* Jefferson county creceived 10.5% of the vote (38,855 votes). 
* Araphoe county received 6.7% of the vote (24,801 votes).
* Denver county had the largest number of votes.

![image](https://user-images.githubusercontent.com/89520192/134830130-6e749481-eb4f-42a9-8593-9040740d6f6a.png)
     
The breakdown of the number of votes and the percentage of the total votes for the three condidates in this election:

* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)

Diana DeGette won the election with a total number of 272,892 votes, counting for 73.8% of the total vote.

### Election-Audit Summary

The script can be re-used for any future election the commission sees fit. 
1. Adding another if statement to this script could further inquire about the percentage of each county vote for each candidate.
This would allow for more accurate prediction of votes to certain candidates or parties according to the county where voting takes place. 
2. The addition of demographic analytics. Using demographics as an influencing characteristic for the votes cast in this election could provide further insight into the spread of votes cast across the counties. 

**Note that for the above changes to be implemented in the script for future elections, more data columns would be required for analysis in the original CSV file such as age column, if one would like to analyze demographics.**

