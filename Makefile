.PHONY: install run debug lint lint-strict build clean fclean

install:
	uv python install 3.10
	uv venv --python 3.10 .venv
	uv pip install --python .venv/bin/python -r requirements.txt
	uv pip install --python .venv/bin/python build

run:
	uv run Fly-in.py config.txt

debug:
	uv run python -m pdb Fly-in.py config.txt

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
		--disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

build:
	uv run python -m build

clean:
	rm -rf __pycache__ */__pycache__ .mypy_cache dist build *.egg-info

fclean: clean
	rm -rf .venv
