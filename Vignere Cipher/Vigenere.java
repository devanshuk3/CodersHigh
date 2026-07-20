import java.util.Scanner;
public class Vigenere {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

            String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        System.out.print("First input: ");
String input = sc.nextLine().toUpperCase();

    System.out.print("Encyption Key: ");
        String key = sc.nextLine().toUpperCase();

        String cipher = "";

        for (int i = 0; i < input.length(); i++) {
            int p = letters.indexOf(input.charAt(i));
                int k = letters.indexOf(key.charAt(i % key.length()));
             cipher += letters.charAt((p + k) % 26);
        }

        System.out.println("Ciphertext: " + cipher);
        sc.close();
    }
}