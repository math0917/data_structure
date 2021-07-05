import time
MAX_QSIZE = 20
class Queue :
    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self) : 
        return self.front == self.rear
    def isFull(self) : 
        return self.front == (self.rear + 1) % MAX_QSIZE
    def clear(self) : 
        self.front = self.rear
    def enqueue(self, item):
        if not self.isFull() :
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty() :
            return self.items[(self.front + 1) % MAX_QSIZE]
    def display(self):
        out = []
        if self.front <= self.rear :
            out = self.items[self.front+1:self.rear+1]
        else :
            out = self.items[self.front +1:MAX_QSIZE] + self.items[0:self.rear+1]
        return out
def next_index(index):
    if index==25:
        return 0
    else:
        return index+1
system=Queue()
print('시스템이 시작됩니다')  
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
index=0     
while(1):
    start=time.time()
    num=int(input(''))
    end=time.time() #걸린시간을 조사하는 것 time 모듈에 포함되어있다.
    wait_time=int(end-start)
    print('%d초 경과'%(wait_time))
    for i in range(wait_time):
        """
        걸린 시간 만큼 data를 stack에 넣어 둘건데 그것은 걸린 시간만큼 for문을 돌리면 가능했고 가득차면
        넣기 실패했다고 나타내주기만 하면 됐다.
        """
        if system.isFull()==False:
            system.enqueue(alphabet[index])
            print('(SYSTEM) ADDQUEUE (%s)  F=%d R=%d' %(alphabet[index], system.front,system.rear))
            index=next_index(index)
        else:
            print('(SYSTEM) ADDQUE () FAIL. QueueFull')
            break
    if num:
        """
        만약 빼야될 데이터의 갯수가 0보다 크면 이 if문을 실행하는데 빼야할 데이터의 갯수만큼 for문을 돌며 빼는데
        우선 peek로 그 stack안에 원소가 있는지 확인 하도록 했다. (이는 stack의 class에 추가한 메서드이다.)
        그리고 그 뺀 데이터를 결과로 출력시켜줘야 하므로 따로 저장해 주었다.
        """
        arr=[]
        for i in range(num):
            if system.peek()!=None:
                data=system.dequeue()
                arr.append(data)
                print('DELETEQUEUE( ) = %s,  F=%d R=%d' %(data,system.front,system.rear))
            else:
                print('DELETEQUEUE( ) FAIL. QueueEmpty')
                break
        print('RESULT = ',end='')
        for i in range(len(arr)):
            print('%s' %arr[i],end='')
        print('')
    """
    최종 결과를 display해줘야 했고 이는 front와 rear의 대소비교를 통해 출력방법을 달리 해줘야 했다. 
    """
    print('QUEUE = ',end='')
    out=system.display()
    for i in range(len(out)):
        print('%s'%(out[i]),end='')
    if system.rear>=system.front:
        print('(%d)'% (system.rear-system.front))
    else:
        print('(%d)'%(MAX_QSIZE-(system.front-system.rear)))
        
    
