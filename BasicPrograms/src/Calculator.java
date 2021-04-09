import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        int a,b,add,sub,mul,div;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter 1st number");
        a=sc.nextInt();
        System.out.println("enter 2nd number");
        b=sc.nextInt();
        add=a+b;
        sub=a-b;
        mul=a*b;
        div=a/b;
        System.out.println("add is"+add);
        System.out.println("sub is"+sub);
        System.out.println("mul is"+mul);
        System.out.println("div is"+div);

    }
}
