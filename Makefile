RUN = poetry run
PROJ = schemasheets

all: project

test: project

source/rda-crosswalk.tsv:
	curl -L -s 'https://docs.google.com/spreadsheets/d/1mu9iWZxX4DvtklLIQgEloM8oZfzZdzfJ/export?format=tsv&gid=1108662376' > $@


project: source/rda-crosswalk.tsv
	$(RUN) linkml2project $< -d schema

crosswalk.yaml: schema/rda.yaml
	cp $< $@

schema/mappings/rda.sssom.tsv: crosswalk.yaml
	$(RUN) gen-sssom  $< -o $@

gendocs:
	$(RUN) gen-markdown -d stage-docs  crosswalk.yaml && \
	mv stage-docs/index.md docs/schema.md && mv stage-docs/*md docs/


docserve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy
