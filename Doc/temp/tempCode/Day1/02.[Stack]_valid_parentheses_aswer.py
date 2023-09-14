def isValid(s) :
    pair_bracket_dict = {
                                '{' : '}',
                                '(' : ')',
                                '[' : ']',
                        }
    
    opened_bracket_stack = []
    
    for char in s :
        # 현재 문자가 열린 괄호인 경우 실행
        if char in pair_bracket_dict.keys() :
            opened_bracket_stack.append(char)
        
        # 현재 문자가 열린 괄호가 아닌 경우 실행
        else : 
             # 열린 괄호가 없는데 닫힌 괄호가 나온 경우, False리턴
            if not opened_bracket_stack :
                return False
            # 닫힌 괄호가 나온 경우
            else : 
                # 가장최근에 열린 괄호를에서 문자를 가져옴
                last_opened_bracket = opened_bracket_stack.pop()      
                # 해당 딕셔너리의 열린괄호가 현재 괄호와 쌍을 이루지 않는다면 False리턴                
                if pair_bracket_dict[last_opened_bracket] != char :
                    return False
               
    # print(opened_bracket_stack)
    return not opened_bracket_stack

print(isValid(s))



'''
'(', ')', '{', '}', '[' 및 ']' 문자만 포함된 문자열 s가 주어졌을 때 입력 문자열이 유효한지 확인합니다.

입력 문자열은 다음과 같은 경우에 유효합니다:

1. 열린 대괄호는 같은 유형의 대괄호로 닫아야 합니다.
2. 열린 대괄호는 올바른 순서로 닫아야 합니다.
3. 모든 닫는 대괄호에는 동일한 유형의 열린 대괄호가 있습니다.

예시 1:

입력: s = "()"
 출력: true
예 2:

입력: s = "()[]{}"
 출력: true
예시 3:

입력: s = "(]"
 출력: false

'''