# LinkedList
# array : list , tuple , dict , set , linkedList

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# "salom",2,3,4
# node1 = Node("salom")
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4

# tmp = node1
# while tmp:
#     print(tmp.value)
#     tmp = tmp.next


# massiv = range(1,100)
#
# head = Node(0)
# tmp = head
# for i in massiv:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head
# while tmp.next:
#     if not tmp.value % 2 == 0:
#         tmp.next = tmp.next.next
#     tmp = tmp.next
#
# tmp = head.next
# while tmp.next:
#     print(tmp.value)
#     tmp = tmp.next


# massiv = range(1,111)
#
# head = Node(0)
# tmp = head
# for i in massiv:
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head
# while tmp.next.next:
#     tmp = tmp.next
# print(tmp.value)
#
#
# def create_LinkedList(array):
#     head = Node(0)
#     tmp = head
#     for i in array:
#         tmp.next = Node(i)
#         tmp = tmp.next
#     return head
#
#
# class LinkedList:
#     def __init__(self, head: Node):
#         self.head = head
#
#     def add(self, value):
#         tmp = self.head.next
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = Node(value)
#         return self.head
#
#     def print(self):
#         tmp = self.head.next
#         while tmp:
#             print(tmp.value, end=" ")
#             tmp = tmp.next
#
#     def remove(self, value):
#         tmp = self.head
#         while tmp and tmp.next:
#             if tmp.next.value == value:
#                 tmp.next = tmp.next.next
#             tmp = tmp.next
#
#         return self.head
#
#
# names = ["Akmal","Botirjon", "Akmal", "Nodir","Akmal"]
# linked_l = create_LinkedList(names)
# object = LinkedList(linked_l)
# object.print()
# object.add("Fazliddin")
# print()
# object.print()
# object.remove("Akmal")
# print()
# object.print()
#









