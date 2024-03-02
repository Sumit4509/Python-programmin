# 1. WAP to find the maximum and minimum element of list

# l1=[10,20,30,40,50,60,70]
# print(max(l1))
# print(min(l1))

# 2. WAP to create a list of numbers and print sum of all the elements.

# l1=[10,20,30,40,50,60,70]
# sum =0
# for i in l1:
#     sum+=i
# print("sum is {0}" .format(sum))

# 3. WAP to check list is sorted or not.

# l1= [10,20,30,40,50,60,70]
# n = len(l1)
# a=0
# for i in range(0,n-1,1):
#     if l1[i]>l1[i+1]:
#         a=1
# if a==0:
#     print("array is sorted")
# else:
#     print("array is not sorted")

# 4. WAP to count the occurrence of element in list.

# def count_occurrences(lst):
#     occurrence_dict = {}
#     for item in lst:
#         if item in occurrence_dict:
#             occurrence_dict[item] += 1
#         else:
#             occurrence_dict[item] = 1
#     return occurrence_dict

# # Example usage:
# my_list = [1, 2, 3, 4, 2, 2, 3, 4, 5, 2]
# occurrences = count_occurrences(my_list)
# print("Occurrences of each element in the list:")
# for element, count in occurrences.items():
#     print("Element:", element, "- Count:", count)

# 5. WAP to check weather the list is containnig duplicate elementes or not.

# my_list_with_duplicates = [1, 2, 3, 4, 2, 5, 6, 7, 8]
# a=len(my_list_with_duplicates)
# b=len(set(my_list_with_duplicates))
# # here we put list value in set and check length if same then no duplicate else there is duplicate
# if a==b:
#     print("list does not contain duplicate")
# else:
#     print("list do contain duplicate")

# 6. WAP to display the distinct element of the list.

# def distinct_elements(lst):
#     return list(set(lst))

# # Example usage:
# my_list = [1, 2, 3, 4, 2, 5, 6, 7, 8]
# distinct_list = distinct_elements(my_list)
# print("Distinct elements of the list:", distinct_list)
'''
8. WAP to remove all occurrences of an element from a Python list

def remove_all_occurrences(lst, element):
    return [x for x in lst if x != element]

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 6, 2, 7, 8]
element_to_remove = 2
new_list = remove_all_occurrences(my_list, element_to_remove)
print("Original list:", my_list)
print("List after removing all occurrences of", element_to_remove, ":", new_list)
'''

# 9. Extract Even and odd number from a given list in Python.

'''l1=[1,12,23,47,234,73,123,489,9]
l2=[]
l3=[]
for i in l1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
print("even values",l2)
print("odd values",l3)'''

# 10. Check all elements of a list are the same or not in Python.
'''
l1=[3,3,3,3,3,3,3,3,3]
start = l1[0]
s=0
for i in l1:
    if i!=start:
        s=1
if s==0 :
    print("all elements are same")
else:
    print("all elements are not same")
'''

# 11. Check all elements are unique or not in Python without using set data structure.
'''
def are_elements_unique(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

# Example usage:
my_list = [1, 2, 3, 4, 5]
print(are_elements_unique(my_list))  # Output: True

my_list = [1, 2, 3, 4, 1]
print(are_elements_unique(my_list))  # Output: False

'''

# 12. WAP to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

'''
def count_strings_with_same_first_and_last(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example usage:
string_list = ['aba', 'xyz', 'level', 'hello', 'radar', 'python']
result = count_strings_with_same_first_and_last(string_list)
print("Number of strings where the first and last character are the same:", result)
'''
'''
# 15. WAP to check weather sub list is presented or not in a list.

def sum_of_digits(number):
    # Convert number to string to access individual digits
    number_str = str(number)
    # Sum the digits
    digit_sum = sum(int(digit) for digit in number_str)
    return digit_sum

def sum_of_digits_in_list(lst):
    total_sum = 0
    for number in lst:
        total_sum += sum_of_digits(number)
    return total_sum

# Example usage:
number_list = [123, 456, 789]
result = sum_of_digits_in_list(number_list)
print("Sum of digits of numbers in the list:", result)

'''

# 16. Python program to check if the list contains N consecutive common numbers in Python.
'''
def has_consecutive_common_numbers(lst, N):
    for i in range(len(lst) - N + 1):
        sub_list = lst[i:i+N]
        if len(set(sub_list)) == 1:
            return True
    return False

# Example usage:
my_list = [1, 1, 1, 2, 3, 4, 5]
N = 3
result = has_consecutive_common_numbers(my_list, N)
print("Does the list contain", N, "consecutive common numbers?", result)
'''
'''
# 17. Given two sorted List, L1, and L2 of size n and m. Find the union of two sorted List.

def find_union_sorted_lists(L1, L2):
    union = []
    i = j = 0
    
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            union.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            union.append(L2[j])
            j += 1
        else:  # If both elements are equal
            union.append(L1[i])
            i += 1
            j += 1

    # Add remaining elements from both lists
    while i < len(L1):
        union.append(L1[i])
        i += 1
    
    while j < len(L2):
        union.append(L2[j])
        j += 1

    return union

# Example usage:
L1 = [1, 3, 5, 7, 9]
L2 = [2, 4, 5, 6, 8]
union_result = find_union_sorted_lists(L1, L2)
print("Union of the two sorted lists:", union_result)'''
'''
# 18. given a list of integers, rotating list of elements by k elements right.

def rotate_list_right(lst, k):
    n = len(lst)
    if n == 0:
        return lst
    k = k % n  # Normalize k in case it's larger than the list size
    
    # Split the list into two parts: last k elements and the rest
    first_part = lst[:n - k]
    second_part = lst[n - k:]
    
    # Rotate and rejoin the parts
    rotated_list = second_part + first_part
    
    return rotated_list

# Example usage:
my_list = [1, 2, 3, 4, 5]
k = 2
result = rotate_list_right(my_list, k)
print("Original list:", my_list)
print("List after rotating right by", k, "elements:", result)

'''