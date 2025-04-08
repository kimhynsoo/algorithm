import java.io.*;
import java.util.*;
public class Main
{
    // tip: arguments are passed via the field below this editor
    public static void main (String[] args)throws IOException
    {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int n = Integer.parseInt(br.readLine());
    int sum=0;
    int max=-1;
    st= new StringTokenizer(br.readLine());
    for(int i=0; i<n; i++)
    {
        int score=Integer.parseInt(st.nextToken());
        sum +=score;
        if(score>max)
            max=score;
    }

//    double result = (double)sum * 100/max/n;

    System.out.println(sum* 100.0 / max / n);




    }
}