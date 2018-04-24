local_test: test_env
	heroku local

local: deploy_env
	heroku local

test_env:
	cp testing-roboto.env .env

deploy_env:
	cp mr-roboto.env .env
