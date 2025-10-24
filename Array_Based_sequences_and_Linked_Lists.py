#Thomas Cubstead
#Algorithm_Runtime_Project
#linked_List_Project
#10/23/25
#this program uses the build_list_forward and tests different methods of a singly linked list

#Node class for singly linked list
def test_forward_list():
    print("---- Build a forward list ----")
    ll = SinglyLinkedList()
    ll.build_forward_list([10, 20, 30, 40, 50])
    ll.display()
    
    print("Delete the first node:")
    ll.remove(10)
    ll.display()
    
    print("Delete the last node:")
    ll.remove(50)
    ll.display()
    
    print("Delete the interior node:")
    ll.remove(30)
    ll.display()

#tests build_list_backward
def test_backward_list():
    print("\n---- Build a backward list ----")
    ll = SinglyLinkedList()
    ll.build_backward_list([10, 20, 30, 40, 50])
    ll.display()
    
    print("Delete the first node:")
    ll.remove(50)
    ll.display()
    
    print("Delete the last node:")
    ll.remove(10)
    ll.display()
    
    print("Delete the interior node:")
    ll.remove(30)
    ll.display()

#tests non-recursive reverse display
def test_reverse_display():
    """Test non-recursive reverse display"""
    print("\n---- Non-recursive reverse print test----")
    ll = SinglyLinkedList()
    ll.build_forward_list([10, 20, 30, 40, 50])
    
    print("Insertion order:")
    ll.display()
    
    print("Reverse order (recursive):")
    ll.display_reverse()
    
    print("Reverse order (non-recursive):")
    ll.display_reverse_nr()

#removes functions
def test_remove_all():
    print("\n---- Remove all test ----")
    ll = SinglyLinkedList()
    ll.build_forward_list([1, 2, 4, 6, 1, 3, 6])
    ll.display()
    
    print("Removing 1 and all duplicates:")
    ll.remove_all(1)
    ll.display()
    
    print("Removing 6 and all duplicates:")
    ll.remove_all(6)
    ll.display()

#output
def main():
    test_forward_list()
    test_backward_list()
    test_reverse_display()
    test_remove_all()


if __name__ == "__main__":
    main()