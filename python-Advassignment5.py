#!/usr/bin/env python
# coding: utf-8

# 1.Create a function that takes a number n (integer greater than zero) as an argument, and returns 2 if n is odd and 8 if n is even.
# You can only use the following arithmetic operators:
# addition of numbers +, subtraction of numbers -,
# multiplication of number *, division of number /, and exponentiation **.
# You are not allowed to use any other methods in this challenge (i.e. no if statements, comparison operators, etc).
# Examples:
# f(1) ➞ 2
# f(2) ➞ 8
# f(3) ➞ 2

# In[2]:


def f(in_num):
    output = [8,2]
    print(f'f({in_num})➞ {output[in_num&1]}')
    
f(1)
f(2)
f(3)


# 2.Create a function that returns the majority vote in a list.
# A majority vote is an element that occurs > N/2 times in a list
# (where N is the length of the list).
# Examples:
# 
# majority_vote(["A", "A", "B"]) ➞ "A"
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

# In[3]:


def majority_vote(in_list):
    out_list = None
    for ele in set(in_list):
        if in_list.count(ele) > (len(in_list)/2):
            out_list = ele
    print(f'majority_vote({in_list}) ➞ {out_list}')
    
majority_vote(["A", "A", "B"])
majority_vote(["A", "A", "A", "B", "C", "A"])
majority_vote(["A", "B", "B", "A", "C", "C"])


# 3.Create a function that takes a string txt and censors any word from a given list lst. 
# The text removed must be replaced by the given character char.

# Examples:
# censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
# censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
# censor_string("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"
# 

# In[4]:


def censor_string(in_string_1, in_string_2, rep_char):
    out_string = []
    for ele in in_string_1.split():
        if ele.title() in in_string_2 or ele.lower() in in_string_2 or ele.upper() in in_string_2:
            out_string.append(rep_char*len(ele))
        else:
            out_string.append(ele)
    print(f'censor_string({in_string_1}) ➞ {" ".join(out_string)}')

censor_string("Today is a Wednesday!", ["Today", "a"], "-")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
censor_string("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*")


# 4.In mathematics a Polydivisible Number (or magic number) is a number in a given number base with digits abcde... 
# that has the following properties:
# Its first digit a is not 0.
# The number formed by its first two digits ab is a multiple of 2.
# The number formed by its first three digits abc is a multiple of 3.
# The number formed by its first four digits abcd is a multiple of 4.
# Create a function which takes an integer n and returns True if the given number is a Polydivisible Number and False otherwise.

# Examples:
# is_polydivisible(1232) ➞ True # 1 / 1 = 1 # 12 / 2 = 6 # 123 / 3 = 41 # 1232 / 4 = 308 is_polydivisible(123220 ) ➞ False # 1 / 1 = 1 # 12 / 2 = 6 # 123 / 3 = 41 # 1232 / 4 = 308 # 12322 / 5 = 2464.4 # Not a Whole Number # 123220 /6 = 220536.333... # Not a Whole Number
# 
# def is_polydivisible(in_num):

# In[6]:


def is_polydivisible(in_num):
    output = False
    in_num_temp = str(in_num)
    for ele in range(len(in_num_temp)):
        if(int(in_num_temp[:ele+1])%(ele+1) == 0):
            output = True
        else:
            output = False
            break
    print(f'is_polydivisible({in_num}) ➞ {output}')
        
is_polydivisible(1232)
is_polydivisible(123220)


# 5.. Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
# Examples:
# sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
# sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
# sum_primes([]) ➞ None

# In[7]:


def sum_primes(in_list):
    out_string = []
    for ele in in_list:
        if ele in [2,3]:
            out_string.append(ele)
        elif ele in [6*n-1 for n in range(0,ele)] or ele in [6*n+1 for n in range(0,ele)]:
            out_string.append(ele)
    if 1 in out_string:
        out_string.remove(1)
    print(f'sum_prices({in_list}) ➞ {sum(out_string) if len(out_string) > 0 else None}')
        
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_primes([2, 3, 4, 11, 20, 50, 71])
sum_primes([])


# In[ ]:




