charstar: FORCE
	g++ charstar.cpp -o charstar

scope: FORCE
	g++ scope.cpp -o scope

map: FORCE
	g++ map.cpp usemap.cpp -o map

parse:
	(cd parse_python && make parse)

clean:
	rm -f charstar
	rm -f scope
	rm -f usemap
	rm -f map
	(cd parse_python && make clean)

FORCE:
