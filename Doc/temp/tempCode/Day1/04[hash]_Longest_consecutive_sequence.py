'''
정렬되지 않은 정수 배열이 주어졌을 때, 가장 긴 연속 요소 시퀀스의 길이를 반환합니다.

O(n) 시간 안에 실행되는 알고리즘을 작성해야 합니다.
----------------------------------------------------
예시 1:

입력: nums = [100,4,200,1,3,2]
 출력: 4
 설명: 가장 긴 연속 요소 시퀀스는 입니다 [1, 2, 3, 4]. 그러므로 길이는 4이다.
예 2:

입력: 숫자 = [0,3,7,2,5,8,4,6,0,1]
 출력: 9
 
'''

'''
1. 주어진 리스트에 모든 수를 스택에 넣는다.
2. 만약 딕셔너리 에 있는 숫자+1 인 숫자가 있다면 result에 넣는다
3. result에갯수를 구한다.
4. 최종적으로 가장 길이가 긴 숫자의 합을 출력한다.
'''

nums = [0,3,7,2,5,8,4,6,10,1]

def longestConsecutive(nums) :
    # 숫자를 키로, 해당 숫자의 인덱스를 값으로 가지는 딕셔너리를 생성
    num_dict = {}
    # 가장긴 시퀀스 사이즈 초기화
    max_sequence_size = 0

    # 숫자와 인덱스를 리스트에서 추출1
    for index, number in enumerate(nums) :
        # 딕셔너리에 숫자가 없을때 현재 숫자,인덱스를 딕셔너리에 저장
        if number not in num_dict :
            num_dict[number] = index

    # 숫자를 리스트에서 추출2
    for number in nums:
        # 만일 현재 숫자보다 1만큼 작은수가 딕셔너리에 없을시, 현재시퀀스사이즈는 1로설정
        prev_number = number - 1
        if prev_number not in num_dict :
            current_number = number
            current_sequence_size = 1
            # 만일 현재 숫자보다 1만큼 큰수가 딕셔너리에 있다면 반복문 적용하여 현재시퀀스사이즈에 += 1 반복
            next_number = current_number + 1
            while next_number in num_dict :
                current_number += 1
                current_sequence_size += 1

            # 두 시퀀스 사이즈를 비교하여 업데이트
            max_sequence_size = max(max_sequence_size, current_sequence_size)

    # 최종시퀀스 사이즈를 리턴
    return max_sequence_size
