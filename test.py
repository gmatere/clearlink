from neo4j.v1 import GraphDatabase
uri = "bolt://im-interview-test-8d5jfp.clearlinkdata.com:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "5T\z8kV#n!E/a{'7"))


with open("/home/osboxes/Desktop/mvc.data") as f:
    next(f)
    with driver.session() as session:
        for line in f:
            a = line.split('\t')
            print a
            result = session.run(
                "MERGE (r:Rid {id:'" + a[1] + "' }) MERGE (c:Cid { id: '" + a[2] + "'})  CREATE UNIQUE  (r)-[:HAS]->(c);")
            print a




with open("/home/osboxes/Desktop/moc.data") as f:
    next(f)
    with driver.session() as session:
        for line in f:
            a = line.split('\t')
            print a
            result = session.run(
                "MERGE (o:Oid {id:'" + a[1] + "' }) MERGE (c:Cid { id: '" + a[2] + "'})  CREATE UNIQUE  (o)-[:HAS]->(c);")
            print a



