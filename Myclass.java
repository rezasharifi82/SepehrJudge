import java.util.Scanner;

public class Myclass {

    public static void main(String[] args) {
        // Create a Scanner object
        Scanner scanner = new Scanner(System.in);

        // Get the first integer from the user
        int firstNumber = scanner.nextInt();

        // Get the second integer from the user
        int secondNumber = scanner.nextInt();

        // Calculate the sum
        int sum = firstNumber + secondNumber;

        // Print the sum
        System.out.println(sum);
    }
}
