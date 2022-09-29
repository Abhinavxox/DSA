package Easy;

public class MergeTwoSortedLists {
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

    ListNode toReturn;

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode pointer1 = list1, pointer2 = list2;

        while (pointer1.next != null || pointer2 != null) {
            if (pointer1.val <= pointer2.val) {
                creation(pointer1.val);
                pointer1 = pointer1.next;
            } else {
                creation(pointer2.val);
                pointer2 = pointer2.next;
            }
        }

        if (pointer1 == null && pointer2 != null) {
            while (pointer2 != null) {
                creation(pointer2.val);
                pointer2 = pointer2.next;
            }

        } else if (pointer2 == null && pointer1 != null) {
            while (pointer1 != null) {
                creation(pointer1.val);
                pointer1 = pointer1.next;
            }
        } else if (pointer1 == null && pointer2 == null) {
            return toReturn;
        }
        return toReturn;
    }

    public void creation(int val) {
        ListNode pointer = toReturn;
        if (pointer == null) {
            pointer.val = val;
            return;

        }
        while (pointer.next != null) {
            pointer = pointer.next;
        }
        pointer.next.val = val;
    }
}
