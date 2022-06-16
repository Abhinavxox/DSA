package Cirular_Priority;

public class QN2 {
	
	//to perform basic operations in a double ended queue using arrays
	
	int N = 10;
	int circularQueue[] = new int[N];
	int front = -1;
	int rear = -1;
	
	public void insertAtTheFront(int data) {
		//if queue is full
		if((rear+1)%N==front) {
			System.out.println("The queue is full");
		}
		//if queue is empty
		else if(isEmpty()) {
			front =0;
			rear =0;
			circularQueue[front] = data;
		}
		else {
			front = (front+1)%N;
			circularQueue[front] = data;
		}
	}
	
	public void insertAtTheBack(int data) {
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
	
	public int deleteFromTheFront() {
		if(isEmpty()) {
			System.out.println("The queue is full");
		}
		else if (front == rear) {
			rear = front = -1;
		}
		else {
			int value = circularQueue[rear];
			front = (front-1)%N;
			return value;
		}
		return 0;
	}
	
	public int deleteFromTheBack() {
		if(isEmpty()) {
			System.out.println("The queue is full");
		}
		else if (front == rear) {
			rear = front = -1;
		}
		else {
			int value = circularQueue[rear];
			rear = (rear-1)%N;
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
