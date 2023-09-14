#==================================================================
#         [해시테이블-딕셔너리] Longest consecutive sequence
#==================================================================



# 학습용 def코드 
#------------------------   
def longestConsecutive(nums) :
    # 딕셔너리 생성        
    num_dict = {number: True for number in nums}
    # 가장긴 시퀀스 사이즈 초기화
    max_sequence_size = 0
            
    # 숫자를 리스트에서 추출
    for number in nums:
        # 만일 현재 숫자보다 1만큼 작은수가 딕셔너리에 없을시, 현재 시퀀스 사이즈는 1로설정
        if number - 1 not in num_dict:
            current_number = number
            current_sequence_size = 1
            # 만일 현재 숫자보다 1만큼 큰수가 딕셔너리에 있다면 반복문 적용하여 현재시퀀스사이즈에 += 1 반복
            while current_number + 1 in num_dict:
                current_number += 1
                current_sequence_size += 1
            # 두 시퀀스 사이즈를 비교하여 업데이트  
            max_sequence_size = max(max_sequence_size, current_sequence_size)
            
    # 최종시퀀스 사이즈를 리턴
    return max_sequence_size

#==================================================================

numsExam = [0,3,7,2,5,8,4,6,10,1]

result = longestConsecutive(numsExam)
print(f'정답 : {result}')