import java.io.*;

class Solution {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    /**
    * Send one guess to the judge and return the judge's reply.
    *
    * GUESS: a string of length N, one character per position
    * Returns: the judge's reply for this guess: either the string
    *         "CORRECT", or a string of length N where position i shows
    *         the true character if GUESS.charAt(i) was correct and '_'
    *         otherwise.
    */
    static String submit(String GUESS) throws IOException {
        out.println(GUESS);
        out.flush();
        return in.readLine();
    }

    /**
    * Guess the hidden string of length N.
    *
    * N: the length of the hidden string
    * K: the number of allowed characters
    * A: the list of the K allowed characters
    * The hidden string must be guessed using submit(); use no more than
    * 2*N guesses.
    */
    static void solve(int N, int K, String[] A) throws IOException {
        // YOUR CODE HERE
    }

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());

        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int K = Integer.parseInt(temp[1]);

            String[] A = in.readLine().split(" ");
            solve(N, K, A);
        }
        out.flush();
    }
}
