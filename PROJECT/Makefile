# Define a list of input KRA files
DEPENDENCIES := $(wildcard pg*.kra)

TARGETS := $(foreach file, $(DEPENDENCIES), $(shell printf "out/pg%03d.png" $(shell echo $(file) | sed 's/pg\([0-9]\+\)\.kra/\1/')))

all: $(TARGETS)

.PHONY: all

define dynamic_rule 
TARGET := $$(shell printf "out/pg%03d.png" $$(shell echo $(1) | sed 's/pg\([0-9]\+\)\.kra/\1/'))
$$(info $$(TARGET))
$$(TARGET): $(1)
	echo $$< | sed 's/pg\([0-9]\+\)\.kra/\1/' | xargs python3 ../process.py $$(shell pwd)

endef

$(foreach DEPENDENCY, $(DEPENDENCIES), $(eval $(call dynamic_rule,$(DEPENDENCY))))

