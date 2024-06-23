from neo4j import GraphDatabase
import json

uri = "neo4j://graphdb.mad.uom.gr:8687"
username = "db"
password = "db-neo4j"

driver = GraphDatabase.driver(uri, auth=(username, password))


queries = {
    "query_1": """
        MATCH (c:Category)-[:PART_OF]-(p:Product)-[:SUPPLIES]-(s:Supplier)
        WHERE s.country IN ['USA', 'UK']
        RETURN c.categoryName AS category, c.description AS description
    """,
    "query_2": """
        MATCH (p:Product)-[:ORDERS]-(o:Order)
        WHERE (p.productName STARTS WITH 'C' OR p.productName ENDS WITH 't')
          AND o.discount > 0.25
        RETURN p.productName AS product
    """,
    "query_3": """
        MATCH (s:Supplier)-[:SUPPLIES]->(p:Product {productName: 'Tofu'})
        WITH s
        MATCH (s)-[:SUPPLIES]->(otherProducts:Product)-[:PART_OF]->(c:Category)
        RETURN otherProducts.productName AS product, c.categoryName AS category
    """,
    "query_4": """
        MATCH (c:Customer)-[:PURCHASED]-(o:Order)-[:ORDERS]-(p:Product)
        WHERE p.productName = 'Tofu' AND c.country IN ['UK', 'Germany']
        AND NOT EXISTS {
            MATCH (c)-[:PURCHASED]-(order:Order)-[:ORDERS]-(product:Product)
            WHERE product.productName = 'Chai'
        }
        RETURN c.contactName AS customer
    """,
    "query_5": """
        MATCH (c:Customer)-[:PURCHASED]-(o:Order)
        RETURN c.contactName AS customer, COUNT(o) AS orderCount
        ORDER BY orderCount DESC LIMIT 5
    """,
    "query_6": """
        MATCH (c:Customer)
        WHERE NOT EXISTS {
            MATCH (c)-[:PURCHASED]-(:Order)
        }
        RETURN c.contactName AS customer
    """,
    "query_7": """
        MATCH (c:Customer)-[:PURCHASED]-(o:Order)-[:ORDERS]-(p:Product)
        RETURN c.contactName AS customer, o.orderDate AS orderDate, COLLECT(p.productName) AS products
        ORDER BY o.orderDate ASC LIMIT 1
    """,
    "query_8": """
        MATCH (s:Supplier)-[:SUPPLIES]-(p:Product)-[:PART_OF]-(c:Category)
        RETURN s.companyName AS supplier, c.categoryName AS category, COUNT(p) AS productCount
    """,
    "query_9": """
        MATCH (c:Customer)-[:PURCHASED]-(o:Order)-[:ORDERS]-(p:Product)-[:PART_OF]-(cat:Category {categoryName: 'Seafood'})
        WITH c, COUNT(o) AS orderCount
        WHERE orderCount >= 10
        RETURN c.contactName AS customer, orderCount
    """,
    "query_10": """
        MATCH (cat:Category)-[:PART_OF]-(p:Product)-[:ORDERS]-(o:Order)
        WITH cat, COUNT(p) AS productCount, COUNT(o) AS orderCount
        WHERE productCount > 10
        RETURN cat.categoryName AS category, orderCount
        ORDER BY productCount DESC
    """,
    "query_11": """
        MATCH (s:Supplier)-[:SUPPLIES]-(p:Product)
        RETURN s.country AS country, COUNT(p) AS productCount
    """,
    "query_12": """
        MATCH (c1:Customer)-[:PURCHASED]-(o1:Order)-[:ORDERS]-(p:Product),
              (c2:Customer)-[:PURCHASED]-(o2:Order)-[:ORDERS]-(p)
        WHERE c1 <> c2
        WITH c1, c2, COLLECT(DISTINCT p.productName) AS commonProducts
        RETURN c1.contactName AS customer1, c2.contactName AS customer2, SIZE(commonProducts) AS commonProductCount
        ORDER BY commonProductCount DESC LIMIT 1
    """,
    "query_13": """
        MATCH (p1:Product)-[:ORDERS]-(o:Order)-[:ORDERS]-(p2:Product)
        WHERE p1 <> p2
        WITH p1, p2, COUNT(DISTINCT o) AS orderCount
        WHERE orderCount >= 3
        RETURN p1.productName AS product1, p2.productName AS product2
    """,
    "query_14": """
        MATCH (s:Supplier {country: 'Germany'})-[r:SUPPLIES*..4]-(other:Supplier {country: 'Germany'})
        RETURN s.companyName AS supplier1, other.companyName AS supplier2
    """,
    "query_15": """
        MATCH (c1:Customer), (c2:Customer)
        WHERE c1.contactName STARTS WITH 'S' AND c2.contactName STARTS WITH 'S' AND c1 <> c2
        MATCH path=shortestPath((c1)-[*]-(c2))
        RETURN c1.contactName AS customer1, c2.contactName AS customer2, LENGTH(path) AS pathLength
        ORDER BY pathLength ASC
    """
}




def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [record.data() for record in result]



results = {name: run_query(query) for name, query in queries.items()}


with open("results.json", "w") as file:
    json.dump(results, file, indent=4)

print("Results have been saved to results.json")


driver.close()
