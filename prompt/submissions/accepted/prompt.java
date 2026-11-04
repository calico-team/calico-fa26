import java.io.*;

class Solution {
    
	public static String solve(String prompt){
        if (prompt.contains("write_me")) {
			return prompt + "make_it_sound_human";
		}
        else if (prompt.contains("what_is")) {
            return prompt + "do_not_hallucinate";
		}
        else if (prompt.contains("solve")) {
            return prompt + "make_no_mistakes";
		}
        else {
            return prompt + "thank_you";
		} 
    }

	static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    public static void main(String[] args) throws IOException{ 
        int T = Integer.parseInt(in.readLine());


        for (int t = 0; t < T; t++) {
            String prompt = in.readLine();

            String result = solve(prompt);
            out.println(result);
        }
        out.flush();
    } 
}