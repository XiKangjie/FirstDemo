'''
in_order = ['T', 'b', 'H', 'V', 'h', '3', 'o', 'g', 'P', 'W', 'F', 'L', 'u', 'A',
			'f', 'G', 'r', 'm', '1', 'x', 'J', '7', 'w', 'e', '0', 'i', 'Q', 'Y',
			'n', 'Z', '8', 'K', 'v', 'q', 'k', '9', 'y', '5', 'C', 'N', 'B', 'D',
			'2', '4', 'U', 'l', 'c', 'p', 'I', 'E', 'M', 'a', 'j', '6', 'S', 'R',
			'O', 'X', 's', 'd', 'z', 't']
post_order = ['T', 'V', 'H', 'o', '3', 'h', 'P', 'g', 'b', 'F', 'f', 'A', 'u', 'm',
			  'r', '7', 'J', 'x', 'e', 'w', '1', 'Y', 'Q', 'i', '0', 'Z', 'n', 'G',
			  'L', 'K', 'y', '9', 'k', 'q', 'v', 'N', 'D', 'B', 'C', '5', '4', 'c',
			  'l', 'U', '2', '8', 'E', 'I', 'R', 'S', '6', 'j', 'd', 's', 'X', 'O',
			  'a', 'M', 'p', 'W', 't', 'z']
'''
in_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
post_order = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.data = value

def make_tree(node, left, right):
	print(left, right)
	data = post_order[right]
	node = Node(data)
	if left == right:
		return
	rooti = in_order.index(data)
	make_tree(tree.left, left, rooti - 1)
	make_tree(tree.right, rooti, right -1)

def show_tree(root):
	if root is None:
		return
	print(root.data)
	show_tree(root.left)
	show_tree(root.right)

tree = Node(post_order[-1])
make_tree(tree, 0, len(post_order) - 1)
show_tree(tree)

0 8
0 4
0 0
1 3
1 2
1 3
1 2
1 3
1 2
1 3
1 2
1 3
1 2