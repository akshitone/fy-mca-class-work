import java.util.Scanner;

class MaxMinAlgo {
    Scanner scanner;

    MaxMinAlgo() {
        this.scanner = new Scanner(System.in);
    }

    void minimum(int arr[], int start, int end) {
        int min = arr[start];
        for (int i = start; i <= end; i++) {
            if (arr[i] < min) {
                int temp = min;
                min = arr[i];
                arr[i] = temp;
            }
            arr[start] = min;
        }
    }

    void maximum(int arr[], int start, int end) {
        int max = arr[end];
        for (int i = start; i <= end; i++) {
            if (arr[i] > max) {
                int temp = arr[i];
                arr[i] = arr[end];
                arr[end] = temp;
            }
            max = arr[end];
        }
    }

    int getArraySize() {
        int size;
        System.out.printf("\n Enter size of list:");
        size = this.scanner.nextInt();
        return size;
    }

    int[] getArray(int size) {
        int[] arr = new int[size];
        System.out.printf("\n Enter elements:");
        for (int i = 0; i <= size - 1; i++) {
            arr[i] = this.scanner.nextInt();
        }
        return arr;
    }

    @Override
    protected void finalize() throws Throwable {
        this.scanner.close();
    }
}

public class Main {

    public static void main(String[] args) {

        MaxMinAlgo maxMinAlgo = new MaxMinAlgo();

        long startTime = System.currentTimeMillis();
        int size = maxMinAlgo.getArraySize();

        int[] arr = new int[size];

        System.out.printf("\n Unsorted Array is:");

        for (int i = 0; i <= size - 1; i++) {
            System.out.printf("\n Element %d : %d", i + 1, arr[i]);
        }

        System.out.printf("\n Sorted Array is: ");
        int start = 0, end = size - 1;
        while (start < end) {
            maxMinAlgo.minimum(arr, start, end);
            maxMinAlgo.maximum(arr, start, end);
            start++;
            end--;
        }

        for (int i = 0; i <= size - 1; i++) {
            System.out.printf("\n Element %d : %d", i + 1, arr[i]);
        }

        long endTime = System.currentTimeMillis();
        System.out.println();

        System.out.println(endTime - startTime);
    }
}