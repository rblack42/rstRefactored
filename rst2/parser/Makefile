# Makefile for rst2 parser

EBNF	= rst2.ebnf
TARGET	= rst2Parser.py

all:	$(TARGET)

$(TARGET):		$(EBNF)
	grako -o $@ $< 2>&1

test:	$(TARGET)
	python  rst2_parser.py tests/test.rst --trace

clean:
	-@rm -f $(TARGET) *.pyc
