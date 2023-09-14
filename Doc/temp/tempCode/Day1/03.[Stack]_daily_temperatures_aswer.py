'''
정수 온도 배열이 일일 온도를 나타낼 때, answer[i]가 따뜻한 온도를 얻기 위해
이후 기다려야 하는 일수가 되도록 배열의 답을 반환합니다. 
이것이 가능한 미래 날짜가 없는 경우 대신 answer[i] == 0을 유지합니다

예시 1:

입력: 온도 = [73,74,75,71,69,72,76,73]
 출력: [1,1,4,2,1,1,0,0]
예 2:

입력: 온도 = [30,40,50,60]
 출력: [1,1,1,0]
예시 3:

입력: 온도 = [30,60,90]
 출력: [1,1,0]

'''



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_day = stack.pop()
                result[last_day] = i - last_day
            stack.append(i)
        
        return result