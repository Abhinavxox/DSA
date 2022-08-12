package Easy;

import java.util.ArrayList;

public class PascalsTriangle {

    public static void main(String[] args) {
        int numRows = 5;
        System.out.println(generate(numRows));
    }

    public static ArrayList<ArrayList<Integer>> generate(int numRows) {
        ArrayList<ArrayList<Integer>> alist = new ArrayList<>();
        int pointer = 0;
        for (int i = 0; i < numRows; i++) {
            ArrayList<Integer> internalList = new ArrayList<>();
            if (i == 0) {
                internalList.add(1);
                alist.add(internalList);
                continue;
            }
            int upperSize = alist.get(pointer).size();
            internalList.add(1);
            if (upperSize != 1) {
                for (int j = 0; j < upperSize - 1; j++) {
                    internalList.add(alist.get(pointer).get(j) + alist.get(pointer).get(j + 1));
                }
            }
            internalList.add(1);
            alist.add(internalList);
            pointer++;
        }
        return alist;
    }
}
