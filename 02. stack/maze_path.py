import copy
STACKSIZE = 100

class Stack:
    def __init__(self):
        self.items = [0] * STACKSIZE
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == STACKSIZE - 1

    def push(self, val):
        if not self.isFull() :
            self.top += 1
            self.items[self.top] = val

    def pop(self):
        if not self.isEmpty() :
            retvalue = self.items[self.top]
            self.top -= 1
            return retvalue
    def speek(self):
        if not self.isEmpty():
            return self.items[self.top]

class maze_element: #state는 정수로 저장하여 각 위치당 1 2 4 8과 비트연산을 통해 열린곳을 조사하겠다.
    def __init__(self,state):
        self.state=state
        self.istake=0  #istake는 stack에 넣어져있는 갈림길이면 갈 수 없도록 만들기 위해서 선언했다.
        self.up=1  #이미 stack에 넣어서 조사한 구역이면 갈 수 없도록 하였다 예를들어 갈림길에서 이번 스택에서는
        self.right=1 #위로가는 것을 조사했으면 right=0이되고 다음 스택에 올때에는 위로 갈 수 없게 된다.
        self.down=1
        self.left=1
    def oneway(self): #길이 한개인것
        if (((self.state)&1)/1 + ((self.state)&2)/2 + ((self.state)&4)/4 + ((self.state)&8)/8) == 1:
            return True
        else: return False
    def twoway(self):#길이 두개인것
        if (((self.state)&1)/1 + ((self.state)&2)/2 + ((self.state)&4)/4 + ((self.state)&8)/8) == 2:
            return True
        else : return False
    def threeway(self):#길이 3개인것
        if (((self.state)&1)/1 + ((self.state)&2)/2 + ((self.state)&4)/4 + ((self.state)&8)/8) == 3:
            return True
        else : return False
    def isup(self): #갈림길에서 각각 위로갈수 있는지 물어보는 함수 (self.up)과 관련이 있다.
        if self.up==1:
            return True
        else: return False
    def isright(self):
        if self.right==1:
            return True
        else: return False
    def isdown(self):
        if self.down==1:
            return True
        else: return False
    def isleft(self):
        if self.left==1:
            return True
        else: return False
class stack_data: #스택에 지금 현재 좌표와 count를 넣어놓고 만약 갔는데 막다른 길이면 다시 돌아오면서 기억해둘 변수
    def __init__(self,xcoord,ycoord,count):
        self.xcoord=xcoord
        self.ycoord=ycoord
        self.count=count
class stack_use: #스택에 push했는지 pop했는지 정보를 계속 남겨둘 변수 (나중에 스택사용 횟수 출력하기위해서)
    def __init__(self,what,xcoord,ycoord,count):
        self.what=what
        self.xcoord=xcoord
        self.ycoord=ycoord
        self.count=count
    def __str__(self): # 나중에 어떠한 스택을 사용했는지 출력할때 쓸 print(self)할때... 
        if self.what==0:
            return 'push({},{}),count {}'.format(self.xcoord,self.ycoord,self.count)
        else:
            return 'pop({},{}),count {}'.format(self.xcoord,self.ycoord,self.count)
def go(row,col,i): #각각의 위치에서 위로가면 i=1 오른쪽 i=2, 아래쪽 i=4, 왼쪽 i=8 각각의 row col의 변화
    if i==1:
        return row-1,col
    elif i==2:
        return row,col+1
    elif i==4:
        return row+1,col
    else:
        return row,col-1
class display: #나중에 출력해내기위해 경로의 위치를 저장해두는 class ㅋ
    def __init__(self,xcoord,ycoord):
        self.xcoord=xcoord
        self.ycoord=ycoord

maze=[]
arr=[]                 #1 2 4 8
arr.append(maze_element(6))
arr.append(maze_element(10))
arr.append(maze_element(10))
arr.append(maze_element(12)) 
arr.append(maze_element(2))
arr.append(maze_element(10))
arr.append(maze_element(14))
arr.append(maze_element(12))
arr.append(maze_element(4))
#2번째
maze.append(arr)
arr=[]                 #1 2 4 8
arr.append(maze_element(3))
arr.append(maze_element(10))
arr.append(maze_element(12))
arr.append(maze_element(5)) 
arr.append(maze_element(6))
arr.append(maze_element(10))
arr.append(maze_element(13))
arr.append(maze_element(5))
arr.append(maze_element(5))     
#3번째
maze.append(arr)
arr=[]                 #1 2 4 8
arr.append(maze_element(6))
arr.append(maze_element(10))
arr.append(maze_element(13))
arr.append(maze_element(3)) 
arr.append(maze_element(9))
arr.append(maze_element(6))
arr.append(maze_element(9))
arr.append(maze_element(5))
arr.append(maze_element(5))
maze.append(arr)
#4번째
arr=[]
arr.append(maze_element(5))
arr.append(maze_element(4))
arr.append(maze_element(1))
arr.append(maze_element(4)) 
arr.append(maze_element(4))
arr.append(maze_element(1))
arr.append(maze_element(6))
arr.append(maze_element(11))
arr.append(maze_element(13))
maze.append(arr)
#5번째
arr=[]                 #1 2 4 8
arr.append(maze_element(5))
arr.append(maze_element(5))
arr.append(maze_element(6))
arr.append(maze_element(13)) 
arr.append(maze_element(3))
arr.append(maze_element(10))
arr.append(maze_element(9))
arr.append(maze_element(6))
arr.append(maze_element(13))
maze.append(arr)
#6번째
arr=[]                 #1 2 4 8
arr.append(maze_element(7))
arr.append(maze_element(9))
arr.append(maze_element(5))
arr.append(maze_element(7)) 
arr.append(maze_element(10))
arr.append(maze_element(8))
arr.append(maze_element(2))
arr.append(maze_element(9))
arr.append(maze_element(5))
maze.append(arr)
#7번째
arr=[]                 #1 2 4 8
arr.append(maze_element(3))
arr.append(maze_element(10))
arr.append(maze_element(9))
arr.append(maze_element(5)) 
arr.append(maze_element(6))
arr.append(maze_element(10))
arr.append(maze_element(10))
arr.append(maze_element(14))
arr.append(maze_element(13))
maze.append(arr)
#8번째
arr=[]                 #1 2 4 8
arr.append(maze_element(4))
arr.append(maze_element(6))
arr.append(maze_element(10))
arr.append(maze_element(9)) 
arr.append(maze_element(5))
arr.append(maze_element(6))
arr.append(maze_element(10))
arr.append(maze_element(9))
arr.append(maze_element(1))
maze.append(arr)
#9번째
arr=[]                 #1 2 4 8
arr.append(maze_element(5))
arr.append(maze_element(3))
arr.append(maze_element(10))
arr.append(maze_element(14)) 
arr.append(maze_element(9))
arr.append(maze_element(3))
arr.append(maze_element(14))
arr.append(maze_element(10))
arr.append(maze_element(12))
maze.append(arr)
#10번째
arr=[]                 #1 2 4 8
arr.append(maze_element(7))
arr.append(maze_element(10))
arr.append(maze_element(12))
arr.append(maze_element(7)) 
arr.append(maze_element(12))
arr.append(maze_element(4))
arr.append(maze_element(1))
arr.append(maze_element(4))
arr.append(maze_element(5))
maze.append(arr)
#11번째
arr=[]                 #1 2 4 8
arr.append(maze_element(3))
arr.append(maze_element(12))
arr.append(maze_element(5))
arr.append(maze_element(5)) 
arr.append(maze_element(5))
arr.append(maze_element(7))
arr.append(maze_element(10))
arr.append(maze_element(9))
arr.append(maze_element(5))
maze.append(arr)
#12번째
arr=[]                 #1 2 4 8
arr.append(maze_element(2))
arr.append(maze_element(9))
arr.append(maze_element(3))
arr.append(maze_element(9)) 
arr.append(maze_element(3))
arr.append(maze_element(9))
arr.append(maze_element(2))
arr.append(maze_element(10))
arr.append(maze_element(9))
maze.append(arr)
#arr, maze 이미 쓰고있는 변수
possible_road=[]
possible_stack=[]
result=[0]
row,col=0,0
data=Stack()
stackhistory=[]
count=0
flag=0
while(1):
    """
    사실 처음 갈림길이 threeway()인경우도 있지만, 이 정도는 미로를 보고 판단 할 수 있다고 생각하고 코드를 작성 했습니다.
    대신 이 사실 말고는 미로에 대한 모든정보를 도착지 빼고는 모른다는 가정하에 코드를 작성했습니다. 
    """
    if flag==1: #flag==1 이면 종료해도 된다는 것인데 이 상황은 오직 처음 갈림길에서 갈곳이 사라졌을때 올것이다
        break
    road=maze[row][col].state
    if maze[row][col].istake==1: #딱 왔더니 istake=1즉, 왔던 갈림길이면 그 전의 stack에 있던 데이터를 빼옵니다.
        popData=data.pop()
        result=result[:popData.count+1]
        row=popData.xcoord
        col=popData.ycoord
        count=popData.count
        maze[row][col].istake=0
        stackhistory.append(stack_use(1,row,col,count))
        continue
    elif maze[row][col].oneway(): #딱 왔더니 갈 수 있는길이 한개만 열려있는 곳이면
        if data.isEmpty()==True: #처음에 stack도 비어있으면 어디로갈지 정해서 글로 가야됩니다.
            for i in range(4):
                if (road&(2**i))==2**i:
                    break
            maze[row][col].istake=1
            result.append(2**i)
            row,col= go(row,col,2**i)
            count=count+1
            continue
            """
            딱 도착지점으로 왔다면(이는 oneway twoway threeway 동일) 나는 지금까지 왔던 stackhistory, 움직인 history인 result를 
            어딘가에 저장하고 이는 출발부터 끝까지 갈 수 있는 길중 하나로 추가해놓는다.
            그 후 지금까지 stack에 있으면서 가보지 않은 길들을 가봐야 하므로 하나씩 pop하며 그 동안 가지 않았던 루트들을 탐색하게 된다.
            그래서 들어 가자마자 istake=0으로 바꿔준다 그래야 나중에 좀더 pop연산을 진행 하고 난 후 이 갈림길을 지나더라도 올 수 있도록 만들어 준 것이다.
            """
        elif row==11 and col==8:
            possible_road.append(result)
            popData=data.pop()
            result=result[:popData.count+1]
            row=popData.xcoord
            col=popData.ycoord
            maze[row][col].istake=0
            count=popData.count
            possible_stack.append(copy.copy(stackhistory))
            print('finish 추가')
            continue
            """
            이 경우는 갈림길에서 어떠한 길을 선택해서 왔는데 막힌 길 인 경우이다. 이 경우 최근의 stack의 상황으로 돌아가야 한다.
            또한 istake=0으로 해야 갈림길에서 선택할 수 있게 될 것이다. 그리고 이미 간곳의 경우에는 self.up또는 right와 같은 변수가 0으로 되어있어
            다시는 안 갈 수 있도록 설계 되어 있다.
            """
        else:
            popData=data.pop()
            result=result[:popData.count+1]
            row=popData.xcoord
            col=popData.ycoord
            maze[row][col].istake=0
            count=popData.count
            stackhistory.append(stack_use(1,row,col,count))
    elif maze[row][col].twoway():
        """
        만약 스택이 비어있으면 아직 출발지점에서 갈림길을 만나지 않은 상태이다. 이 경우 난 우선 result가 처음 초기화할때 저장해둔 0을 제외하고 원소가 있는지 확인을 한다.
        만약 있으면 아직 갈림길을 만나지 않고 몇번의 움직임이 있는 상태이므로 내가 갈 수 있는 곳은 한 곳으로 정해지는데 그 곳으로 가게 해준다.
        """
        if data.isEmpty()==True:
            if len(result)>1:
                if result[count]==1:
                    road=road-4
                elif result[count]==2:
                    road=road-8
                elif result[count]==4:
                    road=road-1
                else:
                    road=road-2
                if road&(1)==1 and  maze[row][col].isup()==True:
                    result.append(1)
                    row,col=go(row,col,1)
                    count=count+1
                elif road&(2)==2 and  maze[row][col].isright()==True:
                    result.append(2)
                    row,col=go(row,col,2)
                    count=count+1
                elif road&(4)==4 and  maze[row][col].isdown()==True:
                    result.append(4)
                    row,col=go(row,col,4)
                    count=count+1
                elif road&(8)==8 and  maze[row][col].isleft()==True:
                    result.append(8)
                    row,col=go(row,col,8)
                    count=count+1
                else:flag=1
                continue
            
            else:
                """
                사실 이 미로는 위의 경우는 나오지 않는다 왜냐하면 처음부터 갈림길이 나눠지기 때문이다. 그래서 이 코드에만 집중했다. 만약 미로가 바뀔 수 있다는
                가정이 있었다면 위의 코드를 아래코드처럼 바꿨겠지만 처음 시작의 상황정도는 내가 판단한다고 가정을 했다. (바꿀 수는 있지만 실행도 안될 코드에는 적당한 
                논리만 skatch 해놨습니다.)
                처음 갈림길이 생길 것이므로 stackhistory를 초기화 시켰다. 이쪽에서부터 stack 새로 시작할 수 있도록 말이다.
                또한 0,0에서 갈 수 있는 길은 오른쪽 or 아래이다. 그래서 둘 중에 갈 수 있는곳이 있는지 조사했고 그 곳으로 갈 수 있도록 하였다. 다만 
                둘 다 갈 수 없는 경우 경로탐색을 끝냈다 판단을 하고 flag=1을 넣고, 다음 무한루프 안에서 빠져 나갈 수 있도록 하였다.
                """
                stackhistory=[]
                if (road&2)==2 and maze[row][col].isright()==True:
                        maze[row][col].right=0
                        data.push(stack_data(row,col,count))
                        stackhistory.append(stack_use(0,row,col,count))
                        maze[row][col].istake=1
                        result.append(2)
                        row,col= go(row,col,2)
                        count=count+1
                        continue
                elif (road&4)==4 and maze[row][col].isdown()==True: 
                        maze[row][col].down=0
                        data.push(stack_data(row,col,count))
                        stackhistory.append(stack_use(0,row,col,count))
                        maze[row][col].istake=1
                        result.append(4)
                        row,col= go(row,col,4)
                        count=count+1
                        continue
                else:
                    flag=1
            
        elif row==11 and col==8:
            """
            도착한 경우에는 몇방향으로 뚫려있는지가 중요하지 않다. oneway와 같다.
            """
            possible_road.append(result)
            popData=data.pop()
            result=result[:popData.count+1]
            row=popData.xcoord
            col=popData.ycoord
            maze[row][col].istake=0
            count=popData.count
            possible_stack.append(copy.copy(stackhistory))
            
            print('finish 추가')
            continue
        else:
            """
            이 경우가 일반적인 2way인경우이다. 그저 들어온곳으로 부터 다른곳으로 가면 된다. 그 방법은 result에서 최근 원소를 빼와서 
            어떠한 방향으로 부터 왔는지 판단하고 1 2 4 8과 비트연산을 하여 다음 위치를 계산했다.
            """
            if result[count]==1:
                road=road-4
            elif result[count]==2:
                road=road-8
            elif result[count]==4:
                road=road-1
            else:
                road=road-2
            for i in range(4):
                if (road&(2**i))==2**i:
                    break
            result.append(2**i)
            row,col=go(row,col,2**i)
            count=count+1
            continue
    elif maze[row][col].threeway():
        """
        3가지 방향이 있다면 이 것은 갈림 길이다. 그 중 도착한경우는 이전과 동일
        """
        if row==11 and col==8:
            possible_road.append(result)
            popData=data.pop()
            result=result[:popData.count+1]
            row=popData.xcoord
            col=popData.ycoord
            maze[row][col].istake=0
            count=popData.count
            possible_stack.append(copy.copy(stackhistory))
            print('finish 추가')
            continue
            """
            이제 진짜 본격적인 생각이 필요하다. 우선 지금 위치의 state와 위아래, 양옆과 비트연산들을 할 것인데 그것 뿐만아니라 이미 그 전에 갈림길에 와서 가봤던 방향이 아닌지 확인을
            해야 하고 또한 가고자 하는 방향이 이 갈림길을 오기위한 그 전의 위치인지 확인을 해야 그쪽으로 갈 수 있게 하였다.(3단확인) 
            """
        elif (road&1)==1 and result[count]!=4 and maze[row][col].isup()==True:
                maze[row][col].up=0
                maze[row][col].istake=1
                data.push(stack_data(row,col,count))
                stackhistory.append(stack_use(0,row,col,count))
                row,col=go(row,col,1)
                result.append(1)
                count=count+1
        elif (road&2)==2 and result[count]!=8 and maze[row][col].isright()==True:
                maze[row][col].right=0
                maze[row][col].istake=1
                data.push(stack_data(row,col,count))
                stackhistory.append(stack_use(0,row,col,count))
                row,col=go(row,col,2)
                result.append(2)
                count=count+1
        elif (road&4)==4 and result[count]!=1 and maze[row][col].isdown()==True:
                maze[row][col].down=0
                maze[row][col].istake=1
                data.push(stack_data(row,col,count))
                stackhistory.append(stack_use(0,row,col,count))
                row,col=go(row,col,4)
                result.append(4)
                count=count+1 
        elif (road&8)==8 and result[count]!=2 and maze[row][col].isleft()==True:
                maze[row][col].left=0
                maze[row][col].istake=1
                data.push(stack_data(row,col,count))
                stackhistory.append(stack_use(0,row,col,count))
                row,col=go(row,col,8)
                result.append(8)
                count=count+1
        else:
            """
            위의 모든경우가 안되는 3way인경우 그 위치에서 이미 모든 갈림길의 경로를 가본 상태 일 것이다. 그러므로 이 갈림길로는 못간다하고 stack에 있는 data를 뽑아다
            그 전의 좌표에 가야 한다.
            """
            maze[row][col].up=1
            maze[row][col].right=1
            maze[row][col].down=1
            maze[row][col].left=1
            popData=data.pop()
            result=result[:popData.count+1]
            row=popData.xcoord
            col=popData.ycoord
            maze[row][col].istake=0
            count=popData.count
            stackhistory.append(stack_use(1,row,col,count))
    else:
        print('미로 오류')
        break
#result에 있는 필요없는 첫번째원소 0제거한다.
for i in range(len(possible_road)):
    possible_road[i]=possible_road[i][1:]
#stack의 활용 횟수 및 어떠한 stack의 형태를 사용했는지 출력
for i in range(len(possible_stack)):
    for j in range(len(possible_stack[i])):
        print(possible_stack[i][j])
    print('스택 활용 횟수 %d 회' %j)

print('모두 %d개의 길을 찾았습니다.'%len(possible_road))
print('가장 짧은 길을 표시합니다.')
#길이가 최소가되는것 찾기위하여
idx=0
minimum=len(possible_road[0])
for i in range(1,len(possible_road)):
    if len(possible_road[i])<minimum:
        minimum=len(possible_road[i])
        idx=i
possible_road=possible_road[idx]
print('거리 (%d)'%(minimum))

row,col=0,0
#각각의 위치에 [x,y]형태로 들어가 있어 경로가 되는 곳이면...
dis=[[row,col]]
miz=[]
for i in range(len(possible_road)):
    if possible_road[i]==1:
        row=row-1
        miz.append(row)
        miz.append(col)
        dis.append(miz)
        miz=[]
    elif possible_road[i]==2:
        col=col+1
        miz.append(row)
        miz.append(col)
        dis.append(miz)
        miz=[]
    elif possible_road[i]==4:
        row=row+1
        miz.append(row)
        miz.append(col)
        dis.append(miz)
        miz=[]
    else:
        col=col-1
        miz.append(row)
        miz.append(col)
        dis.append(miz)
        miz=[]
for i in range(len(dis)):
    print(' (%d, %d)-> ' %(dis[i][0],dis[i][1]),end='')
#아름다운 출력을 위해서 여러 출력들을 하며 최적화 시켰습니다. 이 부분은 설명보다는 그저 시행착오 끝에 성공한 것이기에 설명은 안하도록 하겠습니다.
print('')
print('* ',end='')
print('* * * '*9,end='')
print('*')
for i in range(12):
    print('* ',end='')
    for j in range(8):
        if [i,j] in dis:
            print('  O  ',end='')
        else :
            print('     ',end='')
        if maze[i][j].state&2==0 :
            print('|',end='')
        else:
            print(' ',end='')
    if [i,8] in dis:
        print('   O  ',end='')
    else:
        print('      ',end='')
    print('*')
    print('* ',end='')    
    for j in range(9):
        
        if maze[i][j].state&4==0 :
            print('------',end='')
        else:
            print('      ',end='')
    print('*')        
