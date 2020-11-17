docker build -t dgguilherme /home/busercamp/guilherme
docker stop dgguilherme
docker rm dgguilherme
docker run -d -p 8003:8000 --name=dgguilherme \
	-v /home/busercamp/guilherme/dbdata:/dbdata \
	--env-file=/home/busercamp/guilherme/dg.properties \
	dgguilherme \
	./start_prod.sh