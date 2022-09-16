while l1_s or l2_s or carry:
we also need to add carry in while loop to handle case where we have carry left in last
```python3
carry,head = 0,None
while l1_s or l2_s or carry:
n1 = l1_s.pop().val if l1_s  else 0
n2 = l2_s.pop().val if l2_s  else 0
carry,q = divmod(n1+n2+carry,10)
head = ListNode(q,head) # nice trick
return head
```
one more solution