package Linked_list;

public class QN5 {
	
	//to implement an algo to find the k to the last element
	public static void main(String[] args) {
		QN5 obj = new QN5();
		obj.creation(1);
		obj.creation(4);
		obj.creation(2);
		obj.creation(4);
		obj.creation(3);
		obj.creation(2);
		obj.creation(9);
		obj.creation(9);
		obj.searching(2);
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
	
	public void searching(int data) {
		if(head == null) {
			System.out.println("List is empty");
		}
		Node pointer = head;
		int p = 0;
		while(pointer.next != null) {
			if(pointer.data == data) {
				//finds the elements and prints every data after it
				Node q = pointer;
				while(q.next != null) {
					System.out.println(q.data);
					q = q.next;
				}
				System.out.println(q.data);
				
			}
			pointer = pointer.next;
			p++;
		}
	}

}
