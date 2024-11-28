# STACK WITH LIST..
class stack:
    def __init__(self):
        self.elements=[]
    def isEmpty(self):
        return len(self.elements)==0
    def pop(self):
        if len(self.elements)==0:
            print("UNDERFLOW")
        else:
            x=self.elements.pop()
            return x
    def push(self,value):
        self.elements.append(value)
    def top(self):
        return self.elements[len(self.elements)-1]
    def stackImpl(self):
        x=input("PUSH OR POP?")
        if x=="pop" or x=="Pop" or x=="POP":
            self.pop()
        if x=="PUSH" or x=="Push" or x=="push":
            val=input("ENTER VALUE")
            self.push(val)
    def evaluatePost(self):
        z=input("Enter expression you want to evaluate")
        for i in range(len(z)):
            if z[i].isdigit()==True:
                self.push(z[i])
            else:
                b=self.pop()
                a=self.pop()
                res=(str(eval(a + z[i] + b))) 
                self.push(res)
        return self.pop()
    def notGreater(self, i): 
        try: 
            a = self.pre[i] 
            b = self.pre[self.top()] 
            return True if a  <= b else False
        except KeyError:  
            return False
    def In_pos(self):
        z=input("Enter Infix Expression")
        pre={'(':'0',')':'0','+':'1', '-':'1', '*':'2', '/':'2', '^':'3',}
        p=[]   
        for i in range(len(z)):
            if z[i].isdigit()==True:
                p.append(z[i])
            elif z[i]=="(":
                self.push(z[i])
            elif z[i]==")":
                while( not self.Empty() and self.top()!="("):
                    a=self.pop()
                    p.append(a)
                    if (not self.Empty() and self.top() != '('): 
                        return -1
                    else: 
                        self.pop()
            else:
                a=pre[z[i]]
                b=pre[self.pop()]
                while(not self.Empty() and self.notGreater(z[i])):
                    p.append(self.pop())
                self.push(z[i])
        while not self.Empty():
            p.append(self.pop())
            
        
                      
                      
  
                
                
##            if z[i].isdigit()==False and z[i]!="(" and z[i]!=")":
##                a=pre[z[i]]
##                b=pre[self.pop()]
##                if a>=b:
##                    p=p+self.pop()
##                else:
##                    self.push(z[i])
##            if z[i]==")":
##                c=self.pop()
##                if c!="(":
##                    p=p+c
##        return p
                    
                    
            
                
                
                
                
            
                
                
            
            
    
    
    









def fib(n):
    assert n>-1,"negative index"
    if n==0:
        return (1,0)
    (a,b)=fib(n-1)
    return (a+b,a)
    





























    

    
    

        
