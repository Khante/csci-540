# csci-540
Advanced Databases Final Project

Run `docker-compose build` to update build.

Run `docker-compose up` to start project.

App should be visible on `localhost:<PORT>` or `0.0.0.0:<PORT>`

Mongo data will be saved locally under `/data/mongodb`

Local directories are mounted inside the containers so you can make changes without having to rebuild.

Current Services - name, parent directory, (port)
- info, /games_api (5000)
- reviews, /reviews (8080)
- mongo, /data (27017)
- gateway, /server (8000)
