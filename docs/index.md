# RDA Schema crosswalk

This is in experiment translating the RDA Crosswalk to [LinkML](https://linkml.io/linkml)

![img](https://www.rd-alliance.org/sites/default/files/RDA%20Logo_5.png)
![linkml logo](https://avatars.githubusercontent.com/u/79337873?s=200&v=4)

This is a DEMO site and NOT an officially sanctioned RDA product - any errors are our own

## Source Files

We took the Excel file from here: https://www.rd-alliance.org/group/research-metadata-schemas-wg/outcomes/collection-crosswalks-fifteen-research-data-schemas

We made changes and put it up as a google sheet: [RDA edited](https://docs.google.com/spreadsheets/d/1mu9iWZxX4DvtklLIQgEloM8oZfzZdzfJ/edit#gid=1108662376)

 - We made various changes to make it more FAIR, including fixing mappings to be CURIEs.
 - We also included a [Schemasheets](https://linkml.io/schemasheets) header line to formally describe the column headings

## Translation

We then use the LinkML generators to make various products

 * schemasheets translation of google sheet to LinkML: [crosswalk.yaml](https://github.com/linkml/rda-crosswalk/blob/main/crosswalk.yaml)

Some limitations:

### Prefixes

- we don't provide any of our own information on prefixes. We rely on bioregistry
- any prefixes not found get an example.org URL

### Documentation Site

* [schema](schema) Schema documentation

This site is entirely automatically generated from the crosswalk file

### Derived Schema Products

These are also auto-derived

* [json-schema](https://github.com/linkml/rda-crosswalk/tree/main/schema/jsonschema)
* [SHACL](https://github.com/linkml/rda-crosswalk/tree/main/schema/shacl)
* [ShEx](https://github.com/linkml/rda-crosswalk/tree/main/schema/shex)
* [Mappings](https://github.com/linkml/rda-crosswalk/tree/main/schema/sssom) (in [SSSOM](https://w3id.org/sssom) )
* Other products: [schema/ folder](https://github.com/linkml/rda-crosswalk/tree/main/schema)
