#==================================================================
#               [그래프] Keys and rooms
#==================================================================

'''Instruction
0부터 n-1까지 번호가 붙은 방이 n개 있고, 0번 방을 제외한 모든 방이 잠겨 있습니다. 
여러분의 목표는 모든 방을 방문하는 것입니다. 단, 열쇠가 없으면 잠긴 방에 들어갈 수 없습니다.

한 방을 방문하면 그 방에서 고유한 열쇠 세트를 찾을 수 있습니다. 
각 열쇠에는 잠금 해제되는 방을 나타내는 번호가 적혀 있으며, 
모든 열쇠를 가지고 다른 방의 잠금을 해제할 수 있습니다.

방[i]가 방 i를 방문했을 때 얻을 수 있는 열쇠의 집합인 방 배열이 주어졌을 때, 
모든 방을 방문할 수 있으면 참을 반환하고 그렇지 않으면 거짓을 반환합니다.

예시 1:

입력: Rooms = [[1],[2],[3],[]]
 출력: true
 설명: 
우리는 0호실을 방문하여 1호실을 수령합니다.
그런 다음 방 1을 방문하여 열쇠 2를 수령합니다.
그런 다음 방 2를 방문하여 열쇠 3을 수령합니다.
이어서 3호실을 방문합니다.
모든 방을 방문할 수 있었으므로 true를 반환합니다.
예 2:

입력: Rooms = [[1,3],[3,0,1],[2],[0]]
 출력: false
 설명: 방을 잠금 해제하는 유일한 열쇠가 방 번호 2에 있기 때문에 방 번호 2에 들어갈 수 없습니다.
'''
# URL : https://leetcode.com/problems/keys-and-rooms/


# 학습용 def코드 
#------------------------   
def canVisitAllRooms(rooms):
    already_visited_room = {}
    def dfs(current_room):
        already_visited_room[current_room] = True
        for next_room in rooms[current_room]:
            if next_room not in already_visited_room:
                dfs(next_room)
    dfs(0)
    return len(already_visited_room) == len(rooms)

#==================================================================

roomsExam =[[1],[2],[3],[]]

result = canVisitAllRooms(roomsExam)
print(f'정답 : {result}')