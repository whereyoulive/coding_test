"""
https://programmers.co.kr/learn/courses/30/lessons/12977

https://www.notion.so/pdg0526/programmers_skilltest-7031dbb7a46045388d6896a9f870d8ee
"""

from itertools import combinations 

def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    
    answer = 0
    A = list(combinations(nums, 3))
    
    for i in A: 
        if check(i[0], i[1], i[2]): 
            answer += 1
                       
    return answer