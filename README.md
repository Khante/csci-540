# csci-540
## Advanced Databases Final Project

Run `docker-compose build` to update build.

Run `docker-compose up` to start project.

App should be visible on `localhost:<PORT>` or `0.0.0.0:<PORT>`

Mongo data will be saved locally under `/data/mongodb`

Services are visible to other services via docker networking, they can be reached at `<serviceName>:<PORT>`


## Current Services - service name, parent directory, (port), endpoints
- info, /games_api (5000)
	- `GET /games/<GAME_TITLE>`
	- `GET /consoles/<CONSOLE_NAME>`
	- `GET /genre/<GENRE_NAME>`
- reviews, /reviews_api (8080)
	- `GET /api/reviews/<GAME_TITLE>`
	- `POST /api/reviews/<GAME_TITLE>`
		- `data: {'review_text': String, 'review_score': Int}`
	- `GET /api/score/<GAME_TITLE>`
- news, /news_api (5001)
	- `GET /`
	- `GET/POST /subscribe/`
		- `data: {'name': String, 'channel': String}`
	- `GET/POST /publish/`
		- `data: {'name': String, 'channel': String, 'news': String}`
- mongo, /data (27017)
- redis, (6379)
- gateway, /server (8000)
