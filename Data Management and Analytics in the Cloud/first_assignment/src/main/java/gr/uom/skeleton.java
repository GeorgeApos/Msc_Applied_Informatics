package gr.uom;

import java.io.*;
import java.util.*;

import io.github.cdimascio.dotenv.Dotenv;
import redis.clients.jedis.Jedis;

public class skeleton {

  public static void main(String[] args) throws IOException {
    String replyFromUser;

    Map<String, Serializable> env = new Main().loadEnv();

    Jedis jedis = new Jedis((String) env.get("REDIS_HOST"), (int) env.get("REDIS_PORT"));

    BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));

    while (true) {
      System.out.println("(I)nsert an artist | (Q)uery an artist | (S)tatistics | e(X)it");
      replyFromUser = inFromUser.readLine();

      switch (replyFromUser.toUpperCase()) {
        case "I":
          insertArtist(jedis, inFromUser);
          break;
        case "Q":
          queryArtist(jedis, inFromUser);
          break;
        case "S":
          showStatistics(jedis);
          break;
        case "X":
          System.out.println("Goodbye");
          jedis.close();
          System.exit(0);
        default:
          System.out.println(replyFromUser + " is not a valid choice, retry");
      }
    }
  }

  private static void insertArtist(Jedis jedis, BufferedReader inFromUser) throws IOException {
    System.out.println("Enter your username:");
    String username = inFromUser.readLine();

    System.out.println("Enter artist name:");
    String artistName = inFromUser.readLine();

    String existingUser = jedis.hget(artistName, "user");
    if (existingUser != null) {
      System.out.println("This artist is already recorded by " + existingUser);
    } else {
      jedis.hset(artistName, "user", username);
      System.out.println("Artist \"" + artistName + "\" inserted successfully by " + username);
    }
  }

  private static void queryArtist(Jedis jedis, BufferedReader inFromUser) throws IOException {
    System.out.println("Enter artist name:");
    String artistName = inFromUser.readLine();

    String existingUser = jedis.hget(artistName, "user");
    if (existingUser != null) {
      jedis.hincrBy(artistName, "counter", 1);
      String counter = jedis.hget(artistName, "counter");
      System.out.println("Artist \"" + artistName + "\" was entered by " + existingUser + " and has been queried " + counter + " times.");
    } else {
      System.out.println("Artist \"" + artistName + "\" not found.");
    }
  }

  private static void showStatistics(Jedis jedis) {
    Map<String, Integer> userCounters = new HashMap<>();
    Set<String> artistSet = jedis.keys("*");
    for (String artist : artistSet) {
      if (jedis.type(artist).equals("hash")) {
        Map<String, String> artistMap = jedis.hgetAll(artist);
        String username = artistMap.get("user");
        if (username != null) {
          userCounters.put(username, userCounters.getOrDefault(username, 0) + 1);
        }
      }
    }
    for (Map.Entry<String, Integer> entry : userCounters.entrySet()) {
      System.out.println("User: " + entry.getKey() + " | Counter: " + entry.getValue());
    }

    int totalQueries = 0;
    int totalArtists = userCounters.size();
    for (String artist : artistSet) {
      if (jedis.type(artist).equals("hash")) {
        Map<String, String> artistMap = jedis.hgetAll(artist);
        String counterValueStr = artistMap.get("counter");
        if (counterValueStr != null) {
          totalQueries += Integer.parseInt(counterValueStr);
        }
      }
    }
    System.out.println("Mean of queries per artist: " + (totalArtists > 0 ? totalQueries / totalArtists : 0));
  }
}
