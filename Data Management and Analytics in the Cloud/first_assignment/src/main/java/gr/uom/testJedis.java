package gr.uom;

import java.io.Serializable;
import java.util.*;
import io.github.cdimascio.dotenv.Dotenv;
import redis.clients.jedis.Jedis;

public class testJedis {

  public static void main (String [] args) throws Exception {

    Map<String, Serializable> env = new Main().loadEnv();

    Jedis jedis = new Jedis((String) env.get("REDIS_HOST"), (int) env.get("REDIS_PORT"));

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
