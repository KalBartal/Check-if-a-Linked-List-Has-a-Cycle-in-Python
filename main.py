# define a Node class
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


# define a has_cycle function
def has_cycle(head):
    # base case if linked list is empty
    if not head:
        return False

    # set 'slow' and 'fast' pointers
    slow, fast = head, head
    while fast and fast.next:
        # increment the 'slow' pointer
        slow = slow.next
        # increment the 'fast' pointer twice
        fast = fast.next.next
        # check if 'slow' and 'fast' meet
        if slow is fast:
            return True
            # if the loop is completed without interruption, return False
    return False


# set up some test cases
# case1: cycle exists - fast pointer should catch up to slow pointer
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

result1 = has_cycle(node1)
print(result1)  # True

# case2: no cycle - fast pointer should reach the end
node5 = ListNode(5)
node6 = ListNode(6)

node5.next = node6

result2 = has_cycle(node5)
print(result2)  # False