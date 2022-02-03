
# rda schema





### Classes

 * [Thing](Thing.md)
 * [CreativeWork](CreativeWork.md)
 * [DataCatalog](DataCatalog.md)
 * [DataDowload](DataDowload.md)
 * [DataDownload](DataDownload.md)
 * [Dataset](Dataset.md)
 * [MediaObject](MediaObject.md)
 * [Schedule](Schedule.md)
 * [Thing](Thing.md)

### Mixins


### Slots

 * [alternateName](alternateName.md) - An alias for the item   (Alternative names that have been used to refer to this dataset, such as aliases or abbreviations.)
 * [citation](citation.md) - A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.  (Identifies academic articles that are recommended by the data provider be cited in addition to the dataset itself. Provide the citation for the dataset itself with other properties, such as name, identifier, creator, and publisher properties. For example, this property can uniquely identify a related academic publication such as a data descriptor, data paper, or an article for which this dataset is supplementary material for.)
 * [contactPoint](contactPoint.md) - A contact point, e.g. email, telephone, address
 * [contentSize](contentSize.md) - File size in (mega/kilo) bytes.
 * [contentURL](contentURL.md) - Actual bytes of the media object, for example the image file or video file.
 * [contributor](contributor.md) - A secondary contributor to the CreativeWork or Event.
 * [copyrightHolder](copyrightHolder.md) - The party holding the legal copyright to the CreativeWork.
 * [copyrightYear](copyrightYear.md) - The year during which the claimed copyright for the CreativeWork was first asserted.
 * [creator](creator.md) - The creator/author of this CreativeWork (dataset). This is the same as the Author property for CreativeWork.  (To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type. To uniquely identify institutions and organizations, use ROR ID. )
 * [dateCreated](dateCreated.md) - The date on which the CreativeWork was created or the item was added to a DataFeed.
 * [dateModified](dateModified.md) - The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
 * [datePublished](datePublished.md) - Date of first broadcast/publication.
 * [description](description.md) - A description of the item.
 * [distribution](distribution.md) - A downloadable form of this dataset, at a specific location, in a specific format (The description of the location for download of the dataset and the file format for download.)
 * [distribution.contentUrl](distribution.contentUrl.md) - (The link for the download.)
 * [distribution.encodingFormat](distribution.encodingFormat.md) - (The file format of the distribution.)
 * [editor](editor.md) - Specifies the Person who edited the CreativeWork.
 * [encodingFormat](encodingFormat.md) - Media type typically expressed using a MIME format
 * [fileFormat (superseded by encordingFormat)](fileFormat_(superseded_by_encordingFormat).md) - Media type, typically MIME format (see IANA site) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry.
 * [funder](funder.md) - A person or organization that supports (sponsors) something through some kind of financial contribution.
 * [hasPart](hasPart.md) - Indicates a CreativeWork that is (in some sense) a part of this CreativeWork. Reverse property isPartOf
 * [identifier](identifier.md) - The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details.
 * [inLanguage](inLanguage.md) - The language of the content or performance or used in an action.  Please use one of the language codes from the IETF BCP 47 standard.
 * [includedInDataCatalog](includedInDataCatalog.md) - A data catalog which contains this dataset.  (The catalog to which the dataset belongs.)
 * [isAccessibleForFree](isAccessibleForFree.md) - A flag to signal that the publication is accessible for free.
 * [isBasedOn](isBasedOn.md) - A resource from which this work is derived or from which it is a modification or adaption
 * [isPartOf](isPartOf.md) - Indicates a CreativeWork that this CreativeWork is (in some sense) part of. Reverse property hasPart.  If the dataset is a collection of smaller datasets, use the hasPart property to denote such relationship. Conversly, if the dataset is part of a larger dataset, use isPartOf.
 * [isRelatedTo](isRelatedTo.md) - A pointer to another, somehow related product (or multiple products).
 * [keywords](keywords.md) - Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.
 * [license](license.md) - A license document that applies to this content, typically indicated by URL.  (A license under which the dataset is distributed.)
 * [measurementTechnique](measurementTechnique.md) - A technique or technology used in a Dataset (or DataDownload, DataCatalog), corresponding to the method used for measuring the corresponding variable(s)
 * [mentions](mentions.md) - Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.
 * [name](name.md) - A descriptive name of the item (e.g. dataset, software, Organization).
 * [producer](producer.md) - The person or organization who produced the work (e.g. music album, movie, tv/radio series etc.).
 * [publisher](publisher.md) - The publisher of the creative work
 * [repeatFrequency](repeatFrequency.md) - This term is proposed for full integration into Schema.org* Defines the frequency at which Events will occur according to a schedule Schedule. The intervals between events should be defined as a Duration of time.
 * [sameAs](sameAs.md) - URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
 * [spatialCoverage](spatialCoverage.md) - The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content.  (You can provide a single point that describes the spatial aspect of the dataset. Only include this property if the dataset has a spatial dimension.)
 * [subjectOf](subjectOf.md) - The subject matter of content
 * [temporalCoverage](temporalCoverage.md) - The temporalCoverage of a CreativeWork indicates the period that the content applies to  (The data in the dataset covers a specific time interval. Only include this property if the dataset has a temporal dimension.)
 * [url](url.md) - URL of the item. (Location of a page describing the dataset.)
 * [variableMeasured](variableMeasured.md) - The variableMeasured property can indicate (repeated as necessary) the variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue.  (The variable that this dataset measures. For example, temperature or pressure.)
 * [version](version.md) - The version of the CreativeWork embodied by a specified resource.

### Enums


### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
