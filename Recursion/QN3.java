package Recursion;

public class QN3 {
	
	//Write a programto reverse String in Java using Recursion
	public static void main(String[] args) {
		System.out.println(reversal("reverse"));
	}
	
	static String reversal(String input) {
		
		if(input==null) {
			System.out.println("INVALID");
			return input;
		}
		else if(input.length()<=1){
			return input;
		}
		System.out.print(input.charAt(input.length()-1));
		return reversal(input.substring(0, input.length()-1));
	}

}
