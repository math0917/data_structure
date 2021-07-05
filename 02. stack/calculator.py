
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
def Priority (num):
    if (num=='(') : return 1
    elif (num=='+' or num=='-'): return 3
    elif(num=='*' or num=='%'): return 5
    elif(num=='^'): return 7
    else : return -1

def WhoPreOp(op1,op2):
    pr_op1=Priority(op1)
    pr_op2=Priority(op2)
    if pr_op1>pr_op2: 
        return 1
    elif pr_op1==pr_op2:
        return 0
    else:
        return -1
def InfixToPostfix(ptr):
    flag=-1
    arr=[]
    equation=Stack()
    for i in range(len(ptr)):
        if ptr[i].isdigit():
            arr.append(ptr[i])
        else:
            arr.append('!') #숫자사이 구분   
            if ptr[i]=='(':
                if i>0 and ptr[i-1].isdigit()==True: #( 이전에 숫자면 오류 ex) 2(
                    flag=i
                elif i<len(ptr)-1 and ptr[i+1].isdigit()==False: #( 이후에 연산이 있으면 오류 ex) (+
                    flag=i+1
                else:    
                    equation.push(ptr[i])
            elif ptr[i]==')':
                if i<len(ptr)-1 and ptr[i+1].isdigit()==True:  #)이후에 끝이 아니고 다음에 바로 숫자있으면 오류 ex) )3
                    flag=i+1
                else:
                    while(1):
                        if equation.isEmpty()==True:
                            flag=i
                            break
                        popOp=equation.pop()
                        if popOp=='(':
                            break
                        arr.append(popOp)
            else:
                if i==0: #처음이 바로 연산자 ex) +1~~
                    flag=0 
                elif ptr[i-1].isdigit()==False and ptr[i-1]!='(' and ptr[i-1]!=')': # 연산이 두개연속? ex) +*
                    flag=i
                elif i==len(ptr)-1:   #마지막에 딸랑 연산자만 있는경우 ex) ~~+
                    flag=i
                else:    
                    while(equation.isEmpty()!=1 and WhoPreOp(equation.speek(),ptr[i])>=0):
                        
                        arr.append(equation.pop())
                       
                    equation.push(ptr[i])
        
        if flag>=0:
            return flag
    while(equation.isEmpty()!=1):
        if equation.speek()=='(':
            return len(ptr)
        arr.append(equation.pop())
    return arr
def EvaluatePostfix(arr):
    Calculate=Stack()
    num=[]
    for i in range(len(arr)):
        tok=arr[i]
        if tok.isdigit():
            num.append(int(tok))
        elif tok=='!': #만약 !가있으면 그동안 num에 있던 값을 int로 변환하는 과정이 필요함
            num_len=len(num)
            if num_len==0:
                continue
            else:
                integer=0
                for j in range(num_len):
                    integer+=num[j]*10**(num_len-1-j)
                num=[]    
            Calculate.push(integer) #최종적으로 변환된 값을 stack에 푸쉬
        else:
            if len(num)>0:
                num_len=len(num)
                integer=0
                for j in range(num_len):
                    integer+=num[j]*10**(num_len-1-j)
                num=[]  
                Calculate.push(integer)
            op1=Calculate.pop()
            op2=Calculate.pop()
            if tok=='+':
                Calculate.push(op2+op1)
            elif tok=='-':
                Calculate.push(op2-op1)
            elif tok=='*':
                Calculate.push(op2*op1)
            elif tok=='%':
                Calculate.push(op2%op1)
            elif tok=='^':
                Calculate.push(op2**op1)
    return Calculate.pop()


while(1):
    arr=input('')
    arr=InfixToPostfix(arr)
    
    if (type(arr) == int):
        print(' '*arr+'^이 위치에 오류가 있습니다.')
    else:
        print('=',EvaluatePostfix(arr))
