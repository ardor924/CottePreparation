s = ')[{{{{}}}}](){}{}()(){}{}[]'


def is_valid(s) :
    
    bracket_dict = {
                        '{' : '}',
                        '(' : ')',
                        '[' : ']',
                   }
    
    opened_bracket_stack = []
    
    for char in s : 
        # 현재 문자가 열린 괄호인 경우
        if char in bracket_dict.keys() :
            opened_bracket_stack.append(char)
        # 현재 문자가 열린 괄호가 아닌경우
        else :
            # 열린괄호 없이 스택에 괄호가 있는경우
            if not opened_bracket_stack :
                return False
            # 현재 문자가 닫힌 괄호인 경우
            else :
                # 스택에서 가장 최근 열린 괄호문자 가져와서
                last_opened_bracket = opened_bracket_stack.pop()
                # 현재 닫힌 문자와 딕셔너리에 키:밸류 비교 후 
                if bracket_dict[last_opened_bracket] !=  char :
                    # 문자가 다를시  False리턴
                    return False
                
    # 스택에 문자가 하나라도 남는다면 False 리턴, 
    # 문자가 없다면 모두 쌍을 찾은것이므로 True 리턴          
    return not opened_bracket_stack
                    
    
    
    
print(is_valid(s))