package Linked_list;

public class QN6 {
	
	//floyd's cycle finding algo
	public static void main(String[] args) {
		QN6 obj = new QN6();
		obj.creation(1);
		obj.creation(2);
		obj.creation(3);
		obj.creation(4);
		obj.creation(4);
		obj.searchingForLoop();
	}
	
	class Node{
		int data;
		Node next;
		Node(int data){
			this.data = data;
			this.next = null;
		}
	}
	
	public Node head = null;
	public Node tail = null;
	
	public void creation(int data) {
		Node newNode = new Node(data);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
		//for last node
		//make newNodelast node
		tail.next = newNode;
		//make newNOde the tail
		tail = newNode;
	}
	
	public void searchingForLoop() {
		int index = 0;
		int max_no_of_iteration = 0;
		Node slow_flag = head, fast_flag = head;
		while(slow_flag !=null && fast_flag != null || max_no_of_iteration !=20) {
			slow_flag = slow_flag.next;
			fast_flag = fast_flag.next.next;
			max_no_of_iteration++;
			if(slow_flag == fast_flag) {
				index = 1;
				break;
			}
		}
		if(index == 1) {
			System.out.println("There is a loop");
		}
		else {
			System.out.println("There is no loop");
		}
	}

}
