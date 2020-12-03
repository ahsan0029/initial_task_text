from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
    SELECT DISTINCT ?lat ?long ?type ?sameAs 
    WHERE {<http://dbpedia.org/resource/Austria>
            geo:lat ?lat;
            geo:long ?long;
            rdf:type ?type;
            owl:sameAs ?sameAs }
    
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)
for result in results["results"]["bindings"]:
    print(result)


# select DISTINCT ?lat ?long ?type ?sameAs   { <http://dbpedia.org/resource/Germany> geo:lat ?lat ; geo:long ?long ; rdf:type ?type ; owl:sameAs ?sameAs}    

