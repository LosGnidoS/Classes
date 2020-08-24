#!usr/bun/python3
#GITHUB ----> LosGnidoS

'''LINKEDLIST'''

class Node:
	def __init__(self,value=None, next_one=None):
		self.value = value
		self.next = next_one

class linkedList:
	def __init__(self):
		self.first = None
		self.last = None
		self.lenght = 0

	def __str__(self):
		if self.first != None:
			current = self.first
			out = 'linkedList [\n' +str(current.value) + '\n'
			while current.next != None:
				current = current.next
				out += str(current.value) + '\n'
			return out + ']'
		return 'linkedList []'

	def clear(self):
		self.__init__()

	def add(self,x):
		self.lenght +=1
		if self.first == None:
			self.first = self.last = Node(x, None)
		else:
			self.last.next = self.last = Node(x, None)


L = linkedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
print(L)