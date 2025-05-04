import java.io.*;
import java.util.*;
public class Main
{
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N,M;
        int [] A;
        StringTokenizer st;
        st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        A=new int[N];
        st=new StringTokenizer(br.readLine());

        int [] S = new int[N+1];
        for(int i=1; i<=N; i++)
        {
            S[i]=S[i-1]+Integer.parseInt(st.nextToken());
        }
        for(int i=0; i<M; i++)
        {
            st=new StringTokenizer(br.readLine());

            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());

            System.out.println(S[b]-S[a-1]);
        }



    }
}