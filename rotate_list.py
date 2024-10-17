# Add your clarifying questions here
# Given a list [1, 2, 3, 4, 5] and a number 3, rotate the items in the list 3 places over to the right. The output should be: [3, 4, 5, 1, 2].
#Hard mode: Rotate the list "in-place" without creating a new list.
#Write your clarifying questions and implementation in `rotate_list.py`. To execute your code, run `python3 rotate_list.py` in the terminal.

def rotate_list(list, shift_by):

#### What equation can we do to find new index?? 
    #option 1: taking original index and adding 3 to index (0 + 3 = 3)
    ## handle edge cases where 3 + index >= length of list 
    ### proposed index - (len(list )- 1) - 1
    #option 2: using modulus to find shift amount from 0 for indexes that exceed len 
    ####  new_index = (old_index+shift_by) % (len(list))
    
    
###1
    ### create new variables to make moving things easier: 
    #### Create empty a list of changes 
    #### create a duplicated list of original list

###2
    ### create a loop that finds new location for each index in original list and saves it into the list of changes. 
    #### go the modulus way - try slow first 
    #######- divide it into equations for indexes that don't start over at 0 and indexes that do. 

###3
    ### iterate through list of changes and update duplicated list. 
    ### return list

    pass