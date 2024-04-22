import java.io.*;
import java.net.*;
import java.util.*;
import redis.clients.jedis.Jedis;

public class tinyURL {

	public static void main (String [] args) throws Exception {

		String replyFromUser;
		Jedis jedis = new Jedis();

		// read from the input
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in)); 
		
		while (true){
			System.out.println("(I)nsert an artist | (Q)uery an artist | (S)tatistics | e(X)it");
			replyFromUser = inFromUser.readLine(); //read the reply
			if (replyFromUser.equals("I")) {
				// to be done
			} else if (replyFromUser.equals("Q")) {
				// to be done
			} else if (replyFromUser.equals("S")) {
				// to be done
			} else if (replyFromUser.equals("X")) {
				System.out.println("Goodbye");
				System.exit(1);
			} else {
				System.out.println(replyFromUser + "is not a valid choice, retry");
			}
		}
	}
}
