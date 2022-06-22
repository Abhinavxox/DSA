package App_of_stack;

import java.util.Stack;

public class QN3 {
	//3.Write a program to evaluate postfix expression.
	
	public static void main(String[] args) {		
		QN3 obj = new QN3();
		String exp = "231*+9-";
		if(obj.postfixEvaluate(exp)) {
			System.out.println("The result of the expression is "+ obj.stack.peek());
		}		
	}
	
	Stack<Integer> stack = new Stack<Integer>();
	
	public boolean postfixEvaluate(String input) {
		for(int i=0; i<input.length(); i++) {
			char ch = input.charAt(i);
			
			//if it is operand
			if(!isOperator(ch)) {
				stack.push(ch-'0');
			}
			else {
				try {
					//if operator is seen
					//pop two elements
					int temp1 = stack.pop();
					int temp2 = stack.pop();
					int result = 0;
					switch (ch) {
					case '+': 
						result = temp2+temp1;
						break;
					case '-': 
						result = temp2-temp1;
						break;
					case '/': 
						result = temp2/temp1;
						break;
					case '*': 
						result = temp2*temp1;
						break;
					case '^': 
						result = temp2^temp1;
						break;
				}
					//push result in stack
					stack.push(result);
					
				} catch (Exception e) {
					System.out.println("Invalid expression");
					return false;
				}
			}
		}
		return true;
	}
	
	public boolean isOperator(char input)   {  
		//check is char is operator
		if (input == '+' || input == '-' || input == '*' || input == '/' || input == '^'|| input == '(' || input == ')') {
			return true; 
		}else {
			return false;
		}
	}  
	
}
