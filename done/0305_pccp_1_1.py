import re


def solution(input_string):
    answer = ''
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'w', 'y', 'z']
    alphabets.sort()
    for ch in alphabets:
        s = input_string
        s = re.sub(f'{ch}+', '.', s)
        lumps = s.count('.')
        if lumps > 1:
            answer += ch

    return answer if answer != '' else 'N'
