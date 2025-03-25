SERVICE_DIR := src
TXT_BOLD := \e[1m
TXT_OCEAN := \e[36m
TXT_RESET := \e[0m

setup:
	@poetry install --no-root

lint:
	@printf "${TXT_BOLD}${TXT_OCEAN}=========================== RUFF ==============================${TXT_RESET}\n"
	@poetry run ruff check --fix --show-fixes --exit-non-zero-on-fix .
	@printf "${TXT_BOLD}${TXT_OCEAN}=========================== MYPY ==============================${TXT_RESET}\n"
	@poetry run mypy $(SERVICE_DIR)/

format:
	@poetry run ruff format $(SERVICE_DIR)/ tests/

test:
	@poetry run pytest tests --cov $(SERVICE_DIR) -vv
