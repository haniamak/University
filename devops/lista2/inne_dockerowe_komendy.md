docker logs <container_id> - pokazuje logi z danego kontenera.
docker stop <container_id> - zatrzymuje działający kontener.
docker prune - usuwa wszystkie zatrzymane kontenery, te króre są 'running' nie zostaną usunięte.
docker exec -it <container_id> bash - pozwala na wejście do działającego kontenera i uruchomienie w nim powłoki bash.
docker volume create <volume_name> - tworzy nowy wolumen do przechowywania danych.
docker run -d -v <volume_name>:/data <image_name> - uruchamia kontener z podłączonym wolumenem do katalogu /data w kontenerze.
docker build -t <image_name> . - buduje obraz Dockera z pliku Dockerfile znajdującego się w bieżącym katalogu nadając mu tag <image_name>.

