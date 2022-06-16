package Linked_list;

public class DoublyLinkedList {
	
	public static void main(String[] args) {
		DoublyLinkedList dlist = new DoublyLinkedList();
		dlist.creation(1);
		dlist.creation(2);
		dlist.creation(3);
		dlist.creation(4);
		dlist.insertionAtBeginning(12);
		dlist.insertionAtLast(11);
		dlist.insertAtMiddle(10, 2);
//		dlist.deletionAtBeginning();
		dlist.deletionAtMiddle(2);
		dlist.searching(2);
		dlist.print();
	}
	
	class Node{
		int data;
		Node next;
		Node previous;
		Node(int data){
			this.data = data;
			this.previous = null;
			this.next = null;
		}
	}
	
	public Node head = null;
	public Node tail = null;
	
	public void creation(int data) {
		Node newNode = new Node(data);
		Node temp = head;
		//if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
		temp = tail.next;
		tail.next = newNode;
		newNode.previous = temp;
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
	
	public void insertionAtBeginning(int data) {
		Node newNode = new Node(data);
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
		newNode.next = head;
		head.previous = newNode;
		head = newNode;
	}
	
	public void insertionAtLast(int data) {
		Node newNode = new Node(data);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
			newNode.previous = tail;
			tail.next = newNode;
			tail = newNode;
	}
	
	public void insertAtMiddle(int data, int position) {
		if(position == 0) {
			this.insertionAtBeginning(data);
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
			while(pointer != null) {
				if(p == position-1) {
					newNode.previous = pointer;
					temp = pointer.next;
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
		//check if list is empty
		if(head == null) {
			System.out.println("List is empty");
		}
		
		temp = head.next;
		temp.previous = null;
		head = temp;
		
	}
	
	public void deletionAtEnd() {
		//check if list is empty
		if(head == null) {
			System.out.println("List is empty");
		}
		Node pointer = head;
		while(pointer != tail) {
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
							pointer.next.previous = pointer;
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
