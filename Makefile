BROWSER=w3m

SERVICE6=service6
DOC_DIR=doc

DOC_SOURCES=$(wildcard s6*/doc/s6*.html)
DOC_TARGETS=$(addprefix $(DOC_DIR)/,$(basename $(notdir $(DOC_SOURCES))))

all: $(DOC_DIR) $(DOC_TARGETS)

$(DOC_DIR):
	mkdir $(DOC_DIR)

doc/%: s6/doc/%.html
	$(BROWSER) -dump $< > $@

doc/%: s6-rc/doc/%.html
	$(BROWSER) -dump $< > $@

install: all
	install $(SERVICE6) /usr/bin
	install -d /usr/share/doc/service6
	install $(DOC_DIR)/* /usr/share/doc/service6
	install bash_completion.d/service6 /etc/bash_completion.d

uninstall:
	rm -f /usr/bin/service6
	rm -rf /usr/share/doc/service6
	rm -f /etc/bash_completion.d/service6

clean:
	rm -rf $(DOC_DIR)
