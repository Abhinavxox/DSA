package Stack_and_Queue;

public class QN4 {
	
	class Node{
		int data;
		Node next;
		Node(int data){
			this.data = data;
			this.next = null;
		}
	}
	
	public static void main(String[] args) {
		QN4 obj = new QN4();
		obj.enqueue(1);
		obj.enqueue(2);
		obj.enqueue(3);
		obj.enqueue(4);
		obj.enqueue(5);
		System.out.println("Queue after enqueueing 5 elements");
		obj.print();
	
		obj.dequeue();
		obj.dequeue();
		System.out.println("Queue after dequeueing 2 times");
		obj.print();
		
		System.out.println("Peeking 4 in the queue");
		obj.peek(4);
		
		
	}
	
	public Node head = null;
	public Node tail = null;
	
	public void enqueue(int data) {
		Node newNode = new Node(data);
		if(head == null) {
			head = newNode;
			tail = newNode;
		}
		tail.next = newNode;
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
	
	public void dequeue() {
		if(!isEmpty()) {
			Node temp = head;
			Node temp2 = head;	
			System.out.println("Element removed :"+head.data);
			temp2 = temp.next;
			head = temp2;
		}
	}
	
	public boolean isEmpty() {
		if(head == null) {
			System.out.println("Queue is empty");
			return true;
		}
		return false;
	}
	
	public void peek(int data) {
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
		System.out.println("Index of the given data in queue is "+index);
	}


}
