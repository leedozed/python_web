#정규식 사용하기
# 1. p = re.compile("원하는 형탸")
# 2. m = p.match("비교할 문자열")
# 3. lst = p.findall("비교할 문자열"): 일치하는 모든 것을 리스트형태로 반환

# . (ca.e) 하나의 문자열 - case
# ^ (^de) 문자열의 시작



import re

p = re.compile("ca.e") #.: 하나의 문자를 의미함 / ^: 문자열의 시작 / $:문자열의 끝

m = p.match("good care")
# print(m.group())

def print_match(m):
    if m:
        print("m.group():", m.group()) #일치하는 문자열 반환
        print("m.string:", m.string) #일치하는 문자열 전체
        print("m.start():", m.start()) #일치하는 문자의 시작 index
        print("m.end():", m.end()) #일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열의 시작, 끝 index
    else:
        print("not match")

# m = p.match("case") #match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") #search: 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") #findall: 일치하는 모든 것을 리스트 형태로 반환
print(lst)


