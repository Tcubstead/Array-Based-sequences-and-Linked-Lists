#Thomas Cubstead
#Algorithm_Runtime_Project
#linked_List_Project
#10/23/25
#this program uses the build_list_forward and tests different methods of a singly linked list

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
