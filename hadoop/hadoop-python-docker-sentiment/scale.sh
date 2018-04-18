if [ $# -ne 1 ]; then
    echo "unknown number of workers, using 1 as default"
    cp ./docker-compose-template.yml ./docker-compose.yml
    exit 0
fi

cp ./docker-compose-template.yml ./docker-compose.yml
for i in $(seq 2 $1)
do
echo -e "  worker"$i":\n\
    build: ./hadoop-worker\n\
    container_name: \"worker"$i"\"\n\
    ports:\n\
      - \"$((9900+$i)):9864\"\n\
      - \"$((8040+$i)):8042\""\
>>./docker-compose.yml
done
echo "docker-compose.yml created with #worker "$1
exit 0