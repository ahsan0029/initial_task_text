from SPARQLWrapper import SPARQLWrapper, JSON
from typing import Optional, Union

def get_location_types(loc_uri: str="http://dbpedia.org/resource/Germany", endpoint: str = 'http://dbpedia.org/sparql') :
    """
       Retrieve types for location URIs using DBPedia.

       loc_uri: str
           URI of the location.
       endpoint: str, 'http://dbpedia.org/sparql' by default
           DBPedia SPARQL endpoint to use.
       """
    sparql = SPARQLWrapper(endpoint)

    query = '''PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
    select DISTINCT ?subject ?type ?lat  
        where{ ?subject owl:same As ?sa.
               ?subject rdf:type ?type.
               ?subject geo:lat ?lat.
               FILTER ((?sa = <http://dbpedia.org/resource/Germany> || ?subject = <http://dbpedia.org/resource/Germany>)). }
       }}'''

    sparql.setQuery(query.format(loc_uri, loc_uri))

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()['results']['bindings']
    print(results)
    if len(results) == 0:
        return None
    return [r['type']['value'] for r in results]
  
 