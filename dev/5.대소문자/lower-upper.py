#string 중 소문자 count 비교
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

# 대소문자 변환
def changeCase(inputData):
    resultData = ""
    for word in inputData:
        if(word.isupper()):
            resultData = resultData + word.lower()
        else :
            resultData = resultData + word.upper()
    return resultData