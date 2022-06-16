package Cirular_Priority;

public class QN3 {
	
	//implement priority queue using sorted list
	public static void main(String[] args) {
		QN3 obj = new QN3();
		obj.add(1, 11);
		obj.add(7, 13);
		obj.add(3, 12);
		obj.add(2, 15);
		obj.add(9, 14);
		obj.print();
		System.out.println("-----lowest key-------");
		System.out.println(obj.min());
		obj.remove_min();
		System.out.println("------after remove_min----");
		obj.print();
		System.out.println("--------length---------");
		System.out.println(obj.len());
	}

	class Node{
		int key;
		int value;
		Node next;
		Node(int key, int value){
			this.key = key;
			this.value = value;
			this.next = null;
		}
	}
	
	Node head = null;
	Node tail = null;
	
	void print() {
		Node pointer = head;
		while(pointer.next != null) {
			System.out.println(pointer.key+" "+pointer.value);
			pointer = pointer.next;
		}
		System.out.println(pointer.key+" "+pointer.value);
		
	}
	
	//basic operations of priority queue using sorted list
	boolean is_empty() {
		if(head==null) {
			return true; 
		}
		return false;
	}
	
	void add(int k, int v) {
		Node newNode = new Node(k,v);
		Node pointer = head;
		//if the list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
		//if newnode has the lowest priority
		else if(pointer.key>k) {
			newNode.next = head;
			head = newNode;
		}
		else {
			//find the position of placement of newNode
			while(pointer.next!=null && pointer.next.key < k) {
				pointer=pointer.next;
			}
			newNode.next = pointer.next;
			pointer.next = newNode;
		}
	}
	
	String min() {
		String out = "("+head.key+","+head.value+")";
		return out;
	}
	
	String remove_min() {
		Node temp = head;
		//check if list is empty
		if(head == null) {
			System.out.println("Queue is empty");
		}
		String out = "("+head.key+","+head.value+")";
		temp = head.next;
		head = temp;
		return out;
	}
	
	int len() {
		Node pointer = head;
		int counter = 0;
		while(pointer!=null) {
			counter++;
			pointer = pointer.next;
		}
		return counter;
	}
	
	
}
