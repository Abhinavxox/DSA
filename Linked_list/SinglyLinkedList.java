package Linked_list;

public class SinglyLinkedList {
	
	public static void main(String[] args) {
		SinglyLinkedList slist = new SinglyLinkedList();
		slist.creation(1);
		slist.creation(2);
//		slist.insertAtBeginning(12);
//		slist.insertAtLast(11);
//		slist.insertAtMiddle(5, 2);
////		slist.deletionAtBeginning();
//		slist.deletionAtEnd();
////		slist.deletionAtMiddle(3);
//		slist.searching(2);
		slist.creation(3);
		slist.creation(4);
		slist.creation(5);
		slist.creation(3);
		slist.insertAtMiddle(0, 0);
		slist.print();
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
	
	public void print() {
		Node pointer = head;
		while(pointer.next != null) {
			System.out.println(pointer.data);
			pointer = pointer.next;
		}
		System.out.println(pointer.data);
		
	}
	
	public void insertAtBeginning(int data) {
		Node newNode = new Node(data);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
			newNode.next = head;
			head = newNode;
	}
	
	public void insertAtLast(int data) {
		Node newNode = new Node(data);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
			tail.next = newNode;
			tail = newNode;
	}
	
	public void insertAtMiddle(int data, int position) {
		if(position == 0) {
			this.insertAtBeginning(data);
		}
		else {
		Node newNode = new Node(data);
		Node pointer = head;
		Node temp = head;
		int p = 0;
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
			while(pointer.next != null) {
				if(p == position-1) {
					temp =pointer.next;
					pointer.next = newNode;
					newNode.next = temp;
				}
				
				p++;
				pointer = pointer.next;
			}
		}
	}
	
	public void deletionAtBeginning() {
		Node temp = head;
		Node temp2 = head;
		//check if list is empty
		if(head == null) {
			System.out.println("List is empty");
		}
		
		temp2 = temp.next;
		head = temp2;
		
	}
	
	public void deletionAtEnd() {
		//check if list is empty
		if(head == null) {
			System.out.println("List is empty");
		}
		Node pointer = head;
		while(pointer.next!= tail) {
			pointer = pointer.next;
		}
		tail = pointer;
		tail.next = null;
	}
	
	public void deletionAtMiddle(int position) {
		if(position == 0) {
			this.deletionAtBeginning();
		}
		else {
			Node pointer = head;
			//check if list is empty
			if(head == null) {
				System.out.println("List is empty");
			}
			else {
				int p = 0;
				while(pointer.next!=null) {
						if(p == position-1) {
							pointer.next = pointer.next.next;
							break;
						}
					pointer = pointer.next;
					p++;
				
					}
				}
		}

	}
	
	public void searching(int data) {
		int index = 0;
		if(head == null) {
			System.out.println("List is empty");
		}
		Node pointer = head;
		int p = 0;
		while(pointer.next != null) {
			if(pointer.data == data) {
				index = p;
				break;
			}
			pointer = pointer.next;
			p++;
		}
		System.out.println("Index of the given data in list is "+index);
	}
	
}