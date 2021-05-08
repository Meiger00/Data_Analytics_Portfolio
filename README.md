Michael Eiger  
DSP439  
Exam #4  

# Python Script Name: Exam_4.py

## Q: What does this script do?
This script takes in a single .txt file where each line only contains a single string (e.g., "ATTTGGATT").  The name of the .txt file is specified by the end user as a command line argument. When the program is first executed, the parser will parse out the name of the .txt file containing strings to be analyzed and pass the name to Exam_4.py's main() function as an argument.

For each line in the .txt file, this script will derive the string name and print the string name directly to the command line for the end user's review. A pandas data frame is then created that contains columns detailing both the observed and possible kmers, respectively, for each value of k relative to a given string.

## Q: How do I run this script?  
