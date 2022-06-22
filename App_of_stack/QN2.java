package App_of_stack;

import java.util.HashMap;
import java.util.Stack;

public class QN2 {
	//2.Write a program to check for balanced paratheses in an expression.
	Stack<Character> stack = new Stack<Character>();
	
	public static void main(String[] args) {
		QN2 obj = new QN2();
		String exp = "[a+{b-(a+b)+(a+b)}}]";
		if(obj.balancedParanthesis(exp)) System.out.println("Expression is correct");
		else System.out.println("Expression is incorrect");
	}
	
	HashMap<Character, Character> table = new HashMap<Character, Character>();
	
	public boolean balancedParanthesis(String input) {
		//table
		table.put(')','(');
		table.put('}','{');
		table.put(']','[');
		
		//traversing the string
		for(int i = 0; i< input.length(); i++) {
			char ch = input.charAt(i);
			
			//for opening paranthesis
			if(table.containsValue(ch)) {
				stack.add(ch);
			}
			//for closing ones
			if(table.containsKey(ch)) {
				if(stack.peek()==table.get(ch)) {
					stack.pop();
				}
				//if wrong expression
				else {
					return false;
				}
			}
		}
		return true;
	}
	

}
