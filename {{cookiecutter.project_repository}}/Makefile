###############################################################################
# Environment
###############################################################################

.PHONY: compile init update install-dev install-prod git-hooks update-deps compile-deps

init: install-dev git-hooks

update: update-deps install-dev

install-dev:
	npm install --production=false

install-prod:
	npm install --production

git-hooks:
	pre-commit install --install-hooks --hook-type pre-commit
	pre-commit install --install-hooks --hook-type pre-push

update-deps:
	npx npm-check-updates --upgrade
	pre-commit autoupdate --freeze

compile-deps:
	npm install --save-dev jest typescript ts-jest @types/jest

compile:
	npx tsc


###############################################################################
# Code
###############################################################################

.PHONY: test coverage report lint

test: lint
	npm run test -- --coverage

coverage:
	npm run coverage

report: coverage
	firefox coverage/lcov-report/index.html

lint:
	echo "TODO: linter"
