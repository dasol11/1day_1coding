def sol (N):
    
    x_li = ["1", "2", "3", "4", "5", "6", "7", "8"]
    y_li = ["a", "b", "c", "d", "e", "f", "g", "h"]
    x = 0
    y = 0
    for i in range(8):
        if x_li[i] == N[1]:
            x += i
        if y_li[i] == N[0]:
            y += i
            
    count = 0
    
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [-1, 1, -1, 1, 2, -2, 2, -2]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx <= 7 and 0 <= ny <= 7 :
            count += 1
            
    return count


a = sol("a1")
print(a) 

"""
row = int (N[1]) 
col = int(ord(N[0]))-int(ord(N["a"]) +1
ord()
문자열을 받아 아스키 코드로 변환해서 숫자를 받아오는 함수
a~h 까지의 알파벳이 존재하기 때문에 아스키로 변환 후 a의 아스키를 빼주고 1을 더해줘서 y축을 구함 
"""