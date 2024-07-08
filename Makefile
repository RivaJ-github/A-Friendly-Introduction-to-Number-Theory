MAIN=main
LATEX=xelatex
RM=rm -f
OUTPUT_DIR=dist

.SUFFIXES: .tex

all:
ifdef OUTPUT_DIR
	if not exist "$(OUTPUT_DIR)" mkdir "$(OUTPUT_DIR)"
	$(LATEX) -output-directory=$(OUTPUT_DIR) $(MAIN)
else
	OUTPUT_DIR=./
endif

clean:
	cd $(OUTPUT_DIR) && $(RM) *.log *.aux *.dvi *.lof *.lot *.toc *.bbl *.blg

clean-pdf:
	cd $(OUTPUT_DIR) && $(RM) $(MAIN).pdf

clean-all: clean clean-pdf