package Linked_list;

public class CircularLinkedList {
	
	public static void main(String[] args) {
		CircularLinkedList clist = new CircularLinkedList();
		clist.creation(1);
		clist.creation(2);
		clist.creation(3);
		clist.creation(4);
		clist.insertAtMiddle(10, 2);
		clist.deletionAtBeginning();
		clist.searching(4);
		clist.print();
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
		//if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
			tail.next = head;
		}
			newNode.previous = tail;
			tail.next = newNode;
			tail = newNode;
			tail.next = head;
		
	}
	
	public void print() {
		Node pointer = head;
		do {
			System.out.println(pointer.data);
			pointer = pointer.next;
		} while (pointer != head);
		 
		
	}
	
	public void insertionAtBeginning(int data) {
		Node newNode = new Node(data);
		if(head == null) {
			head = newNode;
			tail = newNode;
			tail.next = head;
		}
		newNode.next = head;
		head.previous = newNode;
		head = newNode;
		tail.next = head;
	}
	
	public void insertionAtLast(int data) {
		Node newNode = new Node(data);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
			tail.next = head;
		}
			newNode.previous = tail;
			tail.next = newNode;
			tail = newNode;
			tail.next = head;
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
			tail.next = head;
		}
		do {
			if(p == position-1) {
				newNode.previous = pointer;
				temp = pointer.next;
				pointer.next = newNode;
				newNode.next = temp;
				tail.next = head;
			}
			
			p++;
			pointer = pointer.next;
		} while (pointer != head);
		
		}
	}
	
	public void deletionAtBeginning() {
		Node temp = head;
		//check if list is empty
		if(head == null) {
			System.out.println("List is empty");
		}
		
		temp = head.next;
		temp.previous = tail;
		head = temp;
		tail.next = head;
		
	}
	
	
	
	public void searching(int data) {
		int index = 0;
		if(head == null) {
			System.out.println("List is empty");
		}
		Node pointer = head;
		int p = 0;
		do {
			if(pointer.data == data) {
				index = p;
				break;
			}
			pointer = pointer.next;
			p++;
		} while (pointer != head);
		System.out.println("Index of the given data in list is "+index);
	}

}
