rmcache:
	rm -rd __pycache__

rmlog:
	rm log/*

clean:
	make rmlog
	make rmcache
