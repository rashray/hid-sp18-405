DESTDIR=Results
worker=1

dest:
	mkdir -p $(DESTDIR)

all: build start run get down

scale:
	@echo "make docker-compose.yml with 1 master and $(worker) workers"
	./scale.sh $(worker)

build:scale 
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-base:latest hadoop-base
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-master:latest hadoop-master
	docker build -t minchen57/hadoop-docker-python-sentiment-compose-worker:latest hadoop-worker
	docker-compose build


start:
	docker-compose up -d
	echo "http://localhost:9870 for HDFS"
	echo "http://localhost:8088 for YARN"

shell: start
	echo "Now interactive shell for master..."
	docker exec -it master bash

run:
	docker exec master /etc/runall.sh

get: clean dest
	@echo "Getting the results..."
	docker cp master:/cloudmesh/python/output_pos_tagged ./$(DESTDIR)
	docker cp master:/cloudmesh/python/output_neg_tagged ./$(DESTDIR)
	docker cp master:/cloudmesh/python/log.txt ./$(DESTDIR)
	cp docker-compose.yml ./$(DESTDIR)
	

down:
	docker-compose down


clean:
	rm -rf $(DESTDIR)
	rm docker-compose.yml

		