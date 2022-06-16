package Recursion;

public class QN5 {
	
	//Write a program to find how many digits a positive integer has using recursion and test the function that calls this with the values 15, 105,15105? HINT :If n is an integer , n/10 will be an integer without fractional part.
	public static void main(String[] args) {
		System.out.println(five(15));
		System.out.println(five(105));
		System.out.println(five(15105));
	}
	
	static int five(int input) {
		if(input==0) {
			return 0;
		}
		return 1 + five(input/10);
	}
	
}
