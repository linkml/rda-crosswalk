
# Class: Dataset




URI: [rda:Dataset](https://example.org/rda/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset&#124;measurementTechnique:string%20%3F;variableMeasured:string%20%3F;includedInDataCatalog:string%20%3F;distribution:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset&#124;measurementTechnique:string%20%3F;variableMeasured:string%20%3F;includedInDataCatalog:string%20%3F;distribution:string%20%3F])

## Attributes


### Own

 * [measurementTechnique](measurementTechnique.md)  <sub>0..1</sub>
     * Description: A technique or technology used in a Dataset (or DataDownload, DataCatalog), corresponding to the method used for measuring the corresponding variable(s)
     * Range: [String](types/String.md)
 * [variableMeasured](variableMeasured.md)  <sub>0..1</sub>
     * Description: The variableMeasured property can indicate (repeated as necessary) the variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue.  (The variable that this dataset measures. For example, temperature or pressure.)
     * Range: [String](types/String.md)
 * [includedInDataCatalog](includedInDataCatalog.md)  <sub>0..1</sub>
     * Description: A data catalog which contains this dataset.  (The catalog to which the dataset belongs.)
     * Range: [String](types/String.md)
 * [distribution](distribution.md)  <sub>0..1</sub>
     * Description: A downloadable form of this dataset, at a specific location, in a specific format (The description of the location for download of the dataset and the file format for download.)
     * Range: [String](types/String.md)
