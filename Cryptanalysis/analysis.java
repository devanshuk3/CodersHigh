package Cryptanalysis;

import java.io.*;
import java.util.*;

public class analysis {
    public static void main(String[] args) throws Exception {
        // Counting freq of each char
        HashMap<Character, Integer>freqCount = new HashMap<>(); //to store values initially
        Scanner sc = new Scanner(new File("encrypted.txt"));
        while(sc.hasNextLine()) { //raed every line
            String word=sc.nextLine(); //store one line
            for (int i=0 ;i<word.length();i++) {
                char ch = word.charAt(i); //convert line into characters
                freqCount.put(ch, freqCount.getOrDefault(ch, 0) + 1); //gets and updates freq of each character
            }
        }
        sc.close();
        System.out.println("Character Frequencies:");
        System.out.println(freqCount);

        // Convert HashMap to list because hashmap cannot be sorted directly
        List<Map.Entry<Character,Integer>> items=new ArrayList<>(freqCount.entrySet());

        // Bubble Sort for decreasign frequency
        for (int i = 0; i < items.size();i++) {
            for (int j=i+1; j<items.size();j++) {
                if (items.get(j).getValue()>items.get(i).getValue()) { //each element compares with the elments after it
                        //getValue returns the frequerncy 
                    Map.Entry<Character, Integer>temp = items.get(i); //swap values by creating a temp variable
                    items.set(i,items.get(j));
                    items.set(j,temp);
                }
            }
        }
        String[] letters = {
                "E", "T", "A", "O", "I", "N", "S", "R", "H", "D",
                "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B",
                "V", "K", "X", "Q", "J", "Z" 
        };
        HashMap<Character, Character> dictionary = new HashMap<>(); //substitution dictionary 
        //  contains a  keys and values from english and cipher text
        for (int i=0;i<items.size()&&i<letters.length;i++) {
            dictionary.put(items.get(i).getKey(),letters[i].charAt(0)); //charAt(0) because of strings in array letters
        }

        System.out.println("\nSubstitution Dictionary:");
        System.out.println(dictionary);

        // Decrypt the file
        BufferedReader br=new BufferedReader(new FileReader("encrypted.txt")); //re read the file to substite the values
        BufferedWriter bw=new BufferedWriter(new FileWriter("decryptedJava.txt"));

        String line; //variable to store one line
        while ((line=br.readLine())!= null) {
            StringBuilder newLine=new StringBuilder();
            for (char ch:line.toCharArray()) {
                if (dictionary.containsKey(ch)) {
                    newLine.append(Character.toLowerCase(dictionary.get(ch)));
                } else {
                    newLine.append(ch);
                }
            }
            bw.write(newLine.toString());
            bw.newLine();
        }
        br.close();
        bw.close();
        System.out.println("\nDecrypted text written to decrypted.txt");
    }
}