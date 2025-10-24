#Thomas Cubstead
#Algorithm_Runtime_Project
#Split_Evens_Odds
#10/23/25
#this program splits a linked list into two lists one with even integers and the other with odd integers


from linked_List_Project import Node, SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    
    def split(self):

        evens_list = SinglyLinkedList()
        odds_list = SinglyLinkedList()
        

        current = self._SinglyLinkedList__head
        
        evens_tail = None
        odds_tail = None
        
        while current is not None:
            # Save the next node before we modify current.next
            next_node = current.next
            
            # Disconnect current node from the original list
            current.next = None
            
            # Check if even or odd and add to appropriate list
            if current.data % 2 == 0:

                if evens_list._SinglyLinkedList__head is None:

                    evens_list._SinglyLinkedList__head = current
                    evens_tail = current
                else:
                    # Append to evens list
                    evens_tail.next = current
                    evens_tail = current
                
                evens_list._SinglyLinkedList__tail = evens_tail
                evens_list._SinglyLinkedList__count += 1
            else:
                # Add to odds list
                if odds_list._SinglyLinkedList__head is None:

                    odds_list._SinglyLinkedList__head = current
                    odds_tail = current
                else:
                    # Append to odds list
                    odds_tail.next = current
                    odds_tail = current
                
                odds_list._SinglyLinkedList__tail = odds_tail
                odds_list._SinglyLinkedList__count += 1
            
            # Move to next node in original list
            current = next_node
        
        # Clear the original list
        self._SinglyLinkedList__head = None
        self._SinglyLinkedList__tail = None
        self._SinglyLinkedList__count = 0
        
        return evens_list, odds_list

def test_split_evens_odds():
    
    # Create original list
    original = SplitEvensOdds()
    original.build_forward_list([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])
    
    print("Original list:")
    original.display()
    
    # Split the list
    evens, odds = original.split()
    
    print("\nEvens list:")
    evens.display()
    
    print("\nOdds list:")
    odds.display()
    
    print("\nOriginal list after split:")
    original.display()


def test_additional_cases():
    
    print("\n" + "="*60)
    print("Additional Test Cases")
    print("="*60)
    
    # Test 1: All evens
    print("\nTest 1: All even numbers")
    list1 = SplitEvensOdds()
    list1.build_forward_list([2, 4, 6, 8, 10])
    print("Original:")
    list1.display()
    evens, odds = list1.split()
    print("Evens:")
    evens.display()
    print("Odds:")
    odds.display()
    
    # Test 2: All odds
    print("\nTest 2: All odd numbers")
    list2 = SplitEvensOdds()
    list2.build_forward_list([1, 3, 5, 7, 9])
    print("Original:")
    list2.display()
    evens, odds = list2.split()
    print("Evens:")
    evens.display()
    print("Odds:")
    odds.display()
    
    # Test 3: Single element (even)
    print("\nTest 3: Single even element")
    list3 = SplitEvensOdds()
    list3.build_forward_list([4])
    print("Original:")
    list3.display()
    evens, odds = list3.split()
    print("Evens:")
    evens.display()
    print("Odds:")
    odds.display()
    
    # Test 4: Single element (odd)
    print("\nTest 4: Single odd element")
    list4 = SplitEvensOdds()
    list4.build_forward_list([5])
    print("Original:")
    list4.display()
    evens, odds = list4.split()
    print("Evens:")
    evens.display()
    print("Odds:")
    odds.display()
    
    # Test 5: Empty list
    print("\nTest 5: Empty list")
    list5 = SplitEvensOdds()
    print("Original:")
    list5.display()
    evens, odds = list5.split()
    print("Evens:")
    evens.display()
    print("Odds:")
    odds.display()

#run main function to execute tests
def main():

    test_split_evens_odds()
    test_additional_cases()


if __name__ == "__main__":
    main()