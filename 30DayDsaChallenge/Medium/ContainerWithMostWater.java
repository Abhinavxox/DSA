package Medium;

public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int n = height.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                // to reduce complexity
                    // finding the area
                    int firstHeight = height[i];
                    int secondHeight = height[j];
                    int area;
                    if (firstHeight < secondHeight) {
                        area = firstHeight * (j - i);
                    } else {
                        area = secondHeight * (j - i);
                    }
                    // finding the max
                    if (area > maxArea) {
                        maxArea = area;
                    }
            }
        }
        return maxArea;
    }
}
