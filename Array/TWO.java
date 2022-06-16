package Array;

import java.util.Arrays;

public class TWO {
	
	public static void main(String[] args) {
		findMin();
	}
	
	static void findMin(){
		int[] arr = {14, 33, 45, 12, 9, 7, 11};
		Arrays.sort(arr);
		System.out.println(arr[0]);
	}

}
