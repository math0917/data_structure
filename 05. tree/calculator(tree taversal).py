class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return self.__len__() == 0

MAX_QSIZE = 100
class Queue :
    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self) : return self.front == self.rear
    def isFull(self) : 
        return self.front == (self.rear + 1) % MAX_QSIZE
    def clear(self) : self.front = self.rear
    def enqueue(self, item):
        if not self.isFull() :
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        
def preorder(n):
    if n!=None:
        print(n.item, end='')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n!=None:
        inorder(n.left)
        print(n.item, end='')
        inorder(n.right)       
        
def postorder(n):
    if n!=None:
        postorder(n.left)
        postorder(n.right)
        print(n.item, end='')
def PriorityOp(n1):
    if n1 == '+' or n1 == '-':
        return 1
    else:
        return 2
def WhoIsProceOp(n1,n2):
    n1 = PriorityOp(n1)
    n2 = PriorityOp(n2)
    if n1>=n2:
        return 1
    else:
        return 0
    
def evaluate (tree):
    if tree == None : 
        return 0
    if tree.left == None and tree.right == None :
        return int(tree.item)
    else:
        op1 = evaluate(tree.left)
        op2 = evaluate(tree.right)
        if tree.item == '+' : return op1+op2
        if tree.item == '-' : return op1-op2
        if tree.item == '*' : return op1*op2
        if tree.item == '/' : return op1/op2
def levelorder(root) :
    queue = Queue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.item,end='')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
while(1):
    sentence = input('수식을 입력하세요 : ')
    stack=Stack()
    #중위 표현을 후위 표현으로 바꿀 리스트
    result=[]
    for i in sentence:
        tok = i
        if tok.isdigit():
            result.append(tok)
        else:
            if stack.isEmpty():
                stack.push(tok)
            else:
                while stack.isEmpty() == False:
                    popEl = stack.pop()
                    if WhoIsProceOp(popEl, tok):
                        result.append(popEl)
                    else:
                        stack.push(popEl)
                        break
                stack.push(tok)
                
    while stack.isEmpty() == False:
        result.append(stack.pop())
    print(result)
    #후위표기를 트리로 만들기
    for i in result:
        tok = i
        # 정수의 꼴이면 Node(tok)를 스택에 넣기
        if tok.isdigit():
            stack.push(Node(tok))
        # 연산자의 형태이면 스택의 원소 두개를 빼고 연산자와 새로운 노드를 생성후 그 노드를 스택에 push
        else:
            pop1 = stack.pop()
            pop2 = stack.pop()
            node = Node (tok, pop2, pop1)
            stack.push(node)
    tree=stack.pop()
    
    print('전위 순회 : ',end='')
    preorder(tree)
    print('')
    print('중위 순회 : ',end='')
    inorder(tree)
    print('')
    
    print('후위 순회 : ',end='')
    postorder(tree)
    print('')
    
    print('레벨 순회 : ',end='')
    levelorder(tree)
    print('')
    print('계산결과 =', evaluate(tree))

