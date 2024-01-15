#!/usr/bin/env python
# coding: utf-8

# 1.Write a python program for the following:
# – Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the
# resultantstring and print it.
# Sample input:
# •python
# •Sample output:
# •ntyp




def delete_and_reverse(string):
 char_list = list(string)  #  Converting string to list of characters
 del char_list[2:4]  # Deleting at least 2 characters
 char_list.reverse()  # Reverse the list
 return "".join(char_list)  # Join the list back to a string and return it

# Example usage of function
original_string = "Python"    # Input string 
modified_string = delete_and_reverse(original_string)  # Calling the function
print(f"Original string: {original_string}")  # printing the original string
print(f"Modified string: {modified_string}")  # # printing the modified string


# – Take two numbers from user and perform at least 4 arithmetic operations on them.




def arithmetic_operations(a, b):
    # Performing and printing 4 arithmetic operations
    print("Addition of first and second: ",a+b) # Performing and Printing addition operation
    print("Multiplication of first and second: ",a*b) # Performing and Printing multiplication operation
    print("Modulus of first and second: ",a%b) # Performing and printing modulus operation
    print("Exponential of first and second: ",a**b)   # Performing and Printing exponential operation

a = float(input("Enter the first number: "))   # Getting user input1 and typecasting it from string to float
b = float(input("Enter the second number: "))  # Getting user input2 and typecasting it from string to float
arithmetic_operations(a,b)                     # Calling the function


# 2.Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.
# •Sample input:
# •I love playing with python
# •Sample output:
# •I love playing with pythons




def replace_each_occurence(word):
    new_word = word.replace('python','pythons') # replace word python with pythons
    return new_word  # return replaced word

word = "python"   # input word 
modified_word = replace_each_occurence(word)  # calling function

print(f"Original word: {word}") # printing original word
print(f"Modified word: {modified_word}") # printing modified word


# 3.Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the
# grading scheme we are using in this class.hons
# 




def grade_card(score):
    if score >= 90:   # Check for scores in the A grade range
        return 'A grade' # returns grade 
    elif score >= 80:    # Check for scores in the B grade range
        return 'B grade' # returns grade 
    elif score >= 70:    # Check for scores in the C grade range
        return 'C grade' # returns grade 
    elif score >= 60:    # Check for scores in the D grade range
        return 'D grade' # returns grade 
    else:          # Check for scores in the  grade range
        return 'Fail'    # returns grade 

score = int(input("Enter score of the student: "))  # taking input from user and converting into int
score_card = grade_card(score)  # calling function

print(f"Score of the student: {score}") # printing Score of the student
print(f"Grade of the student: {score_card}") # printing Grade of the student







