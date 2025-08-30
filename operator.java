import java.util.*;
import java.io.*;
class Operator{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        int age = sc.nextInt();
        double height = sc.nextDouble();
        System.out.println("Name = "+name);
        System.out.println("Age = "+age);
        System.out.println("Height = "+height);
    }
}