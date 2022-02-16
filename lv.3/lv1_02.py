"""
https://programmers.co.kr/learn/courses/30/lessons/17682

https://www.notion.so/pdg0526/programmers_skilltest-7031dbb7a46045388d6896a9f870d8ee
"""

def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k') 

    for d in dartResult:
        if d.isdigit():
            x = int(d)

        elif d == 'k':
            x = 10

        elif d == "S":
            x = x**1
            answer.append(x)

        elif d == "D":
            x = x**2
            answer.append(x)

        elif d == "T":
            x = x**3
            answer.append(x)

        elif d == "*":
            if len(answer) != 1:
                answer[-2] = answer[-2]*2
                answer[-1] = answer[-1]*2
            else:
                answer[-1] = answer[-1]*2
                
        elif d == "#":
            answer[-1] = answer[-1]*(-1)
    
    return sum(answer)