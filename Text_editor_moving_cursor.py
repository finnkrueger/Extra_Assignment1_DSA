class Empty(Exception):
    pass


class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.cursor = None

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.is_empty():
            return ""
        current = self.head
        string = ""
        while current is not None:
            if current == self.cursor:
                string += "|{}|".format(current.element)
            else:
                string += current.element
            current = current.next
        return string

    def insert_after(self, node, element):
        new_node = Node(element)
        if node is None:
            self.head = new_node
            self.cursor = new_node
        else:
            new_node.next = node.next
            node.next = new_node
            self.cursor = new_node

    def delete_after(self, node):
        if node is None:
            return
        next_node = node.next
        if next_node is None:
            return
        node.next = next_node.next
        if next_node == self.cursor:
            self.cursor = node
        if self.cursor is None:
            self.cursor = self.head


class TextEditor:
    def __init__(self):
        self.text = LinkedList()

    def __str__(self):
        return str(self.text)

    def print_editor(self):
        print(self.text)
        underline = " " * self.cursor_position() + "^"
        print(underline)

    def cursor_position(self):
        current = self.text.head
        position = 0
        while current is not None and current != self.text.cursor:
            current = current.next
            position += 1
        return position

    def left(self):
        if self.text.cursor is not None and self.text.cursor != self.text.head:
            current = self.text.head
            while current.next != self.text.cursor:
                current = current.next
            self.text.cursor = current

    def right(self):
        if self.text.cursor is not None and self.text.cursor.next is not None:
            self.text.cursor = self.text.cursor.next

    def insert(self, c):
        self.text.insert_after(self.text.cursor, c)

    def delete(self):
        self.text.delete_after(self.text.cursor)
        if self.text.cursor is None:
            self.text.cursor = self.text.head


# Test the TextEditor class
editor = TextEditor()

editor.insert('H')
editor.insert('e')
editor.insert('l')
editor.insert('l')
editor.insert('o')

editor.print_editor()  
editor.right()
editor.print_editor()  
editor.right()
editor.print_editor()  
editor.right()
editor.print_editor() 
editor.right()
editor.print_editor() 
editor.left()
editor.insert('p')
editor.print_editor()  
