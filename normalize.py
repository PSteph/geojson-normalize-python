#!/usr/bin/python
# normalize.py
import io, ast, sys
types = {
    "Point": 'geometry',
    "MultiPoint": 'geometry',
    "LineString": 'geometry',
    "MultiLineString": 'geometry',
    "Polygon": 'geometry',
    "MultiPolygon": 'geometry',
    "GeometryCollection": 'geometry',
    "Feature": 'feature',
    "FeatureCollection": 'featurecollection'
}


def normalize(gj):
    print (gj)
    if (not gj or not gj["type"]):
        return None

    type = types[gj["type"]]

    if not type:
        return None
    
    if type == 'geometry':
        return {
            "type": 'FeatureCollection',
            "features": [{
                "type": 'Feature',
                "properties": {},
                "geometry": gj
            }]
        }
    elif type == 'feature':
        return {
            "type": 'FeatureCollection',
            "features": [gj]
        }
    elif type == 'featurecollection':
        return gj

# test
if __name__ == "__main__":
    gj = {"type": "Point","coordinates": [125.6, 10.1]}
    print (normalize(gj))
#     print (str(sys.argv[1]))
#     data = ""
#     for line in open(str(sys.argv[1])):
#         print (line)
#     print (normalize( open(ast.literal_eval(str(sys.argv[1]))) ))