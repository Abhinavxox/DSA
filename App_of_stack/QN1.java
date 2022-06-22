package App_of_stack;

import java.util.Stack;

public class QN1 {
	//1.Write a program to convert infix to postfix expression.
	public static void main(String[] args) {
		QN1 obj = new QN1();
		System.out.println(obj.infixToPostfix("A*B/D*(C-E)/F^G^H^I/J"));
	}
	
	Stack<Character> stack = new Stack<Character>();
	
	public String infixToPostfix(String input) {
		String postfix = "";
		for(int i=0; i<input.length(); i++) {
			char ch = input.charAt(i);
			//first check if it is operand or operator
			if(!isOperator(ch)) {
				postfix+=ch;
			}
			else {
				//if it is operator
				if(stack.isEmpty()) {
					//first operator
					stack.push(ch);
				}
				else if(ch=='(') {
					stack.push(ch);
				}
				else if(ch==')') {
					 while (!stack.isEmpty() && stack.peek() != '(') {
		                    postfix += stack.pop();
		                    
					 }
					 stack.pop();		
				}
				else {
					//check presidency
					while(!stack.isEmpty() && presidencyChart(ch)<=presidencyChart(stack.peek())) {
							postfix+=stack.pop();
					}
					stack.push(ch);
				}
			}
		}
		while(!stack.isEmpty()) {
			postfix+= stack.pop();
		}
		return postfix;
	}
	
	public int presidencyChart(char input) {
		switch (input)
        {
        case '+':
        case '-':
            return 1;
      
        case '*':
        case '/':
            return 2;
      
        case '^':
            return 3;
            
        case '(':
        	return -1;
        }
        return 0;
	}
	
	public int associativity(char input) {
		//if the presidency is same
		//0 means LtoR
		//1 means RtoL
		if(input == '^') {
			return 1;
		}
		else return 0;
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
