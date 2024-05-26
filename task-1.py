# Реалізація однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Функція для реверсування однозв'язного списку
def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


# Алгоритм сортування злиттям для однозв'язного списку
def merge_sort_list(linked_list):
    if not linked_list.head or not linked_list.head.next:
        return linked_list

    def split_list(head):
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return head, slow

    def merge_lists(left, right):
        dummy = Node(0)
        tail = dummy
        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right
        return dummy.next

    def merge_sort(head):
        if not head or not head.next:
            return head
        left, right = split_list(head)
        left = merge_sort(left)
        right = merge_sort(right)
        return merge_lists(left, right)

    sorted_head = merge_sort(linked_list.head)
    linked_list.head = sorted_head
    return linked_list

# Функція для об'єднання двох відсортованих однозв'язних списків в один
def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    tail.next = current1 or current2
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Приклад використання
# Створення двох списків
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

# Друк початкових списків
print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

# Реверсування списку
reverse_list(list1)
print("Reversed List 1:")
list1.print_list()

# Сортування списку
sorted_list = merge_sort_list(list1)
print("Sorted Reversed List 1:")
sorted_list.print_list()

# Об'єднання двох відсортованих списків
merged_list = merge_two_sorted_lists(sorted_list, list2)
print("Merged Sorted Lists:")
merged_list.print_list()
