# Makefile: Compile all .c files in current directory to executable files with same name (no extension)

# Compiler
CC := gcc

# Compiler flags (adjust as needed)
CFLAGS := -Wall -Wextra -O2      # Enable common warnings, optimization level O2
# CFLAGS += -g                    # Uncomment for debugging, add debug information

# Automatically get all .c files in current directory
SOURCES := $(wildcard *.c)

# Generate target executable names from source files (remove .c extension)
TARGETS := $(SOURCES:.c=)

# Default target: compile all executables
all: $(TARGETS)

# Rule: how to generate executable from .c file
# $@ represents target name (e.g., hello), $^ represents all dependencies (e.g., hello.c)
$(TARGETS): %: %.c
	$(CC) $(CFLAGS) $^ -o $@

# Clean generated executables and temporary files
clean:
	rm -f $(TARGETS)

# Declare phony targets
.PHONY: all clean