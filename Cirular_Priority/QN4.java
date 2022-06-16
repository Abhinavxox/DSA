package Cirular_Priority;

import Cirular_Priority.QN3.Node;

public class QN4 {
	
	//implement priority queue using unsorted list
	public static void main(String[] args) {
		QN4 obj = new QN4();
		obj.add(1, 11);
		obj.add(7, 13);
		obj.add(3, 12);
		obj.add(9, 14);
		obj.add(2, 15);
		obj.print();
		System.out.println("-----highest key-------");
		System.out.println(obj.peek());
		obj.pop();
		System.out.println("------after pop----");
		obj.print();
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
	
	static Node head = null;
	static Node tail = null;
	
	void print() {
		Node pointer = head;
		while(pointer.next != null) {
			System.out.println(pointer.key+" "+pointer.value);
			pointer = pointer.next;
		}
		System.out.println(pointer.key+" "+pointer.value);
		
	}
	
	//basic operations of priority queue using unsorted list
	boolean is_empty() {
		if(head==null) {
			return true; 
		}
		return false;
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
	
	void add(int k, int v) {
		Node newNode = new Node(k,v);
		//check if list is empty
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
			tail.next = newNode;
			tail = newNode;
	}
	
	String peek() {
		String out = "";
		Node pointer = head;
		Node temp = head;
		int p = pointer.key;
 		while(pointer!=null) {
			if(pointer.key>p) {
				p = pointer.key;
				temp = pointer;				
			}
			pointer = pointer.next;
		}
 		out = "("+temp.key+","+temp.value+")";
		return out;
	}
	
	void pop() {
		int position  = pos();
		//------------
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
	
	static int pos() {
		Node pointer = head;
        int key = pointer.key;
        int counter = 0;
             while(pointer!=null) {
                if(pointer.key>key) {
                    key = pointer.key;			
                }
                pointer = pointer.next;
            }
        pointer = head;
        while(pointer.key!=key) {
            counter++;
            pointer = pointer.next;
        }
        return counter;
	}
	
	
}
