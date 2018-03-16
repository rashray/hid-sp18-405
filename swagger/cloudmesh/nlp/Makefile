
SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=nlp.yaml
DESTDIR=server/nlp/flaskConnexion
CREATED=server
NLPDIR=nlps

all: service start 
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

service: dest
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython3=true

	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cd $(NLPDIR) && pip install -r requirements.txt && python setup.py install
	
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 

start:  
	cd $(DESTDIR) && python -m swagger_server

test:
	curl http://localhost:8080/nlp/all/Tim%20Cook%20is%20the%20CEO%20of%20Apple.
	curl http://localhost:8080/nlp/pos/Tim%20Cook%20is%20the%20CEO%20of%20Apple.
            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -rf $(CREATED)

container:

	sudo docker build -t cloudmesh-nlp .
	sudo docker run -p 8080:8080 cloudmesh-nlp 