# Author: Martin Luther Bironga
# Date: 26/1/2021

# Problem statement
"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
"""

def evenness(numbers):
	condition=[int(i) % 2 == 0 for i in numbers.split(" ")]
	return condition.index(True) + 1 if condition.count(True) == 1 else condition.index(False) + 1
