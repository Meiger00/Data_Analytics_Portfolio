#!/usr/bin/env python3

################################################################################
#   Michael Eiger                                                              #
#   kmer_analyzer - PYTHON SCRIPT                                              #
################################################################################

# To run this script in your terminal, first place this file and the .txt file 
# containing the strings you want to analyze in your working directory. 
# Then input one of the following commands in your terminal:
#   python3 kmer_analyzer.py
#
#   OR
#
#   chmod +x kmer_analyzer.py <-- (Converts the .py file to an executable, then you run it)
#   ./kmer_analyzer.py

# Import libraries required to run this program
import pandas as pd  
import parser        
import argparse    

# Defining the function that will count kmers of size k in a passed string
def count_kmers(string, k):
    '''
    This function calculates the number of observed kmers of size of a specified 
    size (k) within a passsed string.
    
    Parameters: 
    (1) String (str): The string with which the function will determine the observed
                      kmers of size k
    (2) k (int): The desired kmer length
    
    Returns: 
    (1) Int: The number of observed kmers of size k for the passed string
    '''
    
    # Validating user input via a series of statements involving the assert operator
    # to prevent illegal values/structures being passed to count_kmers(). If any 
    # of the adjoining boolean expressions evaluate to False, an assertion-based
    # error will be thrown
    assert k <= len(string)
    assert k > 0
    assert len(string) > 0
    assert type(string) == str
    assert type(k) == int
    
    # Creating a for loop that will iterate a number of times equal to the length
    # of a passed string (e.g., "CAT" would cause the loop to iterate 3 times because
    # len("CAT") = 3)
    count = 0
    temp = k
    observed = []
    for i in range(len(string)):
        if (string[count:k] not in observed) and (len(string[count:k]) == temp):
            observed.append(string[count:k])
        count += 1
        k += 1
    
    # Return the number of observed kmers to the outside of this function
    return len(observed)

# Defining a function that will create a pandas data frame containing all possible
# values of k relative to a passed string's length, as well as the associated
# number of observed and possible kmers
def create_df(string):
    '''
    Creates a pandas data frame containing all possible values of k relative to 
    a passed string's length, as well as the associated number of observed and 
    possible kmers for that string.

    Parameters:
    (1) String (str): The string for which a pandas data frame will be created 
                      based on its observed/possible kmers
    
    Returns: 
    (1) pandas.core.frame.DataFrame: Includes three columns - k, Observed kmers, 
                                     and Possible kmers for the string
    '''
    # Validating user input via a series of statements involving the assert operator
    # to prevent illegal values/structures being passed to create_df(). If any 
    # of the adjoining boolean expressions evaluate to False, an assertion-based
    # error will be thrown
    assert len(string) > 0
    assert type(string) == str
    
    # Establishing lists that will store what will eventually become the values 
    # of the respective k, observed kmers, and possible kmers columns in the pandas data frame
    k = []
    observed = []
    possible = []
    
    # Creating a for loop that will iteratively determine the observed kmer and possible kmer
    # for each k value relative to the passed string.
    for i in range(1,len(string)+1): 
        k.append(i)
        observed.append(count_kmers(string, i))
        
        # To determine the number of possible kmers for the given string, we establish 
        # the minimum value between (1) the length of the string - k + 1 versus (2) 4^k
        if ((len(string) - i + 1) <= 4**i):
            possible.append(len(string) - i + 1)
        else:
            possible.append(4**i)
    
    # Establishing a dictionary that will serve as the data used to construct the
    # pandas data frame
    df = {'k': k, 'Observed kmers': observed, "Possible kmers": possible}
    
    # Creating the pandas data frame using the dictionary
    df = pd.DataFrame(data = df)
    
    # Returning the data frame object to the outside of this function
    return df

# Defining the function that will calculate linguistic complexity
def complexity(df):
    '''
    Calculates the linguistic complexity of a string by dividing its number of 
    observed kmers by its number of possible kmers.
    
    Parameters:
    (1) df (pandas.core.frame.DataFrame): Details the observed/possible kmers for 
                                each potential value of k relative to the size of
                                a given string. Expected to be in a format congruent
                                with the outputof create_df() (i.e. the data frame 
                                should have columns in the following order: "k",
                                "Observed kmers", "Possible kmers")
    
    Returns: 
    (1) Numpy.float64: Represents the linguistic complexity of the string whose 
                       observed/possible kmers are detailed by the pandas data frame
    '''
    
    # Validating user input via a series of statements involving the assert operator
    # to prevent illegal values/structures being passed to complexity(). If any 
    # of the adjoining boolean expressions evaluate to False, an assertion-based
    # error will be thrown
    assert type(df) == pd.core.frame.DataFrame
    assert df.columns[1] == "Observed kmers"
    assert df.columns[2] == "Possible kmers"
    
    # Creating a pandas Series that will store both the sum of all observed kmers and possible kmers,
    # respectively, from the passed data frame
    sums = df.sum(axis = 0)[1:3]
    
    # Linguistic complexity = Number of observed kmers/Number of possible kmbers
    complexity = sums[0]/sums[1]
    
    # Returning the value representing linguistic complexity to the outside of the function
    return complexity

# Defining the main function
def main(args):
    '''
    Reads in and opens a .txt file containing one string per line, then iteratively
    creates a pandas data frame (by calling create_df()) indicating the string's 
    number of observed and possible kmers, respectively. On each iteration, this
    function will print the linguistic complexity of the passed string directly to
    the command line AND create a .csv file  containing the created pandas data frame.
    
    Parameters: 
    (1) Args (str): The name of a .txt file containing strings to be analyzed
    
    Returns: 
    None
    '''
    # Validating that the user is trying to analyze strings from within a .txt file.
    # If the following boolean expressions evaluate to False, an assertion-based
    # error will be thrown
    assert args.file.endswith(".txt") == True
    
    # Open the file originally declared by the user as a command line argument
    strings = open(args.file, "r")
    
    # For each string in the file
    for string in strings:
        
        # Print the name of the string to the command line
        print("String: " + str(string))
        
        # Create a pandas data frame using the current string, making sure to prevent each line's newline character from being analyzed too
        df = create_df(j[0:len(string)-1])
        
        # Printing the linguistic complexity of the current string to the command line
        print("Calculated Linguistic Complexity for " + str(string[0:len(string)-1]) + ": " + str(complexity(df)))
        
        # Printing the name of the .csv file that will store the pandas data frame to the command line
        print("The data frame depicting k-mers for this string has been saved to the following file: " + str(string[0:len(string)-1]) + ".csv")
        
        # Creating the .csv file based on the content of the pandas data frame
        df.to_csv(str(string[0:len(string)-1]) + ".csv",index=False)
        
        # Printing an empty line to the command line to improve readability
        print("")
    
    # Close the file containing the strings to prevent errors
    strings.close()
    
    # Return nothing to the outside of the function
    return

# If we are running the main program, parse out the name of the file containing the strings
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str)
    args = parser.parse_args()
    main(args)
