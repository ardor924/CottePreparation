class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 딕셔너리(숫자:인덱스) 생성        
        num_dict = {}
        # 가장긴 시퀀스 사이즈 초기화
        max_sequence_size = 0

        # 숫자와 인덱스를 리스트에서 추출1
        for index, number in enumerate(nums):
            # 딕셔너리에 숫자가 없을때 현재 숫자,인덱스를 딕셔너리에 저장
            if number not in num_dict:
                num_dict[number] = index
                
        # 숫자를 리스트에서 추출2
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
