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
PERM_DIR = permutations
NON_DETERM_FOLDER = nondeterministic-programs

TEST_DIRS = C++


GCC_DIR = gcc/libstdc++v3/testsuite/30_threads/
SELECT_GCC_DIR = relevant_tests_from_gcc
LANGUAGE_PROJECT = ..
RUNFCT := $(shell find ../.. -name "CIVIC-Runfct" -type f | sort | head -n 1)
# .PHONY: 
# run, create_table_determ_tests

all: clone_gcc_tests test
# un_determ

# run_determ:
# 	if [ -z "$$(ls -A $(DATA_FOLDER)/runs)" ]; then \
# 		$(PYTHON) $(D_SCRIPT) $(DATA_FOLDER) $(NUMBER_ITERATIONS) $(THREAD_POOL_SIZE) $(INPUT_FOLDER) $(DOCKERFILE) $(REGEN_FUNCONS); \
# 	fi

# force_run_determ:
# 	$(PYTHON) $(D_SCRIPT) $(DATA_FOLDER) $(NUMBER_ITERATIONS) $(THREAD_POOL_SIZE) $(INPUT_FOLDER) $(DOCKERFILE) $(REGEN_FUNCONS); \

# create_table_determ_tests:
# 	$(PYTHON) $(TABLE_SCRIPT) $(RUNS_FOLDER) $(TEX) $(INPUT_FOLDER); \

create_permutations:
	$(PYTHON) scripts/create_permutations.py perm $(PERM_DIR); \

run_permutations: create_permutations
	$(PYTHON) scripts/run_tests.py $(REGEN_FUNCONS) $(DOCKERFILE) $(DATA_FOLDER) $(RUNFCT) $(PERM_DIR) -t $(THREAD_POOL_SIZE); \

test: clean run_gcc_tests run_permutations
	$(PYTHON) scripts/run_tests.py $(REGEN_FUNCONS) $(DOCKERFILE) $(DATA_FOLDER) $(RUNFCT) $(TEST_DIRS) -t $(THREAD_POOL_SIZE); \

# run_non_determ:
# 	$(PYTHON) scripts/run-nondeterministic.py 10 $(NON_DETERM_FOLDER) $(DOCKERFILE) $(REGEN_FUNCONS) $(TEX); \

clone_gcc_tests:
	if [ ! -d "$(GCC_DIR)" ]; then \
		svn export https://github.com/gcc-mirror/gcc/trunk/libstdc++-v3/testsuite/30_threads $(GCC_DIR); \
	fi
# $(PYTHON) scripts/preprocessor.py $(GCC_DIR)

select_gcc_tests:
	if [ ! -d "$(SELECT_GCC_DIR)" ]; then \
		$(PYTHON) scripts/select_relevant_tests_from_gcc.py $(LANGUAGE_PROJECT) $(SELECT_GCC_DIR); \
	fi

run_gcc_tests: clone_gcc_tests select_gcc_tests
	$(PYTHON) scripts/preprocessor.py $(SELECT_GCC_DIR)



# to_fct_gcc_tests:
# 		$(PYTHON) scripts/to_funcons_relevant_tests_from_gcc.py $(SELECT_GCC_DIR) $(REGEN_FUNCONS); \

unbuild: 
	rm -rf $(GCC_DIR)
	rm -rf $(SELECT_GCC_DIR)

# build:

clean:
# rm -rf $(DATA_FOLDER)/runs/*
	for dir in $(TEST_DIRS); do \
		find "$$dir" -type f \( -name "*.civ" -o -name "*.fct" -o -name "*.output" -o -name "*.debug" -o -name "*.json" \) -delete; \
	done
	rm -rf $(PERM_DIR)