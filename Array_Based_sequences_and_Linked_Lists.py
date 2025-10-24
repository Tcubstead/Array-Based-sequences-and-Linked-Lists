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
