package Easy;

public class RemoveDuplicatesFromSortedList {

    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode deleteDuplicates(ListNode head) {
        int data = head.val;
        ListNode pointer = head;
        while (pointer.next != null) {
            if (pointer.next.val == data) {
                pointer.next = pointer.next.next;
            }
            pointer = pointer.next;
        }
        if (pointer.val == data && pointer.next != null) {
            pointer.next = null;
        }
        return head;
    }
}
