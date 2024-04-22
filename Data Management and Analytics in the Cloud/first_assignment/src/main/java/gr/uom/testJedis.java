package gr.uom;

import java.util.*;
import redis.clients.jedis.Jedis;

public class testJedis {

  public static void main (String [] args) throws Exception {
    String redisHost = "172.17.0.2"; // Redis Docker
    int redisPort = 6379;
    Jedis jedis = new Jedis(redisHost, redisPort);

    String key, value;

    Scanner userInput = new Scanner(System.in);

    System.out.println("Type a key:");
    key = userInput.nextLine();
    System.out.println("Type a value:");
    value = userInput.nextLine();
    jedis.set(key, value);

    System.out.println("Type a key:");
    key = userInput.nextLine();
    value = jedis.get(key);
    System.out.println("The value is " + value);

    jedis.close();
  }
}
