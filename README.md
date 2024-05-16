This project is for POC

Edit your /etc/host file
```bash 
127.0.0.1 db.hyetheater.com
127.0.0.1 api.hyetheater.com
127.0.0.1 app.hyetheater.com
```

# Docker Compose 
Start development env
```bash
docker-compose up
```

Connect to MySQL
```bash
mysql -h db.hyetheater.com  -P 3306 --user=admin --password=password1
docker exec -it mysql mysql --user=admin --password=password1
```

Clean the persistent valume
```bash
docker ps -a  --format json | gojq '{ID, Image}' | gojq -s . | gojq -r '.[] | select(.Image == "hyetheater-db" or .Image == "hyetheater-api" or .Image == "hyetheater-ui") | .ID' | xargs docker rm; docker volume rm hyetheater_mysql-data
```

# UI
Imital React App cration. 
We need to run `npx create-react-app ui` on the root folder


Once we do not have CI 
React 
HOST=app.hyetheater.com npm start 
npm start


# API
in api Folder
pip3 install Flask

Run python server
```bash
export MYSQL_HOSTNAME=db.hyetheater.com
export MYSQL_DATABASE=db
export MYSQL_USER=admin
export MYSQL_PASSWORD=password1

python3 setup.py
```
Goto: http://api.hyetheater.com:5000/members


# DB
It is located on db folder
init.sql file is running sql commanda when the mysql inital configuration. 