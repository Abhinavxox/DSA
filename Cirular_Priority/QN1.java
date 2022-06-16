package Cirular_Priority;

import java.util.Arrays;

public class QN1 {
	
	//write a program to perform basic operations in a circular queue using arrays
	public static void main(String[] args) {
		 QN1 obj = new QN1();
		 obj.enqueue(1);
		 obj.enqueue(2);
		 obj.enqueue(3);
		 obj.enqueue(4);
		 obj.enqueue(5);
		 obj.enqueue(6);
		 obj.enqueue(7);
         System.out.println(Arrays.toString(obj.circularQueue));
         obj.dequeue();
         obj.dequeue();
         System.out.println("----Queue after two times dequeue");
         System.out.println(Arrays.toString(obj.circularQueue));
	}
	
	int N = 10;
	int circularQueue[] = new int[N];
	int front = -1;
	int rear = -1;
	
	public void enqueue(int data) {
		
		//if queue is full
		if((rear+1)%N==front) {
			System.out.println("The queue is full");
		}
		//if queue is empty
		else if(isEmpty()) {
			front =0;
			rear =0;
			circularQueue[rear] = data;
		}
		else {
			rear = (rear+1)%N;
			circularQueue[rear] = data;
		}
		
	}
	
	public int dequeue() {
		if(isEmpty()) {
			System.out.println("The queue is empty");
		}
		else if(front == rear){
	        front = rear=-1;
	    }
		else {
			int value = circularQueue[front];
			front = (front+1)%N;
			return value;
		}
		return 0;
		
	}
	
	public boolean isEmpty() {
		if(front==-1&&rear==-1) {
			return true;
		}else {
			return false;
		}
	}
	
	public int length() {
		return (N+rear-front)%N;
	}
	public int peek() {
		return circularQueue[front];
	}

}
