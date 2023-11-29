
inf = float('inf')

class Node:
    def __init__(self, val, children=[], g = None, f = None):
        self.val = val
        self.children = children
        self.f = g
        self.g = g

def max_path(root):
    def f(root):
        if root.children == []:
            root.f = root.val
        else:
            n = len(root.children)
            max_value = -inf
            for i in range (n):
                if root.children[i].f == None:
                    f(root.children[i])
                root.children[i].f
                if root.children[i].f > max_value:
                    max_value = root.children[i].f
                if max_value < 0:
                    max_value = 0
            root.f = root.val + max_value
    
    def g(root):
        n = len(root.children)
        if root.children == []:
            root.g == root.val
        elif n == 1:
            root.g = root.children[0].f + root.val
        else:
            max1_g = 0
            max2_g = 0
            for i in range (n):
                if root.children[i].f > max1_g:
                    max2_g = max1_g
                    max1_g = root.children[i].f
                elif root.children[i].f > max2_g:
                    max2_g = root.children[i].f
            root.g = root.val + max1_g + max2_g
    
    max_g = -inf

    def search_max(root):
        nonlocal max_g
        if root.g > max_g:
            max_g = root.g
        elif root.children == []:
            return
        else:
            for child in root.children:
                search_max(child)

    f(root)
    g(root)
    search_max(root)
    
    return max_g
    

root = Node(20, [
    Node(5, [
        Node(30), 
        Node(-20)
    ]), 
    Node(-20, [
        Node(1, [
            Node(30), 
            Node(22),
            Node(-15)
        ]), 
    ]), 
    Node(15),
    Node(-10, [
        Node(18),
        Node(23),
        Node(-20, [
            Node(100)
        ]),
        Node(-15)
    ])
])

print(max_path(root))

