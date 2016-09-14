from .models import *

def load_gpx(request, track_file):
    from django.http import HttpResponse
    file_parser("tracking/paths/est/"+track_file+".gpx")
    return HttpResponse("ok")
    

def file_parser(filename):
    from xml.etree import ElementTree
    root = ElementTree.parse(filename).getroot()
    
    metadata = root[0]
    track = root[1]
    
    name = track[0].text
    descr = track[1].text
    points = track[2]
    
    #track = Track(id=name, descr=descr)
    track = Track(name=name, descr=descr)
    track.save()

    segments = []
    prev_coord = points[0].attrib
    prev_elev = points[0][0].text
    prev_pos = Position(latitude=prev_coord['lat'], longitude=prev_coord['lon'], elevation=prev_elev)
    prev_pos.save()
    for point in points[1:]:
        coord = point.attrib
        elev = point[0].text
        
        pos = Position(latitude=coord['lat'], longitude=coord['lon'], elevation=elev)
        pos.save()

        segment = Segment(begin=prev_pos, end=pos)
        segment.save()
        track.tracks.add(segment)

        segments.append(segment)
        prev_pos = pos

if __name__ == "__main__":
    filename = "paths/est/E101.gpx"
    

    file_parser(filename, descr=descr)
