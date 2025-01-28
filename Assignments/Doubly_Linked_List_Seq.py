class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        '''node = self.head
        while node:
            yield node.item
            node = node.next'''
        if self.head is not None:
            yield self.head.item
            node = self.head.next
        else:
            return None
        while node is not self.head:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        x = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = x
            self.tail = x
        else:
            
            cur_head = self.head
            cur_tail = self.tail
            x.next = cur_head
            cur_head.prev = x
            x.prev = self.tail
            cur_tail.next = x
            self.head = x

    def insert_last(self, x):
        x = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = x
            self.tail = x
        else:
            cur_head = self.head
            cur_tail = self.tail
            x.prev = cur_tail
            cur_tail.next = x
            x.next = self.head
            cur_head.prev = x
            self.tail = x

    def delete_first(self):
        if self.head is None:
            return
        else:
            cur_head = self.head
        
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            
        else:
            second_node = cur_head.next
            second_node.prev = self.tail
            self.head = second_node

        del(cur_head)
            
    def delete_last(self):
        if self.tail is None:
            return
        else:
            cur_tail = self.tail
        
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            
        else:
            second_last_node = cur_tail.prev
            second_last_node.next = self.head
            self.tail = second_last_node

        del(cur_tail)

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        
        left_elem = x1.prev
        right_elem = x2.next
        left_elem.next = right_elem
        right_elem.prev = left_elem
        
        L2.head = x1
        L2.tail = x2
        
        x1.prev = L2.tail
        x2.next = L2.head

        if self.head == x1 and self.tail == x2:
            self.head = None
            self.tail = None
        elif self.head == x1:
            self.head = right_elem
        elif self.tail == x2:
            self.tail = left_elem
        
        
        return L2

    def splice(self, x, L2):
        if self.head is None:
            self.head = L2.head
            self.tail = L2.tail
            return
        if L2.head is None:
            return
        head_node = L2.head
        tail_node = L2.tail
        tail_node.next = x.next
        x.next = head_node
        head_node.prev = x
        self.tail = tail_node
        L2.head = None
        L2.tail = None
        #need to deal with what happens when inserting after tail


tst = Doubly_Linked_List_Seq()

tst.insert_first(5)
#tst.insert_first(4)
#tst.insert_first(3)
#tst.insert_first(2)
#tst.insert_first(1)

L2 = Doubly_Linked_List_Seq()
L2.insert_first(7)
L2.insert_first(6)
tst.splice(tst.head, L2)
print(tst.__str__())
#print(tst.remove(tst.head.next, tst.tail))
#print(tst.__str__())