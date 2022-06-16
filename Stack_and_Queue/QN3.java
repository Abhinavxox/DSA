package Stack_and_Queue;

import java.util.ArrayList;

public class QN3 {
	public static void main(String[] args) {
		QN3 obj = new QN3();
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
		
		System.out.println("Peeking in the queue");
		obj.peek();
	}
	
	ArrayList<Integer> queue = new ArrayList<Integer>();
	
	int front = 0;
	int rear = -1;
	
	public void enqueue(int data) {
		queue.add(data);
		rear++;	
	}
	
	public void dequeue() {
		int a = queue.get(front);
		queue.remove(front);
		System.out.println("Element removed: "+a);
	}
	

	
	public void print() {
		for(int x : queue) {
			System.out.println(x);
		}
	}
	
	public void isEmpty() {
		if(queue.isEmpty()) {
			System.out.println("Queue is empty");
		}
	}
	
	public void peek() {
		System.out.println(queue.get(front));
	}
	
}
