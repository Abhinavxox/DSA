package Easy;

public class BestTimeToBuyAndSellStock {

    public static void main(String[] args) {
        int[] prices = { 7, 1, 5, 3, 6, 4 };
        System.out.println(maxProfit(prices));
    }

    public static int maxProfit(int[] prices) {
        int profit = 0;
        int lowPrice = prices[0];
        for (int i = 0; i < prices.length - 1; i++) {
            int curPrice = prices[i];
            int nextPrice = prices[i + 1];
            if (lowPrice > curPrice)
                lowPrice = curPrice;
            if (profit < nextPrice - lowPrice)
                profit = nextPrice - lowPrice;
        }
        return profit;
    }
}
