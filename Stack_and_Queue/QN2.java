package Stack_and_Queue;

import java.util.ArrayList;

public class QN2 {
	
	public static void main(String[] args) {
		
		QN2 obj = new QN2();
		obj.creation(1);
		obj.creation(2);
		obj.creation(3);
		obj.creation(4);
		obj.creation(5);
		
		System.out.println("The current stack is :");
		obj.print();
		
		obj.push(6);
		obj.push(7);
		System.out.println("The stack after pushing 6, 7 :");
		obj.print();
		
		obj.pop();
		System.out.println("The stack after poping top");
		obj.print();
		
		obj.peek();
		
		
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
		ArrayList<Integer> a = new ArrayList<Integer>();
		Node pointer = head;
		while(pointer.next != null) {
			a.add(pointer.data);
			pointer = pointer.next;
		}
		a.add(pointer.data);
		for(int i = a.size()-1; i>=0; i--) {
			System.out.println(a.get(i));
		}
		
	}
	
	public void push(int data) {
		Node newNode = new Node(data);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
			tail.next = newNode;
			tail = newNode;
	}
	
	public void pop() {
		//check if list is empty
		if(head == null) {
			System.out.println("Stack is empty");
		}
		Node pointer = head;
		while(pointer.next!= tail) {
			pointer = pointer.next;
		}
		tail = pointer;
		tail.next = null;
	}
	
	public void peek() {
		Node pointer = tail;
		System.out.println("The top of the stack contains "+ pointer.data);
	}
	
	

}
