#!/bin/bash
git clone https://github.com/mcondorimendoza/Git-GroupOmicron2

echo "FROM python" >> Dockerfile
echo "COPY ./Git-GroupOmicron2/2a-meraki.py /home/2a-meraki.py" >> Dockerfile
echo "COPY ./Git-GroupOmicron2/b_dnacenter.py /home/b_dnacenter.py" >> Dockerfile
echo "COPY ./Git-GroupOmicron2/c-csr100v.py /home/c-csr100v.py" >> Dockerfile
echo "COPY ./Git-GroupOmicron2/d_Room-Devnet-GroupOmicron.py /home/d_Room-Devnet-GroupOmicron.py" >> Dockerfile
echo "RUN pip3 install requests" >> Dockerfile
echo "RUN python -m pip install urllib3" >> Dockerfile
echo "RUN pip3 install jsonlib" >> Dockerfile

docker build -t docker_groupomicron2 .
docker run -t -d --name docker_groupomicron2running docker_groupomicron2
docker exec -it docker_groupomicron2running python3 /home/2a-meraki.py
docker exec -it docker_groupomicron2running python3 /home/b_dnacenter.py
docker exec -it docker_groupomicron2running python3 /home/c-csr100v.py
docker exec -it docker_groupomicron2running python3 /home/d_Room-Devnet-GroupOmicron.py
#Token de webex por 12 horas OTk0NzE3MjAtNDVkMi00NGRmLWFlMjMtMDQ2ZDYyN2U2ZGE4OTUwMzNhMzgtMzZk_P0A1_242b07f9-2b66-4cc2-9f6c-81cb45ce0742
