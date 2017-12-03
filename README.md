# csci-540
Advanced Databases Final Project

Run `docker-compose build` to update build.

Run `docker-compose up` to start project.

App should be visible on `localhost:<PORT>` or `0.0.0.0:<PORT>`

Mongo data will be saved locally under `/data/mongodb`

Local directories are mounted inside the containers so you can make changes without having to rebuild.

Current Services (port)
- Game Information (5000)
- Game Reviews (8080)
- MongoDB (27017)