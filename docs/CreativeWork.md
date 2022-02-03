
# Class: CreativeWork




URI: [rda:CreativeWork](https://example.org/rda/CreativeWork)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CreativeWork&#124;citation:string%20%3F;keywords:string%20%3F;license:string%20%3F;creator:string%20%3F;isPartOf:string%20%3F;hasPart:string%20%3F;version:string%20%3F;temporalCoverage:string%20%3F;spatialCoverage:string%20%3F;funder:string%20%3F;publisher:string%20%3F;subjectOf:string%20%3F;dateCreated:string%20%3F;datePublished:date%20%3F;dateModified:string%20%3F;copyrightHolder:string%20%3F;mentions:string%20%3F;isBasedOn:string%20%3F;encodingFormat:string%20%3F;fileFormat_(superseded_by_encordingFormat):string%20%3F;contributor:string%20%3F;producer:string%20%3F;editor:string%20%3F;copyrightYear:string%20%3F;isAccessibleForFree:boolean%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[CreativeWork&#124;citation:string%20%3F;keywords:string%20%3F;license:string%20%3F;creator:string%20%3F;isPartOf:string%20%3F;hasPart:string%20%3F;version:string%20%3F;temporalCoverage:string%20%3F;spatialCoverage:string%20%3F;funder:string%20%3F;publisher:string%20%3F;subjectOf:string%20%3F;dateCreated:string%20%3F;datePublished:date%20%3F;dateModified:string%20%3F;copyrightHolder:string%20%3F;mentions:string%20%3F;isBasedOn:string%20%3F;encodingFormat:string%20%3F;fileFormat_(superseded_by_encordingFormat):string%20%3F;contributor:string%20%3F;producer:string%20%3F;editor:string%20%3F;copyrightYear:string%20%3F;isAccessibleForFree:boolean%20%3F])

## Attributes


### Own

 * [citation](citation.md)  <sub>0..1</sub>
     * Description: A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.  (Identifies academic articles that are recommended by the data provider be cited in addition to the dataset itself. Provide the citation for the dataset itself with other properties, such as name, identifier, creator, and publisher properties. For example, this property can uniquely identify a related academic publication such as a data descriptor, data paper, or an article for which this dataset is supplementary material for.)
     * Range: [String](types/String.md)
 * [keywords](keywords.md)  <sub>0..1</sub>
     * Description: Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.
     * Range: [String](types/String.md)
 * [license](license.md)  <sub>0..1</sub>
     * Description: A license document that applies to this content, typically indicated by URL.  (A license under which the dataset is distributed.)
     * Range: [String](types/String.md)
 * [creator](creator.md)  <sub>0..1</sub>
     * Description: The creator/author of this CreativeWork (dataset). This is the same as the Author property for CreativeWork.  (To uniquely identify individuals, use ORCID ID as the value of the sameAs property of the Person type. To uniquely identify institutions and organizations, use ROR ID. )
     * Range: [String](types/String.md)
 * [isPartOf](isPartOf.md)  <sub>0..1</sub>
     * Description: Indicates a CreativeWork that this CreativeWork is (in some sense) part of. Reverse property hasPart.  If the dataset is a collection of smaller datasets, use the hasPart property to denote such relationship. Conversly, if the dataset is part of a larger dataset, use isPartOf.
     * Range: [String](types/String.md)
 * [hasPart](hasPart.md)  <sub>0..1</sub>
     * Description: Indicates a CreativeWork that is (in some sense) a part of this CreativeWork. Reverse property isPartOf
     * Range: [String](types/String.md)
 * [version](version.md)  <sub>0..1</sub>
     * Description: The version of the CreativeWork embodied by a specified resource.
     * Range: [String](types/String.md)
 * [temporalCoverage](temporalCoverage.md)  <sub>0..1</sub>
     * Description: The temporalCoverage of a CreativeWork indicates the period that the content applies to  (The data in the dataset covers a specific time interval. Only include this property if the dataset has a temporal dimension.)
     * Range: [String](types/String.md)
 * [spatialCoverage](spatialCoverage.md)  <sub>0..1</sub>
     * Description: The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content.  (You can provide a single point that describes the spatial aspect of the dataset. Only include this property if the dataset has a spatial dimension.)
     * Range: [String](types/String.md)
 * [funder](funder.md)  <sub>0..1</sub>
     * Description: A person or organization that supports (sponsors) something through some kind of financial contribution.
     * Range: [String](types/String.md)
 * [publisher](publisher.md)  <sub>0..1</sub>
     * Description: The publisher of the creative work
     * Range: [String](types/String.md)
 * [subjectOf](subjectOf.md)  <sub>0..1</sub>
     * Description: The subject matter of content
     * Range: [String](types/String.md)
 * [dateCreated](dateCreated.md)  <sub>0..1</sub>
     * Description: The date on which the CreativeWork was created or the item was added to a DataFeed.
     * Range: [String](types/String.md)
 * [datePublished](datePublished.md)  <sub>0..1</sub>
     * Description: Date of first broadcast/publication.
     * Range: [Date](types/Date.md)
 * [dateModified](dateModified.md)  <sub>0..1</sub>
     * Description: The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
     * Range: [String](types/String.md)
 * [copyrightHolder](copyrightHolder.md)  <sub>0..1</sub>
     * Description: The party holding the legal copyright to the CreativeWork.
     * Range: [String](types/String.md)
 * [mentions](mentions.md)  <sub>0..1</sub>
     * Description: Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.
     * Range: [String](types/String.md)
 * [isBasedOn](isBasedOn.md)  <sub>0..1</sub>
     * Description: A resource from which this work is derived or from which it is a modification or adaption
     * Range: [String](types/String.md)
 * [encodingFormat](encodingFormat.md)  <sub>0..1</sub>
     * Description: Media type typically expressed using a MIME format
     * Range: [String](types/String.md)
 * [fileFormat (superseded by encordingFormat)](fileFormat_(superseded_by_encordingFormat).md)  <sub>0..1</sub>
     * Description: Media type, typically MIME format (see IANA site) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry.
     * Range: [String](types/String.md)
 * [funder](funder.md)  <sub>0..1</sub>
     * Description: A person or organization that supports (sponsors) something through some kind of financial contribution.
     * Range: [String](types/String.md)
 * [contributor](contributor.md)  <sub>0..1</sub>
     * Description: A secondary contributor to the CreativeWork or Event.
     * Range: [String](types/String.md)
 * [producer](producer.md)  <sub>0..1</sub>
     * Description: The person or organization who produced the work (e.g. music album, movie, tv/radio series etc.).
     * Range: [String](types/String.md)
 * [editor](editor.md)  <sub>0..1</sub>
     * Description: Specifies the Person who edited the CreativeWork.
     * Range: [String](types/String.md)
 * [copyrightYear](copyrightYear.md)  <sub>0..1</sub>
     * Description: The year during which the claimed copyright for the CreativeWork was first asserted.
     * Range: [String](types/String.md)
 * [isAccessibleForFree](isAccessibleForFree.md)  <sub>0..1</sub>
     * Description: A flag to signal that the publication is accessible for free.
     * Range: [Boolean](types/Boolean.md)
