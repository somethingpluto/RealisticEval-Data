import java.util.Arrays;
import java.util.Random;

public class MedianFinder {
    public static double findMedian(int[] arr) {
        // Sort the array in ascending order
        Arrays.sort(arr);
        
        int n = arr.length;
        int midIndex = n / 2;

        // Determine if the array length is even or odd and return the median
        if (n % 2 == 0) {
            // Even number of elements: average the two middle elements
            return (arr[midIndex - 1] + arr[midIndex]) / 2.0;
        } else {
            // Odd number of elements: return the middle element
            return arr[midIndex];
        }
    }

    public static void main(String[] args) {
        Random random = new Random();
        int[] largeArray = random.ints(10001, 0, 10000).toArray();
        double median = findMedian(largeArray);
        System.out.println("Median: " + median);
    }
}