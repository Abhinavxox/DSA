package Stack_and_Queue;
import java.util.ArrayList;

public class QN5 {
	
	public static void main(String[] args) {
		QN5 obj = new QN5();
		obj.push(1);
		obj.push(2);
		obj.push(3);
		obj.push(4);
		obj.push(5);
		System.out.println("Stack after pushing 5 elements:");
		obj.print();
		obj.pop();
		obj.pop();
		System.out.println("Stack after poping 2 elements:");
		obj.print();
		obj.reverse();
		System.out.println("Stack after reversing:");
		obj.print();
		obj.push(11);
		System.out.println("reverse stack after pushing 11:");
		obj.print();

	}
	
	int top = -1;
	int rear = 0;
	ArrayList<Integer> stack = new ArrayList<Integer>();
	
	public void push(int data) {

		stack.add(data);
		top++;
	}
	
	public void pop() {
		if(top == -1) {
			System.out.println("Stack is empty");
			return;
		}
		stack.remove(top);
		top--;
	}
	
	
	public void print() {
		for(int i = stack.size()-1; i>=0; i--) {
			System.out.println(stack.get(i));
		}
	}
	
	public void reverse() {
		ArrayList<Integer> reverseStack = new ArrayList<Integer>();
		for(int i = stack.size()-1; i>=0; i--) {
			reverseStack.add(stack.get(i));
		}
		stack = reverseStack;
	}

}
