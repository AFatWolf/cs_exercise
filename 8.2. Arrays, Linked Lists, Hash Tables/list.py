class MYListUsingLinkedList:
    def __init__(self):
        self.link = None
        self.len = 0
    def pop(self, pos):
        prev = self
        for i in range(0, pos):
            prev = prev.link
        item = prev.link
        prev.link = item.link
        self.len -= 1
    def __str__(self):
        node = self.link
        ret = 'HEAD-->'
        while (node != None):
            ret += str(node.value) + '-->'
            node = node.link
        ret += 'TAIL'
        return ret
    def insert(self, pos, v):
        node = self
        for i in range(pos):
            node = node.link
        newNode = ListEntry(v)
        nextPos = node.link
        node.link = newNode
        newNode.link = nextPos
        self.len += 1
class ListEntry:
    def __init__(self, v):
        self.link = None
        self.value = v
head = MYListUsingLinkedList()
print(str(head))
for i in range(4):
    head.insert(0, i)
print(str(head))
head.pop(2)
print(str(head))
head.pop(2)
print(str(head))
head.pop(0)
print(str(head))


