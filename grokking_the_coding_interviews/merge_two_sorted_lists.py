class Node:
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next_node = next_node



	
def merge(l1, l2):
	dummy_head = tail = Node()

	while l1 and l2:
		if l1.data > l2.data:
			tail.next, l1 = l1, l1.next
			
		else:
			tail.next, l2 = l2, l2.next
	tail.next = l1 or l2
	return dummy_head.next
				
		



