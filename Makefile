VENV := venv
PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python

.PHONY: venv install run debug clean lint lint-strict

venv:
	@if [ ! -d "$(VENV)" ]; then \
		python3 -m venv "$(VENV)"; \
	fi

install: venv requirements.txt
	@$(PIP) install -qq -r requirements.txt

run: venv install
	@$(PYTHON) a_maze_ing.py

debug: venv install
	@$(PYTHON) -m pdb a_maze_ing.py

clean:
	@find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	@rm -rf .mypy_cache
	@rm -rf .DS_Store
	@rm -rf "$(VENV)"

lint:
	python3 -m flake8 .
	python3 -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	python3 -m flake8 .
	python3 -m mypy . --strict


