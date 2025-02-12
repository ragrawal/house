FROM docker1

# Copy the poetry.lock file and other applications to the working directory
COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .
COPY house house
COPY model.pkl .

# Install poetry
RUN pip install --upgrade pip \
    && poetry install --no-interaction --no-root
