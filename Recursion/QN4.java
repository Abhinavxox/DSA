package Recursion;

public class QN4 {
	
	//Write a program to find the sum of n natural numbers in Java using Recursion
	public static void main(String[] args) {
		int highest_number = 10;
		System.out.println(sumOfNumbers(highest_number));
	}
	
	static int sumOfNumbers(int max) {
		if(max == 1) {
			return max;
		} 
		return max+sumOfNumbers(max-1);
	}
	
}
