import java.util.Scanner;

public class PrintN {
    public static void main(String[] args) {
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the limit");
        n=sc.nextInt();
        for(int i=0;i<=n;i++)
        {
            System.out.println(i);
        }
    }
}
