# Hush Line Development

👋 Welcome to the Hush Line Development setup guide. This document provides detailed instructions for configuring your local development environment across Mac, Windows, and Linux systems. It includes specific steps for installing dependencies, cloning the repository, and initiating a local server using the included `Makefile`. The guide also covers utilizing tests, linters, and formatters to ensure code integrity and consistency. Follow these instructions to prepare your machine for Hush Line development 👇.

<img src="https://github.com/scidsg/hushline/assets/28545431/3108811e-226e-4451-9793-c893da96184c" width="66%">

### Development environment

Hush Line is written in Python. To ensure code integrity and consistency, we use [Ruff](https://docs.astral.sh/ruff/) for linting and [mypy](https://www.mypy-lang.org/) for static type checking.

The recommended development environment is [Visual Studio Code](https://code.visualstudio.com/) with the following extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [Mypy](https://marketplace.visualstudio.com/items?itemName=matangover.mypy)

You need Python, Poetry, and pipx. If you're on macOS, install these with [Homebrew](https://brew.sh/):

```sh
brew install python poetry pipx
```

Using pipx, install Python packages required for linting and static type checking:

```sh
pipx install ruff
pipx install mypy
```

### Getting started

Clone the Hush Line code:

```sh
git clone https://github.com/scidsg/hushline.git
cd hushline
```

Install Poetry dependencies:

```sh
poetry install
```

Run the database migrations:

```sh
poetry run migrate
```

Run the app in debug mode:

```sh
poetry run make run
```

Run the tests:

```sh
poetry run make test
```

Run the linters:

```sh
poetry run make lint
```

Format the code:

```sh
poetry run make fix
```
