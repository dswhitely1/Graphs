# Note: This Queue class is sub-optimal. Why?
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        new_head_node = ListNode(value);
        if not self.head and not self.tail:
            self.head = new_head_node
            self.tail = new_head_node
        else:
            new_head_node.next = self.head
            self.head.prev = new_head_node
            self.head = new_head_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        self.length += 1
        new_tail_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_tail_node
            self.tail = new_tail_node
        else:
            new_tail_node.prev = self.tail
            self.tail.next = new_tail_node
            self.tail = new_tail_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()




class Queue:
    def __init__(self):
        self.queue = DoublyLinkList()

    def __len__(self):
        return self.queue.length

    def enqueue(self, value):
        self.queue.add_to_head(value)

    def dequeue(self):
        if not self.queue.head:
            return
        return self.queue.remove_from_tail()

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = DoublyLinkList()

    def __len__(self):
        return self.stack.length

    def push(self, value):
        self.stack.add_to_head(value)

    def pop(self):
        if not self.stack.head:
            return
        return self.stack.remove_from_head()

    def size(self):
        return len(self.stack)
