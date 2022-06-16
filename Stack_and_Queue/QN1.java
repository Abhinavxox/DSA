package Stack_and_Queue;

public class QN1 {
	
	public static void main(String[] args) {
		QN1 obj = new QN1();
		obj.push(1);
		obj.push(2);
		obj.push(3);
		obj.push(4);
		System.out.println("Stack after inserting 1, 2, 3, 4:");
		obj.print();
		obj.pop();
		System.out.println("Stack after poping 4");
		obj.print();
		System.out.println("Peek function : "+obj.peek());
	}
	
	int size = 10;
	int stack[] = new int[size];
	int top = -1;
	
	public void push(int data) {
		//check if the stack is full
		if(top == size-1) {
			System.out.println("Stack is already full");
			return;
		}
		top++;
		stack[top] = data;

	}
	
	public int pop() {
		int data = 0;
		if(top == -1) {
			System.out.println("Stack is empty");
		}else {
			data = stack[top];
			stack[top] = 0;
			top--;
		}
		return data;

	}
	
	public void print() {
		for(int i = top; i>=0; i--) {
			System.out.println(stack[i]);
		}
	}
	
	public int peek() {
		int data = stack[top];
		return data;
	}
	
	
	
	
	
}
