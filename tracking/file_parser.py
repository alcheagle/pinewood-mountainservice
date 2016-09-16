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

    #track_query = Track.objects.filter(name=name)
    #print(track_query.exists())
    #if track_query.exists():
    #    track = track_query[0]
    #else:
    track = Track(name=name, descr=descr)
    track.

    segments = []
    prev_coord = points[0].attrib
    prev_elev = points[0][0].text
    prev_pos = Position(latitude=prev_coord['lat'], longitude=prev_coord['lon'], elevation=prev_elev)
    prev_pos.save()
    for point in points[1:]:
        coord = point.attrib
        elev = point[0].text
        
        pos_query = Position.objects.filter(latitude=coord['lat'], longitude=coord['lon'], elevation=elev)
        print(pos_query)
        if pos_query.exists():
            pos = pos_query[0]
        else:
            pos = Position(latitude=coord['lat'], longitude=coord['lon'], elevation=elev)
            pos.save()

        segment_query = Segment.objects.filter(begin=prev_pos, end=pos)

        if segment_query.exists():
            segment = segment_query[0]
        else:
            segment = Segment(begin=prev_pos, end=pos)
            segment.save()
        track.tracks.add(segment)

        segments.append(segment)#FIXME check if there is already this segment in the track
        prev_pos = pos

if __name__ == "__main__":
    filename = "paths/est/E101.gpx"
    

    file_parser(filename, descr=descr)
