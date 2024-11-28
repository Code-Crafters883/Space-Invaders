import ctypes
class Array:
 def __init__(self, size):
     assert size > 0, 'Array size must be > 0'
     self._size = size
     self._status = 0 #this gives us the number of elements entered so far
     self._elements = (ctypes.py_object * size)()
     self.clear(None)
 def __len__(self):
     return self._size
 def __getitem__(self, index):
     assert index>=0 and index<len(self),"Invalid index"
     return self._elements[index]
 def __setitem__(self, index, value):
     assert index >= 0 and index < len(self), "Invalid index"
     self._status += 1
     self._elements[index]=value
 def addatx(self,index,value):
     assert self._status<len(self),'Overflow' #we ensure we do not exceed array bounds
     assert index >= 0 and index < len(self), "Invalid index"
     if index > self._status: #we ensure elements in the array are stored contiguously
         index = self._status
     for i in range(self._status-1,index-1,-1):
         self._elements[i+1]=self._elements[i]
     self._elements[index]=value
     self._status+=1
 def delatx(self, index):
     assert self._status > 0, 'Underflow' #we ensure we do not delete a nonexistent value
     assert index >= 0 and index < len(self), "Invalid index"
     if index >= self._status:
         return
     for i in range(index,self._status - 1,1):
         self._elements[i] = self._elements[i+1]
         self._status -= 1
         self._elements[self._status]=None
 def traverse(self):
     if self._status==0:
         print("No values present")
         return
     for i in range(len(self)):
         x = self._elements[i]
         print(x, end=" ")
         print()
 def clear(self, value):
     for i in range(self._size):
         self._elements[i] = value
 def append(self,value):
     index=len(self)-1
     assert self._status<len(self),'Overflow' #we ensure we do not exceed array bounds
     assert index >= 0 and index < len(self), "Invalid index"
     if index > self._status: #we ensure elements in the array are stored contiguously
         index = self._status
     for i in range(self._status-1,index-1,-1):
         self._elements[i+1]=self._elements[i]
     self._elements[index]=value
     self._status+=1
 



         
