## This project is for POC:

Edit your /etc/host file
```bash 
127.0.0.1 db.hyetheater.com
127.0.0.1 api.hyetheater.com
127.0.0.1 app.hyetheater.com
```

## Docker Compose 
Start development env
```bash
docker-compose up
```

## DB
It is located on db folder
init.sql file is running sql commanda when the mysql inital configuration. 

![DB Architecture](https://github.com/roybay/hyetheater/blob/master/db_schema.png?raw=true)

Connect to MySQL
```bash
mysql -h db.hyetheater.com  -P 3306 --user=admin --password=password1
docker exec -it mysql mysql --user=admin --password=password1
```

Clean the persistent valume
```bash
docker ps -a  --format json | gojq '{ID, Image}' | gojq -s . | gojq -r '.[] | select(.Image == "hyetheater-db" or .Image == "hyetheater-api" or .Image == "hyetheater-ui") | .ID' | xargs docker rm; docker volume rm hyetheater_mysql-data
```

## API
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

or

Connect via docker-compose
```bash
curl http://api.hyetheater.com:8000/members
```

## UI
Imital React App cration. 
We need to run `npx create-react-app ui` on the root folder


Once we do not have CI 
React 
HOST=app.hyetheater.com npm start 
npm start

Connect via docker-compose
[http://localhost](http://localhost)

#### WebSite Structure:
The website is going to have different pages focusing Armenian Culture
1.  Library hold the list of Armenian playbooks
    - Individual playbook details with different sections
        - Summary
        - Characters list 
          - list of Individual actors played that particular character
        - Different versions 
        - Authors 
        - Period
2. List of Theater Groups
    - Individual Theater Gorup Page
      - Summary of group mission location
      - List of plays cronological order
        - Individual play detail
          - List of Characters with who performs
          - Director
          - Photo Galery
          - Video
3. List of Artists
   - Individual Artist Page
     - Biography
     - Play performed
     - Member of theater groups
4. About Us
   - Contact Us
   - Request forms to contribute the website 
     Approved user will be grant access to profile page of theater-groups, scripts, plays, or artists page to manage, add or modify