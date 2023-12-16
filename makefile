rmcache:
	rm -rd __pycache__

rmlog:
	rm log/*

clean:
	make rmcache
	make rmlog
