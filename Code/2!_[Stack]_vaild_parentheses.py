#==================================================================
#                       [스택] Valid parentheses
#==================================================================


# 학습용 def코드    
#------------------------
def isValid(s) :
    # 괄호모음 딕셔너리(키/밸류) 생성
    bracket_pair_dict = {'(': ')', '{': '}', '[': ']'}
    # 열린 괄호용 빈 리스트 생성
    stack_open_bracket_list  = []
    for char in s:
        # 현재 문자가 열린 괄호인 경우, 리스트에 추가
        if char in bracket_pair_dict:  
            stack_open_bracket_list.append(char)
        # 현재 문자가 열린 괄호가 아닌 경우
        else:  
            # 열린 괄호가 없는데 닫힌 괄호가 나온 경우, False리턴
            if not stack_open_bracket_list:  
                return False
            
            # 가장최근에 열린 괄호를 뽑아서 대입
            last_opened_bracket = stack_open_bracket_list.pop() 
            
            # 괄호의 짝이 맞지 않는 경우 False리턴
            if bracket_pair_dict[last_opened_bracket] != char: 
                return False
            
     # 모든 문자를 검사한 후에도 여전히 열려있는 괄호가 남아있다면,
     # 유효하지 않은 입력으로 판단하여 False 리턴, 그렇지 않다면 True 리턴
    return not stack_open_bracket_list  
    

#==================================================================

# parentheses = '()[[]{()' # False
# parentheses = ')()' # False
# parentheses = '[][]{}[{()}]()' # True
parenthesesExam = '[](){}' # True

result = isValid(parenthesesExam)
print(f'정답 : {result}')



