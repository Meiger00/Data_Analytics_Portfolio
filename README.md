Michael Eiger  
DSP439  
Exam #4  

# Python Script Name: Exam_4.py

## Q: What does this code do?
This script takes in a single .txt file where each line only contains a single string (e.g., "ATTTGGATT").  The name of the .txt file is specified by the end user as a command line argument. When the program is first executed, the parser will parse out the name of the .txt file containing strings to be analyzed and pass the name to Exam_4.py's main() function as an argument.

After opening the .txt file, **for each line in the .txt file** (again emphasizing that each line should *only* contain a single string), this script will derive the string name from the line and print it directly to the command line for the end user's review. A pandas data frame is then created that contains columns detailing both the observed and possible kmers, respectively, for each value of k relative to the current string. After the data frame is created, it will be used to calculate the linguistic complexity of the current string. **The linguistic complexity will then be printed directly to the command line.** Lastly, the contents of the data frame will be output to a .csv file with the same name as the string (e.g., the string "ATTTGGATT" would have its data frame output into a .csv called ATTTGGATT.csv).

After each string in the .txt file has been analyzed (i.e., had its linguistic complexity printed on the command line and had its corresponding data frame saved in a .csv file), the .txt file will close and the script will terminate.

## Q: How do I run this script?  

To run the Python script (Exam_4.py), first relocate both the script and a .txt file where each line contains only one string to your working directory.  

Next, input the following command into your terminal: python3 Exam_4.py (name of the .txt file)  
For example:  
* python3 Exam_4.py strings.txt
