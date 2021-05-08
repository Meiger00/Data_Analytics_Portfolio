Michael Eiger  
DSP439  
Exam #4  

# Python Script Name: Exam_4.py

## Q: What does this code do?
- This script takes in a single .txt file where each line only contains a single string (e.g., "ATTTGGATT") and the last line is blank (see the bottom of the README for an example).  The name of the .txt file is specified by the end user as a command line argument. When the program is first executed, the parser will parse out the name of the .txt file containing strings to be analyzed and pass the name to Exam_4.py's main() function as an argument.

- After opening the .txt file, **for each line in the .txt file** (again emphasizing that each line should *only* contain a single string), this script will derive the string name from the line and print it directly to the command line for the end user's review. A pandas data frame is then created that contains columns detailing both the observed and possible kmers, respectively, for each value of k relative to the current string. After the data frame is created, it will be used to calculate the linguistic complexity of the current string. **The linguistic complexity will then be printed directly to the command line.** Lastly, the contents of the data frame will be output to a .csv file with the same name as the string (e.g., the string "ATTTGGATT" would have its data frame output into a .csv called ATTTGGATT.csv).
  - Beyond the main() function, the above process is heavily reliant on combined use of the following functions (each of which is defined within Exam_4.py):  
      1. ffdf

- After each string in the .txt file has been analyzed (i.e., had its linguistic complexity printed on the command line and had its corresponding data frame saved in a .csv file), the .txt file will close and the script will terminate.

## Q: How do I run this script?  

1. To run the Python script (Exam_4.py), first relocate both the script and a .txt file where each line contains only one string to your working directory.  

2. Next, input the following command into your terminal: python3 Exam_4.py (name of the .txt file)  
  
   For example:  
     * python3 Exam_4.py strings.txt

   **Alternatively**, convert Exam_4.py to an executable file by running the following command from your terminal: chmod +x Exam_4.py  
   If you do convert it an executable file, to run the script, you then would also be able to run the program through the following terminal command: ./Exam_4.py (name of the .txt file)  
  
   For example:  
     * ./Exam_4.py strings.txt

3. If you are also interested in running the adjoining Python Test script (test_Exam_4.py), relocate said file to your working directory and input the following command into your terminal: py.test
    * This command will result in an error if your working directory does not also contain Exam_4.py
    * A .txt file containing strings is *not* required to run the Python Test script

## Other notes/limitations of the Python script

- As has been emphasized throughout this README file, the primary limitation of the Python script (Exam_4.py) is that it is currently coded to perform the described analysis on .txt files where every line is a single string without any spaces at the end of the strings (although the newline character is allowed). An example of a legal .txt file can be found in this repository (see "strings.txt"), the format of which is visualized below:  

    ![image](https://user-images.githubusercontent.com/44222667/117521483-09ca7200-af7c-11eb-8ca2-82a5885b622e.png)  
    * Note the blank line on line 4 in the above example. Failure to leave a blank line at the end of your .txt file will skew the computed linguistic complexity AND the observed/possible kmers for the last string in your file. This is because the script was constructed to expect a newline character at the end of each string. For example, the string on line 3 in the above example file ("ATCGATCG") would have its observed/possible kmers and linguistic complexity inaccurately computed if line 4 (a blank line) was not included at the end of the file.

- Future versions of this script would seek to foster/guarantee compatability with alternate file types (e.g., .csv files) through conditional execution of the code based a file's file extension. Additionally, future versions of this script would aim to better handle the newline character at the end of strings and prevent the end user from having to manipulate the .txt file to accomodate for the script's newline character expectation.
