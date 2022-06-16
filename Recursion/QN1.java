package Recursion;

public class QN1 {
    public static void main(String[] args) {
    	QN1 obj = new QN1();
        System.out.println(obj.factorial(5));

    }

    int factorial(int number) {

        if (number <= 1)
            return number;

        return number * factorial(number - 1);

    }
}
