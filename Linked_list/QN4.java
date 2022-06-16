package Linked_list;

public class QN4 {
	//to remove duplicates from an unsorted linked list.
	public static void main(String[] args) {
		QN4 obj = new QN4();
		System.out.println("Unordered list");
		obj.creation(1);
		obj.creation(4);
		obj.creation(2);
		obj.creation(4);
		obj.creation(3);
		obj.creation(2);
		obj.creation(9);
		obj.creation(9);
		obj.print();
		System.out.println("New list");
		obj.question();
		obj.print();
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
	
	public void question() {
		Node pointer = head;
		Node index = null;
		Node temp = null;
		while(pointer != null) {
			temp = pointer;
			index = pointer.next;
			while(index != null) {
				if (pointer.data == index.data) {
					temp.next = index.next;
				}else {
					temp = index;
				}
				index = index.next;
			}
			pointer = pointer.next;
		}
	}

}
