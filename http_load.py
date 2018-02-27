from neo4j.v1 import GraphDatabase
uri = "bolt://im-interview-test-8d5jfp.clearlinkdata.com:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "5T\z8kV#n!E/a{'7"))
with driver.session() as session:
    result = session.run("LOAD CSV WITH HEADERS FROM 'https://782160b8.ngrok.io/moc.data' AS line FIELDTERMINATOR '\t' Merge (o:Oid_id {id: line.oid}) Merge (c:Cid_id {id: line.cid}) MERGE (o)-[m:HAS]->(c) ;");

with driver.session() as session:
    result = session.run("LOAD CSV WITH HEADERS FROM 'https://782160b8.ngrok.io/mvc.data' AS line FIELDTERMINATOR '\t' Merge (r:Rid_id {id: line.rid}) Merge (c:Cid_id {id: line.cid}) MERGE (r)-[m:HAS]->(c) ;");
