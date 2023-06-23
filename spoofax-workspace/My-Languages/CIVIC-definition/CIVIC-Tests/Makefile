PYTHON = python3
D_SCRIPT = scripts/determ.py
TABLE_SCRIPT = scripts/determ_create_table.py
RUNS_FOLDER = data/runs
DATA_FOLDER = data
INPUT_FOLDER = perm1
THREAD_POOL_SIZE = 1
NUMBER_ITERATIONS = 4
DOCKERFILE = .
REGEN_FUNCONS = regen-funcons.sh
TEX = latex

TEST_DIRS = C++

.PHONY: run, create_table_determ_tests

all: test

run:
	if [ -z "$$(ls -A $(DATA_FOLDER)/runs)" ]; then \
		$(PYTHON) $(D_SCRIPT) $(DATA_FOLDER) $(NUMBER_ITERATIONS) $(THREAD_POOL_SIZE) $(INPUT_FOLDER) $(DOCKERFILE) $(REGEN_FUNCONS); \
	fi

force_run:
	$(PYTHON) $(D_SCRIPT) $(DATA_FOLDER) $(NUMBER_ITERATIONS) $(THREAD_POOL_SIZE) $(INPUT_FOLDER) $(DOCKERFILE) $(REGEN_FUNCONS); \

create_table_determ_tests:
	$(PYTHON) $(TABLE_SCRIPT) $(RUNS_FOLDER) $(TEX) $(INPUT_FOLDER); \

test:
	$(PYTHON) scripts/run_tests.py $(REGEN_FUNCONS) $(DOCKERFILE) $(TEST_DIRS); \

clean:
	rm -rf $(DATA_FOLDER)/runs/*