# Usage: make setup
# Description: Installs the specified versions of Python and Poetry using asdf, and installs project dependencies with Poetry.
# Requires: .tool-versions file with specified Python and Poetry versions.
setup:
	asdf plugin-add python
	asdf plugin-add poetry https://github.com/asdf-community/asdf-poetry.git
	asdf install
	poetry self add poetry-dotenv-plugin	
	poetry install

autofix:
	poetry run ruff check --fix house jobs tests
	poetry run ruff format house jobs tests

# Usage: make format
# Description: Fix imports and indentation
# Requires: .tool-versions file with specified Python and Poetry versions.
format:
	poetry run ruff check house jobs tests
	poetry run ruff format --check house jobs tests

# Usage: make lint
# Description: Runs lint checks
# Requires: .tool-versions file with specified Python and Poetry versions.
lint:
	poetry run mypy house jobs tests
	

# Usage: make test
# Description: Run pytests
# Requires: .tool-versions file with specified Python and Poetry versions.
test:
	poetry install --all-extras
	poetry run coverage run -m pytest
	poetry run coverage report -m


# Usage: build_docker
build_docker:
	docker build -f docker/Dockerfile -t house .	

# Usage: run_server
run_server: build_docker
	docker run \
		-p 80:80 \
		house