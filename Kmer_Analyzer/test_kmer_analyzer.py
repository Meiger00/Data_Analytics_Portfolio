################################################################################
#   PYTHON TEST SCRIPT                                                         #
#   Created By: Michael Eiger                                                  #
################################################################################

# To run this test script, input as: 
# py.test

# Import all of the functions (indicated by "*") from the specified .py program (i.e., kmer_analyzer.py)
from kmer_analyzer import *

# Defines a function that tests the count_kmers() function from kmer_analyzer.py
def test_count_kmers():
  '''
  Performs unit testing using the count_kmers() function from kmer_analyzer.py. If all 
  tests are passed, this function will resolve without errors. If a test is NOT 
  passed, this function will throw an assertion error, indicating that the obtained
  value (i.e., the calculated number of observed kmers in a given string) exhibits
  a discrepancy with the expected value (i.e., the expected number of observed 
  kmers in a given string).
  
  Parameters:
  None
  
  Returns:
  None
  '''
  
  # count_kmers() UNIT TEST NUMBER 1
  
    # Indicate the string we are testing
  string = "ATTTGGATT"
  
    # Creating a list of kmer lengths that we wish to test count_kmers() with
  k_list = list(range(1,len(string)+1,1))
  
    # Creating a list of our expected kmer values for the given string
  exp_list = [3,5,6,6,5,4,3,2,1]
  
    # For each potential k value, determine whether the obtained value (i.e., 
    # the calculated number of observed kmers in a given string) exhibits a 
    # discrepancy with the expected value (i.e., the expected number of observed
    # kmers in a given string).
  count = 0
  for k in k_list:
    actual_result = count_kmers(string,k)
    expected_result = exp_list[count]
    count += 1
    assert actual_result == expected_result
    
  # count_kmers() UNIT TEST NUMBER 2
  
    # Indicate the string we are testing
  string = "CATCAT"
  
    # Creating a list of kmer lengths that we wish to test count_kmers() with
  k_list = list(range(1,len(string)+1,1))

    # Creating a list of our expected kmer values for the given string
  exp_list = [3,3,3,3,2,1]
  
    # For each potential k value, determine whether the obtained value (i.e., 
    # the calculated number of observed kmers in a given string) exhibits a 
    # discrepancy with the expected value (i.e., the expected number of observed
    # kmers in a given string).
  count = 0
  for k in k_list:
    actual_result = count_kmers(string,k)
    expected_result = exp_list[count]
    count += 1
    assert actual_result == expected_result

  # count_kmers() UNIT TEST NUMBER 3
  
    # Indicate the string we are testing
  string = "ATCGATCG"
  
    # Creating a list of kmer lengths that we wish to test count_kmers() with
  k_list = list(range(1,len(string)+1,1))

    # Creating a list of our expected kmer values for the given string
  exp_list = [4,4,4,4,4,3,2,1]

    # For each potential k value, determine whether the obtained value (i.e., 
    # the calculated number of observed kmers in a given string) exhibits a 
    # discrepancy with the expected value (i.e., the expected number of observed
    # kmers in a given string).
  count = 0
  for k in k_list:
    actual_result = count_kmers(string,k)
    expected_result = exp_list[count]
    count += 1
    assert actual_result == expected_result

# Defines a function that tests the create_df() function from kmer_analyzer.py
def test_create_df():
  '''
  Performs unit testing using the create_df() function from kmer_analyzer.py. If all 
  tests are passed, this function will resolve without errors. If a test is NOT 
  passed, this function will throw an assertion error, indicating that the obtained
  value (i.e., the calculated number of observed kmers in a given string) exhibits
  a discrepancy with the expected value (i.e., the expected number of observed 
  kmers in a given string) in either the "k", "Observed Kmers", or "Possible
  Kmers" column in the generated data frame.
  
  Parameters:
  None
  
  Returns:
  None
  '''

  # create_df() UNIT TEST NUMBER 1

    # Indicate the string we are testing (i.e., the string we will create a data frame for)
  string = "ATTTGGATT"
  
    # Creating a list of the "actual" legal k values for the given string 
  act_k_list = list(range(create_df(string)['k'].iloc[0], create_df(string)['k'].iloc[len(string)-1]+1,1))
  
    # Creating a list of the "expected" possible k values for the given string
  exp_k_list = list(range(1,len(string)+1,1))
  
    # Determine whether the "actual" value in the "k" column of what will become
    # the generated data frame a discrepancy with the "expected" value for each 
    # value in said column. We are expecting that the "actual values" will just
    # be a list of k-values beginning at 1 and ending at the length of the string.
    # For this unit test, the length of the string would equal 9, so we expect the
    # actual values to include (1,2,3,4,5,6,7,8,9)
  count = 0
  for k in act_k_list:
    actual_result = act_k_list[count]
    expected_result = exp_k_list[count]
    count += 1
    assert actual_result == expected_result

  # create_df() UNIT TEST NUMBER 2 
    # - NOTE: This unit test uses the same string that was used for Unit Test #1
    
    # Creating a list of the "actual" observed kmer values for the given string 
  act_obv_list = list(range(create_df(string)["Observed kmers"].iloc[0], create_df(string)["Observed kmers"].iloc[len(string)-1]+1,1))
  
    # Creating a list of the "expected" observed kmer values for the given string 
  exp_obv_list = [3,5,6,6,5,4,3,2,1]
  
    # Determine whether the "actual" value in what will become the "Observed kmers" column in
    # the generated data frame exhibits a discrepancy with the "expected" value for each 
    # value within said column. 
  count = 0
  for k in act_obv_list:
    actual_result = act_obv_list[count]
    expected_result = exp_obv_list[count]
    count += 1
    assert actual_result == expected_result
    
  # create_df() UNIT TEST NUMBER 3 
    # - NOTE: This unit test uses the same string that was used for Unit Test #1/2
    
    # Creating a list of the "actual" possible kmer values for the given string 
  act_pos_list = list(range(create_df(string)["Possible kmers"].iloc[0], create_df(string)["Possible kmers"].iloc[len(string)-1]+1,1))
  
    # Creating a list of the "expected" possible kmer values for the given string 
  exp_pos_list = [4,8,7,6,5,4,3,2,1]
  
    # Determine whether the "actual" value in what will become the "Possible kmers" column in
    # the generated data frame exhibits a discrepancy with the "expected" value for each 
    # value within said column. 
  count = 0
  for k in act_pos_list:
    actual_result = act_pos_list[count]
    expected_result = exp_pos_list[count]
    count += 1
    assert actual_result == expected_result

# Defines a function that tests the complexity() function from kmer_analyzer.py
def test_complexity():
  '''
  Performs unit testing using the complexity() function from kmer_analyzer.py. If all 
  tests are passed, this function will resolve without errors. If a test is NOT 
  passed, this function will throw an assertion error, indicating that the 
  obtained value (i.e., the calculated linguistic complexity of a given string) 
  exhibits a discrepancy with the expected value (i.e., the expected linguistic 
  complexity of a given string) as derived from values in the data frame returned
  by create_df().
  
  Parameters:
  None
  
  Returns:
  None
  '''
  
    # Create a list of strings that we will calculate the linguistic complexity
    # of for the purpose of unit testing and store it in a variable "string_list"
  string_list = ["ATTTGGATT", "CATCAT", "ATCGATCG", "TAAGAAT", "GTACAGTG"]
  
    # Create a list of expected linguistic complexity values where each value's index
    # corresponds to the index of the string in string_list, which is the string
    # to which the calculated linugistic complexity belongs
  exp_list = [0.875, 0.7894736842105263, 0.8125, 0.92, 0.96875]
  
    # Creating a for loop that will iterate through a sequence of operations for
    # each string in string_list
  count = 0
  for string in string_list:
    df = create_df(string)
    actual_result = complexity(df)
    expected_result = exp_list[count]
    count += 1
    assert actual_result == expected_result
