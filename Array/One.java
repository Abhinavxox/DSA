package Array;
import java.util.Arrays;

public class One {
	
	public static void main(String[] args) {
		creation();
		insertion();
		deletion();
		traversing();
		searching();
	}
	
	static void creation() {
		int[] arr = new int[11];
		for(int i = 0; i<=10; i++) {
			arr[i]=i;
		}
		System.out.println(Arrays.toString(arr));
	}
	
	static void insertion() {
		int[] arr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		//inserting 88 at index 8
		int[] newarr = new int[arr.length+1];
		for(int i=0; i<arr.length+1; i++) {
			if(i<8) {
				newarr[i] = arr[i];
			}else if(i == 8) {
				newarr[i] = 88;
			}else {
				newarr[i]=arr[i-1];
			}
		}
		System.out.println(Arrays.toString(newarr));
	}

	static void deletion() {
		int[] arr2 = {55, 56, 57, 58, 59};
		//deleting the object at index 2
		int[] newarr2 = new int[arr2.length-1];
		for(int i = 0, k= 0; i<arr2.length; i++) {
			if(i == 2) {
				continue;
			}
			newarr2[k++] = arr2[i];
		}
		System.out.println(Arrays.toString(newarr2));
	}
	
	static void traversing() {
		int[] arr = {1001, 1002, 1003, 1004, 1005, 1006, 1009, 1008, 1007};
		for(int  i:arr) {	
			System.out.println(i);
		}
	}
	
	static void searching() {
		//search for element "3" in the array and get its index
		int[] arr3 = {1, 3, 5, 7, 9, 11};
		for(int i = 0; i<arr3.length; i++) {
			if(arr3[i] == 3) {
				System.out.println("Its index is "+i);
			}

		}
	}
	
	
}
