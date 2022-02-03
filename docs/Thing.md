
# Class: Thing




URI: [rda:Thing](https://example.org/rda/Thing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing&#124;description:string;name:string;identifier:string%20%3F;alternateName:string%20%3F;sameAs:uriorcurie%20%3F;url:uriorcurie%20%3F;contactPoint:string%20%3F;inLanguage:string%20%3F;isRelatedTo:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing&#124;description:string;name:string;identifier:string%20%3F;alternateName:string%20%3F;sameAs:uriorcurie%20%3F;url:uriorcurie%20%3F;contactPoint:string%20%3F;inLanguage:string%20%3F;isRelatedTo:string%20%3F])

## Attributes


### Own

 * [description](description.md)  <sub>1..1</sub>
     * Description: A description of the item.
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>1..1</sub>
     * Description: A descriptive name of the item (e.g. dataset, software, Organization).
     * Range: [String](types/String.md)
 * [identifier](identifier.md)  <sub>0..1</sub>
     * Description: The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details.
     * Range: [String](types/String.md)
 * [alternateName](alternateName.md)  <sub>0..1</sub>
     * Description: An alias for the item   (Alternative names that have been used to refer to this dataset, such as aliases or abbreviations.)
     * Range: [String](types/String.md)
 * [sameAs](sameAs.md)  <sub>0..1</sub>
     * Description: URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [url](url.md)  <sub>0..1</sub>
     * Description: URL of the item. (Location of a page describing the dataset.)
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [contactPoint](contactPoint.md)  <sub>0..1</sub>
     * Description: A contact point, e.g. email, telephone, address
     * Range: [String](types/String.md)
 * [inLanguage](inLanguage.md)  <sub>0..1</sub>
     * Description: The language of the content or performance or used in an action.  Please use one of the language codes from the IETF BCP 47 standard.
     * Range: [String](types/String.md)
 * [isRelatedTo](isRelatedTo.md)  <sub>0..1</sub>
     * Description: A pointer to another, somehow related product (or multiple products).
     * Range: [String](types/String.md)
