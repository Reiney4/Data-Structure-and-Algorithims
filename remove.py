"""
----------------------- Question 2 --------------------------------------
 Write a function remove_duplicates(sequence) that takes a 
sequence (list or tuple) and returns a new sequence with duplicates 
removed while maintaining the original order of elements. 

sample input = 

result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
"""

# ----------works but does not keep the order-------------
# def remove_duplicates(seq):
#     return list(set(seq))


def remove_duplicates(seq):
    unique_list = list()
    # iterate thru the seq
    for el in seq:
        # check if the element exists in the unuque list
        if el not in unique_list:
            # if no, append it
            unique_list.append(el)
    return unique_list


input_sequence = [1, 1, 11, 1, 1, 2, 3, 2, 4, 5, 3, 6, 7, 5]
print(remove_duplicates(input_sequence))