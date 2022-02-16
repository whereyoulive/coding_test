"""
https://programmers.co.kr/learn/courses/30/lessons/87390

삽질
https://www.notion.so/pdg0526/n-2-d5f99034e0144a778a7160e679b7a3c2
"""

def solution(n, left, right):
    answer = []
    
    for i in range(int(left), int(right)+1):
        answer.append(max(divmod(i, n)) + 1)

    return answer