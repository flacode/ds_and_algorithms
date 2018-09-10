# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def get_min_right(segments):
	min_right = segments[0]
	for s in segments:
		if s.end < min_right.end:
			min_right = s
	return min_right.end

def includes_point(segment, point):
	points = list(range(segment.start, segment.end + 1))
	return point in points
	

def optimal_points(segments):
	points = []
	while(segments):
		if len(segments) == 0:
			return points
		point = get_min_right(segments)
		i = 0
		while i < len(segments):
			if includes_point(segments[i], point):
				del segments[i]
			else:
				i = i+1
		points.append(point)
	return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
