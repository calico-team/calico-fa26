import java.io.*;
import java.util.*;

class Solution {
    
    /*
     * Print a sequence of guesses until you guess the answer string.
     * You may use the readString() and printGuess() helper functions defined below.
     *
     * N: Length of the string
     * K: Number of different -ities
     * A: List containing the different -ities
     */
    static void solve(int N, int K, String[] A) throws IOException {
        String guess = "_".repeat(N);
		for (int i = 0; i < K; i++) {
			StringBuilder newGuess = new StringBuilder();
			for (int j = 0; j < N; j++) {
				if (guess.charAt(j) == '_') {
					newGuess.append(A[i]);
				}
				else {
					newGuess.append(guess.charAt(j));
				}
			}

			guess = newGuess.toString();
			printGuess(guess);
			guess = readString();

			if (guess.equals("CORRECT")) {
				break;
			}
		}
    }

    /*
     * Reads a single string from standard input.
     */
    static String readString() throws IOException {
        return in.readLine();
    }

    /*
     * Prints a guess to standard output. The PrintWriter will automatically flush the output stream buffer.
     */
    static void printGuess(String guess) {
        out.println(guess);
    }


    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out, true);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());

        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int K = Integer.parseInt(temp[1]);

            String[] A = in.readLine().split(" ");

            solve(N, K, A);
        }
    }
}
