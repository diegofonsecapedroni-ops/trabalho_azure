IMAGE=ghcr.io/diegofonsecapedroni-ops/trabalho_azure
CONTAINER=minha-api-python

build:
	docker build -t $(IMAGE):latest .

push:
	docker push $(IMAGE):latest

pull:
	docker pull $(IMAGE):latest

deploy:
	docker pull $(IMAGE):latest
	docker rm -f $(CONTAINER) || true
	docker run -d \
		--name $(CONTAINER) \
		--restart unless-stopped \
		-p 127.0.0.1:8000:8000 \
		$(IMAGE):latest

logs:
	docker logs -f $(CONTAINER)

stop:
	docker rm -f $(CONTAINER)
