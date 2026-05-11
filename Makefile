DRAWIO ?= drawio
BUILD_DIR := build
DOCS_DIR := docs
DIST_DIR := dist
PLUGIN_SRC := plugin
PLUGIN_NAME := ai-pdlc-plugin
PLUGIN_VERSION := $(shell python3 -c "import json; print(json.load(open('plugin/.claude-plugin/plugin.json'))['version'])" 2>/dev/null || echo "dev")
PLUGIN_OUT := $(DIST_DIR)/$(PLUGIN_NAME)
SOURCES := $(wildcard *.drawio)
PNGS := $(patsubst %.drawio,$(BUILD_DIR)/%.png,$(SOURCES))
SVGS := $(patsubst %.drawio,$(BUILD_DIR)/%.svg,$(SOURCES))
DOC_PNGS := $(patsubst %.drawio,$(DOCS_DIR)/%.png,$(SOURCES))

.PHONY: all png svg docs-png clean list package package-zip validate-links help

all: png svg docs-png

docs-png: $(DOC_PNGS)

$(DOCS_DIR)/%.png: $(BUILD_DIR)/%.png
	mkdir -p $(DOCS_DIR)
	cp $< $@

png: $(PNGS)

svg: $(SVGS)

$(BUILD_DIR)/%.png: %.drawio | $(BUILD_DIR)
	$(DRAWIO) --export --format png --scale 2 --output $@ $<

$(BUILD_DIR)/%.svg: %.drawio | $(BUILD_DIR)
	$(DRAWIO) --export --format svg --output $@ $<

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

list:
	@echo "Sources: $(SOURCES)"
	@echo "PNG targets: $(PNGS)"
	@echo "SVG targets: $(SVGS)"

clean:
	rm -rf $(BUILD_DIR) $(DIST_DIR)

# ---- Plugin packaging ----

# Materialize plugin/ into dist/ai-pdlc-plugin/ with symlinks dereferenced into real copies.
# Uses rsync -aL so content/* (which is symlinks in the source repo) becomes real files in the output.
package: validate-links
	@rm -rf $(PLUGIN_OUT)
	@mkdir -p $(DIST_DIR)
	rsync -aL --exclude='.DS_Store' $(PLUGIN_SRC)/ $(PLUGIN_OUT)/
	@echo ""
	@echo "Materialized plugin at $(PLUGIN_OUT) (version $(PLUGIN_VERSION))"
	@find $(PLUGIN_OUT) -type l | grep -q . && { echo "ERROR: symlinks remain in $(PLUGIN_OUT):"; find $(PLUGIN_OUT) -type l; exit 1; } || echo "Verified: no symlinks in materialized plugin."
	@$(MAKE) --no-print-directory _validate-materialized

# Zip the materialized plugin for distribution.
package-zip: package
	cd $(DIST_DIR) && zip -rq $(PLUGIN_NAME)-$(PLUGIN_VERSION).zip $(PLUGIN_NAME)
	@echo "Zipped: $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION).zip"

# Validate handbook links before building the plugin (against live content in the repo root).
validate-links:
	@python3 scripts/validate_links.py .

# Validate links in the materialized plugin (symlink-free copy).
_validate-materialized:
	@python3 scripts/validate_links.py $(PLUGIN_OUT)/skills/ai-pdlc-navigator/content

help:
	@echo "Common targets:"
	@echo "  make                Build PNG+SVG from .drawio and copy PNG into docs/"
	@echo "  make docs-png       Refresh docs/*.png (embedded in README)"
	@echo "  make package        Materialize plugin/ → dist/$(PLUGIN_NAME)/ with symlinks dereferenced"
	@echo "  make package-zip    Build package and zip it for distribution"
	@echo "  make validate-links Check that activity links in AI-PDLC-linear-flow.md resolve"
	@echo "  make clean          Remove build/ and dist/"