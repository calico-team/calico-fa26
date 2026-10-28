import java.io.*;

class Solution{ 
    public static void main(String[] args) throws IOException{ 

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        int T = Integer.parseInt(br.readLine());


        for (int t = 0; t < T; t++) {
            String prompt = br.readLine();

            String result = solve(prompt);
            pw.println(result);
        }

        pw.flush();
    }


    public static String solve(String prompt){

        if (prompt.contains("write_me")) 
            return prompt + "make_it_sound_human";
        else if (prompt.contains("what_is"))
            return prompt + "do_not_hallucinate";
        else if (prompt.contains("solve")) 
            return prompt + "make_no_mistakes";
        else 
            return prompt + "thank_you";
        
    }
    
}