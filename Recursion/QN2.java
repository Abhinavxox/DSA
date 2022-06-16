package Recursion;

public class QN2 {
    public static void main(String[] args) {
    	QN2 obj = new QN2();
        obj.fibonacci(10);
    }

    int num1 = 0;
    int num2 = 1;

    void fibonacci(int number) {
        if (number == 0)
            return;
        System.out.print(num1 + " ");
        int temp = num2;
        num2 = num1 + num2;
        num1 = temp;
        number--;
        fibonacci(number);

    }
}
