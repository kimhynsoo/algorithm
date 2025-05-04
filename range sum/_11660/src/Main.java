import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        int N,M;
        int [][] matrix;
        int [][] s_matrix;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
//        matrix=new int[N+1][N+1];
        s_matrix=new int[N+1][N+1];
//        for(int i=1; i<=N; i++)
//        {
//            st = new StringTokenizer(br.readLine());
//            for(int j=1; j<=N; j++)
//            {
//                matrix[i][j]=Integer.parseInt(st.nextToken());
//            }
//
//        }

        for(int i=1; i<=N; i++)
        {
            st = new StringTokenizer(br.readLine());

            for(int j=1; j<=N; j++)
            {
                s_matrix[i][j]=s_matrix[i-1][j]+s_matrix[i][j-1]-s_matrix[i-1][j-1]+Integer.parseInt(st.nextToken());
            }

        }

        for(int i=0; i<M; i++)
        {
            st = new StringTokenizer(br.readLine());
            int x1=Integer.parseInt(st.nextToken());
            int y1=Integer.parseInt(st.nextToken());
            int x2=Integer.parseInt(st.nextToken());
            int y2=Integer.parseInt(st.nextToken());

            System.out.println(s_matrix[x2][y2]-s_matrix[x1-1][y2]-s_matrix[x2][y1-1]+s_matrix[x1-1][y1-1]);
        }
    }
}