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
#in_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
#post_order = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.data = value
'''
# logical error
def make_tree(node, left, right):
	print(left, right)
	data = post_order[right]
	node = Node(data)
	if left == right:
		return
	rooti = in_order.index(data)
	make_tree(node.left, left, rooti - 1)
	make_tree(node.right, rooti, right -1)
'''

'''
# can't change argument node
def make_tree(node, in_order, post_order):
    print(in_order, post_order)
    data = post_order[-1]
    node = Node(data)
    if len(post_order) > 1:
        rooti = in_order.index(data)
        if rooti != 0:
            make_tree(node.left, in_order[:rooti], post_order[:rooti])
        if rooti != len(in_order) - 1:
            make_tree(node.right, in_order[rooti + 1:], post_order[rooti:-1])
'''

def make_tree(in_order, post_order):
    if not in_order:
        return
    root = Node(post_order[-1])
    rootPos = in_order.index(post_order[-1])
    root.left = make_tree(in_order[ : rootPos], post_order[ : rootPos])
    root.right = make_tree(in_order[rootPos + 1 : ], post_order[rootPos : -1])
    return root
    
def show_tree(root):
	if root is None:
		return
	show_tree(root.left)
	print(root.data, end = ' ')
	show_tree(root.right)

def find_deepest_path(tree):
    #show_tree(tree)
    #print()
    if not tree:
        return
    path = [tree.data]
    left_path = find_deepest_path(tree.left)
    right_path = find_deepest_path(tree.right)
    if (not left_path) and (right_path):
        path.extend(right_path)
    elif (left_path) and (not right_path):
        path.extend(left_path)
    elif (left_path) and (right_path):
        if len(left_path) > len(right_path):
            path.extend(left_path)
        else:
            path.extend(right_path)
    return path

#tree = Node(post_order[-1])
#make_tree(tree, 0, len(post_order) -1)
#make_tree(tree, in_order, post_order)
tree = make_tree(in_order, post_order)
show_tree(tree)
deepest_path = find_deepest_path(tree)
print("".join(deepest_path)) # zWp8LGn01wxJ7

'''
echo "U2FsdGVkX1+gxunKbemS2193vhGGQ1Y8pc5gPegMAcg=" | openssl enc -aes-128-cbc -a -d -pass pass:"zWp8LGn01wxJ7"
nqueens
'''
