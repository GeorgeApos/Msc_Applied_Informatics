package gr.uom;

import io.github.cdimascio.dotenv.Dotenv;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Serializable;
import java.util.Map;

public class Main {
  public static void main(String[] args) throws Exception {
    System.out.println("Do you want to test Redis connection or run the main program? (T/M)");
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String replyFromUser = reader.readLine();
    if (replyFromUser.equalsIgnoreCase("T")) {
      testJedis.main(args);
    } else if (replyFromUser.equalsIgnoreCase("M")) {
      skeleton.main(args);
    } else {
      System.out.println(replyFromUser + " is not a valid choice, retry");
    }
  }

  public Map<String, Serializable> loadEnv() {
    Dotenv dotenv = Dotenv.configure().load();

    String redisHost = dotenv.get("REDIS_HOST");
    int redisPort = dotenv.get("REDIS_PORT") != null ? Integer.parseInt(dotenv.get("REDIS_PORT")) : 6379;
    if (redisHost == null) {
      System.err.println("REDIS_HOST environment variable is not set");
      System.exit(1);
    }

    return Map.of("REDIS_HOST", redisHost, "REDIS_PORT", redisPort);
  }
}
