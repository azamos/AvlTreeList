#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1 # Balance factor
		self.rank = 0
		self.size = 1
		self.isReal = True

	def setToVirtual(self):
		self.isReal = False


	def isLeft():
		return self.right is None and self.left is None
	def isRealNode(self):
		return self.isReal

	def isLeftSon(self):
		return  True if self.parent.left is self else False

	def isRightSon(self):
		return not self.isLeftSon()

	def updateRank(self):
		newRank = -100
		parentRank = self.parent.rank
		if self.isLeftSon():
			newRank = parentRank -1 -self.right.size
		elif self.isRightSon():
			newRank = parentRank +1 +self.left.size
		self.rank = newRank
	""""
		TODO: make sure doesnt cause stack overflow due to improper recursive calls
	"""
	def calculateHeight(self):
		l = 0 if self.left is None else self.lef.getHeight()
		r = 0 if self.right is None else self.right.getHeight()
		return = 1 + max(l,r)
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
	""""
		Note to self: when calling this method, pass node.calculateHeight() as the arg.
	"""

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return not self.value is None

"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		# add your fields here
		self.minKeyNode = None
		self.maxKeyNode = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.root is None

	def isValidIndex(self,index):
		return False if index < 0 or index > self.size-1 else True

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

	""""
		TODO: TEST
	"""
	def retrieve(self, i):
		if self.isValidIndex(i):
			return None
		p = self.root
		while i>=0:
			if p.rank == i+1:
				return p
			elif p.rank > i:
				p = p.getLeft()
			elif p.rank < i:
				p = p.getRight()
			i = i - p.rank
		return p

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	

	""""
			TODO: TEST
	"""
	def insert(self, i, val):
		newNode = AVLNode(val)
		
		leftVirtualKid = AVLNode(None)
		leftVirtualKid.setToVirtual()
		leftVirtualKid.setParent(newNode)
		
		rightVirtualKid = AVLNode(None)
		rightVirtualKid.setToVirtual()
		rightVirtualKid.setParent(newNode)
		
		newNode.setLeft(leftVirtualKid)
		newNode.setRight(rightVirtualKid)
		
		newParent = self.traverseTo(i)

	def traverseTo(self,index):
		traverser = self.root
		while traverser.isRealNode():
			if traverser.rank == index:
				insertLocal = traverser.getParent()
			if traverser.rank > index:
				traverser = traverser.getLeft()
			elif traverser.rank < index:
				traverser = traverser.getRight()
		return traverser

	def rotateLeft(self, criminalNode):
		rightSonOfCriminal = criminalNode.right
		newRightSonOfProblemNode = rightSonOfCriminal.left
		parent = criminalNode.parent
		if criminalNode is parent.right:
			parent.right = rightSonOfCriminal
		elif criminalNode is parent.left:
			parent.left = rightSonOfCriminal
		criminalNode.parent = rightSonOfCriminal
		rightSonOfCriminal.parent = parent
		newRightOfCriminal = rightSonOfCriminal.left
		rightSonOfCriminal.left = criminalNode
		criminalNode.right = newRightOfCriminal




	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

	""""
			TODO: TEST
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.minKeyNode

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.maxKeyNode

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		if self.empty():
			return None
		n = self.size
		arr = [None] * n
		arr[0] = self.first()
		arr[n-1] = self.last()
		for i in range(1,n-1):
			valAtIndexi = self.retrieve(i)
			arr[i] = valAtIndexi
		return arr

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		arr = self.listToArray()
		for node in arr:
			if node.value == val:
				return node.tank-1
		return -1



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root


