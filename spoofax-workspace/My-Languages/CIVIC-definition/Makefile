FOLDERS := $(wildcard *-cbs)

all: summary

summary: $(FOLDERS)
	python3 summary.py > summary

.PHONY: all summary

$(FOLDERS):
	@$(MAKE) summary