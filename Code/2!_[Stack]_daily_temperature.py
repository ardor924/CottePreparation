#==================================================================
#                       [스택] Daily temperatures
#==================================================================

# 학습용 def코드    
#------------------------
def dailyTemperatures(temperatures) :
    
    # 결과를 저장할 리스트 생성(기본값 : 0)
    days_until_warmer = [0] * len(temperatures)
    
    # 스택
    stack = []
    
    for i in range(len(temperatures)) :
        while stack and temperatures[i] > temperatures[stack[-1]] :
            last_day = stack.pop()
            days_until_warmer[last_day] = i - last_day        
        stack.append(i)
        
    return days_until_warmer
#==================================================================

temperaturesExam  = [30,10,28,20,34,26,27,3]

result = dailyTemperatures(temperaturesExam)
print(f'정답 : {result}')