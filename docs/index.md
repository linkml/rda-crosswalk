# RDA Schema crosswalk

This is in experiment translating the RDA Crosswalk to [LinkML](https://linkml.io/linkml)

## Source Files

We took the Excel file from here: https://www.rd-alliance.org/group/research-metadata-schemas-wg/outcomes/collection-crosswalks-fifteen-research-data-schemas

We made various changes to make it more FAIR, including fixing mappings to be CURIEs.

Our google sheet: [RDA edited](https://docs.google.com/spreadsheets/d/1mu9iWZxX4DvtklLIQgEloM8oZfzZdzfJ/edit#gid=1108662376)

We also included a [Schemasheets](https://linkml.io/schemasheets) header line to formally describe the column headings


## Translation

We then use the LinkML generators to make various products

* [schema](schema) Schema documentation
