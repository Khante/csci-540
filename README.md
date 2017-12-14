# csci-540
## Advanced Databases Final Project

A project built around the microservices architecture that provides video-game related data services.  Currently provides the following services:
- Game Information:  Allows the user to request data by video game title, as well as list all available platforms or genres in the game database.  Database is based off of the [MobyGames](http://www.mobygames.com/) database.  No data is included as part of this project, MobyGames has an excellent API if you are in need of real data!
- Game Reviews:  Allows the user to post new reviews for a video game as well as fetch all reviews for a title and fetch an average score for a title.
- Game News:  Uses Redis to provide endpoints for a publish-subscribe system where a user can subscribe to a channel and receive news published to that channel.  Currently no integrations with the actual database.

## Requirements
* Docker

## Running Instructions

Run `docker-compose build` to update build.

Run `docker-compose up` to start project.

App should be visible on `localhost:<PORT>` or `0.0.0.0:<PORT>`.  The gateway service provides a user interface for interacting with the other services at `http://localhost:8000`.  All services are currently exposed to the localhost however, so all endpoints should be reachable directly.

Mongo data will be saved locally under `/data/mongodb`, database files can be copied into this directory and should be automatically mounted to the container.

Services are visible to other services via docker networking, they can be reached internally at `<serviceName>:<PORT>`


## Current Services - service name, parent directory, (exposed port), endpoints
- info, /games_api (5000)
	- `GET /games/<GAME_TITLE>`
	- `GET /consoles/<CONSOLE_NAME>`
	- `GET /genre/<GENRE_NAME>`
	- `GET /genres`
	- `GET /consoles`
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
	- `GET /subscriptions/`
	- `GET /publications/<GAME_TITLE>`
- mongo, /data (27017)
- redis, (6379)
- gateway, /server (8000)
