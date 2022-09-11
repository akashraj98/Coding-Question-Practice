Since we need last node to connect with first node and so on.
We traverse LL and  use stack to store element of linkedlist
We can use this stack to get end element using stack.pop().
Second time we have to iterate only len(stack)//2 time. ie half of the list
and after that **we can terminate linked list with node.next = none.
This should make sure that no cycle is formed**