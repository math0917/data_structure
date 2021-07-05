import math
class Route:
    def __init__(self, station, length):
        self.station = station
        self.length = length

class station_from:
    def __init__(self, From, km):
        self.From = From
        self.km = km
#이미 발견한 곳이면 넘어가고 계속 확인해가기 (all connected)
def dfs(graph,start,visited = set()):
    if start not in visited:
        visited.add(start)
        print(start,' ',end='')
        for route in graph[start]:
            if route.station not in visited:
                dfs(graph,route.station,visited)
    return visited
#visited : 최소로 이미 뽑힌 집합 distance : 어디서 왔고 길이최소는 얼마인지를 입력해두는...
def shortest_path(mystation,start,arrival,all_station):
    visited = set()
    visited.add(start)
    distance = dict()
    for i in all_station:
        distance[i]=station_from(None,math.inf)
    distance[start].km = 0
    while len(all_station) > len(visited):
        #기존의 visited들을 순회하면서
        for i in visited: 
            #그 속에서 갈 수 있는 곳들을 다 조사해서 최소값을 바꿔야할 distance값이 있으면 바꾸고
            for j in mystation[i]:
                if j.station not in visited:
                    if (distance[i].km + j.length) < distance[j.station].km:
                        distance[j.station].km = distance[i].km + j.length
                        distance[j.station].From = i
        #한번의 visited시행을 끝내고 입력된 배열중 가장 최소의 값을 visited에 추가하는 작업                
        minimum= math.inf
        for i in distance:
            if i in visited:
                continue
            if minimum > distance[i].km:
                minimum_station = i
                minimum = distance[i].km
        visited.add(minimum_station)
    #이제 나머지는 나의 지나온 루트를 출력해주기 위한 작업인데 이는 From들을 순회하면 됩니다.!
    route = []
    route.append(arrival)
    from1 = distance[arrival].From 
    while from1 != arrival:
        route.append(from1)
        if distance[from1].From is None:
            break
        from1 = distance[from1].From
    
    route.reverse()
    for i in route:
        print(i,'-> ', end='')
    print('(',distance[arrival].km ,'km)')

#mystation은 dict로 value값을 set으로 만들었습니다.
station = ['사당','교대','이수','고속터미널','노량진','용산','흑석','동작','남영','삼각지','약수','대림','숙대입구','충정로','시청','서울','종로3가','충무로','경복궁','청구','동묘앞']
mystation = {'사당':{Route('교대',4.5),Route('대림',11.0),Route('이수',2.7)},#3
             '교대':{Route('사당',4.5),Route('고속터미널',2.7)},#2
             '이수':{Route('대림',9.7),Route('고속터미널',4.0),Route('사당',2.7),Route('동작',2.5)},#4
             '고속터미널':{Route('동작',4.7),Route('이수',4.0),Route('교대',2.7),Route('약수',8.0)},#4
             '노량진':{Route('용산',5.4)},#1
             '용산':{Route('노량진',5.4),Route('흑석',5.3),Route('남영',2.9)},#3
             '흑석':{Route('용산',5.3),Route('동작',6.4)},#2
             '동작':{Route('이수',2.5),Route('고속터미널',4.7),Route('삼각지',6.5),Route('흑석',6.4)},#4
             '남영':{Route('용산',2.9),Route('서울',2.4)},#2
             '삼각지':{Route('동작',6.5),Route('약수',6.2),Route('숙대입구',2.7)},#3
             '약수':{Route('고속터미널',8.0),Route('청구',0.7),Route('충무로',2.1),Route('삼각지',6.2)},#4
             '대림':{Route('사당',11.0),Route('이수',9.7),Route('충정로',10.0)},#3
             '숙대입구':{Route('삼각지',2.7),Route('서울',2.3)},#2
             '충정로':{Route('대림',10),Route('시청',1.9),Route('종로3가',3.0)},#3
             '시청':{Route('충정로',1.9),Route('종로3가',1.9),Route('서울',4.6)},#3
             '서울':{Route('남영',2.4),Route('숙대입구',2.3),Route('충무로',4.6),Route('시청',4.6)},#4
             '종로3가':{Route('충정로',3.0),Route('시청',1.9),Route('충무로',1.9),Route('청구',2.9),Route('동묘앞',2.2),Route('경복궁',2.2)},#6
             '충무로':{Route('종로3가',1.9),Route('서울',4.6),Route('약수',2.1)},#3
             '경복궁':{Route('종로3가',2.2)},#1
             '청구':{Route('종로3가',2.9),Route('약수',0.7),Route('동묘앞',1.2)},#3
             '동묘앞':{Route('종로3가',2.2),Route('청구',1.2)}#2
             }

visited=dfs(mystation,station[0])

starting_point = input('출발역 : ')
arrival_point = input('도착역 : ')

shortest_path(mystation,starting_point,arrival_point, visited)
