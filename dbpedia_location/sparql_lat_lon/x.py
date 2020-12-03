from SPARQLWrapper import SPARQLWrapper, JSON
loc_uri=''
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql = SPARQLWrapper(endpoint)
query = '''PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
    SELECT DISTINCT ?label ?subject  ?lat ?long WHERE {
    ?subject geo:lat ?lat.
    ?subject geo:long ?long.
    ?subject rdfs:label ?label.
    FILTER ((?sa = <http://dbpedia.org/resource/Germany> || ?subject = <http://dbpedia.org/resource/Germany>)).
    } LIMIT 10000 OFFSET 10000}'''

sparql.setReturnFormat(JSON)
results = sparql.query().convert()['results']['bindings']
print(results)

# for result in results:
#     print(result)

