# Auto generated from rda.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-02-02T17:47:13
# Schema: rda
#
# id: rda
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
B2FIND = CurieNamespace('B2FIND', 'http://example.org/B2FIND/')
CODEMETA = CurieNamespace('CodeMeta', 'http://example.org/CodeMeta/')
DATS = CurieNamespace('DATS', 'http://example.org/DATS/')
DDI = CurieNamespace('DDI', 'http://example.org/DDI/')
DATACITE = CurieNamespace('Datacite', 'http://example.org/Datacite/')
DATAVERSE = CurieNamespace('Dataverse', 'http://example.org/Dataverse/')
ECRIN = CurieNamespace('ECRIN', 'http://example.org/ECRIN/')
EOSC = CurieNamespace('EOSC', 'http://example.org/EOSC/')
ISO19115_1 = CurieNamespace('ISO19115-1', 'http://example.org/ISO19115-1/')
BIOSCHEMAS = CurieNamespace('bioschemas', 'http://example.org/bioschemas/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'http://example.org/dct/')
DCTERMS = CurieNamespace('dcterms', 'https://dublincore.org/specifications/dublin-core/dcmi-terms/#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDA = CurieNamespace('rda', 'https://example.org/rda/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SOSA = CurieNamespace('sosa', 'http://example.org/sosa/')
UNKNOWN = CurieNamespace('unknown', 'http://example.org/unknown/')
DEFAULT_ = RDA


# Types

# Class references



@dataclass
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.Thing
    class_class_curie: ClassVar[str] = "rda:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = RDA.Thing

    description: str = None
    name: str = None
    identifier: Optional[str] = None
    alternateName: Optional[str] = None
    sameAs: Optional[Union[str, URIorCURIE]] = None
    url: Optional[Union[str, URIorCURIE]] = None
    contactPoint: Optional[str] = None
    inLanguage: Optional[str] = None
    isRelatedTo: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.alternateName is not None and not isinstance(self.alternateName, str):
            self.alternateName = str(self.alternateName)

        if self.sameAs is not None and not isinstance(self.sameAs, URIorCURIE):
            self.sameAs = URIorCURIE(self.sameAs)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.contactPoint is not None and not isinstance(self.contactPoint, str):
            self.contactPoint = str(self.contactPoint)

        if self.inLanguage is not None and not isinstance(self.inLanguage, str):
            self.inLanguage = str(self.inLanguage)

        if self.isRelatedTo is not None and not isinstance(self.isRelatedTo, str):
            self.isRelatedTo = str(self.isRelatedTo)

        super().__post_init__(**kwargs)


@dataclass
class DataDownload(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.DataDownload
    class_class_curie: ClassVar[str] = "rda:DataDownload"
    class_name: ClassVar[str] = "DataDownload"
    class_model_uri: ClassVar[URIRef] = RDA.DataDownload

    distribution.contentUrl: Optional[Union[str, URIorCURIE]] = None
    distribution.encodingFormat: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.distribution.contentUrl is not None and not isinstance(self.distribution.contentUrl, URIorCURIE):
            self.distribution.contentUrl = URIorCURIE(self.distribution.contentUrl)

        if self.distribution.encodingFormat is not None and not isinstance(self.distribution.encodingFormat, str):
            self.distribution.encodingFormat = str(self.distribution.encodingFormat)

        super().__post_init__(**kwargs)


@dataclass
class CreativeWork(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.CreativeWork
    class_class_curie: ClassVar[str] = "rda:CreativeWork"
    class_name: ClassVar[str] = "CreativeWork"
    class_model_uri: ClassVar[URIRef] = RDA.CreativeWork

    citation: Optional[str] = None
    keywords: Optional[str] = None
    license: Optional[str] = None
    creator: Optional[str] = None
    isPartOf: Optional[str] = None
    hasPart: Optional[str] = None
    version: Optional[str] = None
    temporalCoverage: Optional[str] = None
    spatialCoverage: Optional[str] = None
    funder: Optional[str] = None
    publisher: Optional[str] = None
    subjectOf: Optional[str] = None
    dateCreated: Optional[str] = None
    datePublished: Optional[Union[str, XSDDate]] = None
    dateModified: Optional[str] = None
    copyrightHolder: Optional[str] = None
    mentions: Optional[str] = None
    isBasedOn: Optional[str] = None
    encodingFormat: Optional[str] = None
    fileFormat_(superseded_by_encordingFormat): Optional[str] = None
    contributor: Optional[str] = None
    producer: Optional[str] = None
    editor: Optional[str] = None
    copyrightYear: Optional[str] = None
    isAccessibleForFree: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.isPartOf is not None and not isinstance(self.isPartOf, str):
            self.isPartOf = str(self.isPartOf)

        if self.hasPart is not None and not isinstance(self.hasPart, str):
            self.hasPart = str(self.hasPart)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.temporalCoverage is not None and not isinstance(self.temporalCoverage, str):
            self.temporalCoverage = str(self.temporalCoverage)

        if self.spatialCoverage is not None and not isinstance(self.spatialCoverage, str):
            self.spatialCoverage = str(self.spatialCoverage)

        if self.funder is not None and not isinstance(self.funder, str):
            self.funder = str(self.funder)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.subjectOf is not None and not isinstance(self.subjectOf, str):
            self.subjectOf = str(self.subjectOf)

        if self.dateCreated is not None and not isinstance(self.dateCreated, str):
            self.dateCreated = str(self.dateCreated)

        if self.datePublished is not None and not isinstance(self.datePublished, XSDDate):
            self.datePublished = XSDDate(self.datePublished)

        if self.dateModified is not None and not isinstance(self.dateModified, str):
            self.dateModified = str(self.dateModified)

        if self.copyrightHolder is not None and not isinstance(self.copyrightHolder, str):
            self.copyrightHolder = str(self.copyrightHolder)

        if self.mentions is not None and not isinstance(self.mentions, str):
            self.mentions = str(self.mentions)

        if self.isBasedOn is not None and not isinstance(self.isBasedOn, str):
            self.isBasedOn = str(self.isBasedOn)

        if self.encodingFormat is not None and not isinstance(self.encodingFormat, str):
            self.encodingFormat = str(self.encodingFormat)

        if self.fileFormat_(superseded_by_encordingFormat) is not None and not isinstance(self.fileFormat_(superseded_by_encordingFormat), str):
            self.fileFormat_(superseded_by_encordingFormat) = str(self.fileFormat_(superseded_by_encordingFormat))

        if self.funder is not None and not isinstance(self.funder, str):
            self.funder = str(self.funder)

        if self.contributor is not None and not isinstance(self.contributor, str):
            self.contributor = str(self.contributor)

        if self.producer is not None and not isinstance(self.producer, str):
            self.producer = str(self.producer)

        if self.editor is not None and not isinstance(self.editor, str):
            self.editor = str(self.editor)

        if self.copyrightYear is not None and not isinstance(self.copyrightYear, str):
            self.copyrightYear = str(self.copyrightYear)

        if self.isAccessibleForFree is not None and not isinstance(self.isAccessibleForFree, Bool):
            self.isAccessibleForFree = Bool(self.isAccessibleForFree)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.Dataset
    class_class_curie: ClassVar[str] = "rda:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = RDA.Dataset

    measurementTechnique: Optional[str] = None
    variableMeasured: Optional[str] = None
    includedInDataCatalog: Optional[str] = None
    distribution: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurementTechnique is not None and not isinstance(self.measurementTechnique, str):
            self.measurementTechnique = str(self.measurementTechnique)

        if self.variableMeasured is not None and not isinstance(self.variableMeasured, str):
            self.variableMeasured = str(self.variableMeasured)

        if self.includedInDataCatalog is not None and not isinstance(self.includedInDataCatalog, str):
            self.includedInDataCatalog = str(self.includedInDataCatalog)

        if self.distribution is not None and not isinstance(self.distribution, str):
            self.distribution = str(self.distribution)

        super().__post_init__(**kwargs)


@dataclass
class DataCatalog(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.DataCatalog
    class_class_curie: ClassVar[str] = "rda:DataCatalog"
    class_name: ClassVar[str] = "DataCatalog"
    class_model_uri: ClassVar[URIRef] = RDA.DataCatalog

    measurementTechnique: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurementTechnique is not None and not isinstance(self.measurementTechnique, str):
            self.measurementTechnique = str(self.measurementTechnique)

        super().__post_init__(**kwargs)


@dataclass
class DataDowload(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.DataDowload
    class_class_curie: ClassVar[str] = "rda:DataDowload"
    class_name: ClassVar[str] = "DataDowload"
    class_model_uri: ClassVar[URIRef] = RDA.DataDowload

    measurementTechnique: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measurementTechnique is not None and not isinstance(self.measurementTechnique, str):
            self.measurementTechnique = str(self.measurementTechnique)

        super().__post_init__(**kwargs)


@dataclass
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.Thing
    class_class_curie: ClassVar[str] = "rda:Thing"
    class_name: ClassVar[str] = " Thing"
    class_model_uri: ClassVar[URIRef] = RDA.Thing

    subjectOf: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subjectOf is not None and not isinstance(self.subjectOf, str):
            self.subjectOf = str(self.subjectOf)

        super().__post_init__(**kwargs)


@dataclass
class MediaObject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.MediaObject
    class_class_curie: ClassVar[str] = "rda:MediaObject"
    class_name: ClassVar[str] = "MediaObject"
    class_model_uri: ClassVar[URIRef] = RDA.MediaObject

    contentURL: Optional[Union[str, URIorCURIE]] = None
    contentSize: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contentURL is not None and not isinstance(self.contentURL, URIorCURIE):
            self.contentURL = URIorCURIE(self.contentURL)

        if self.contentSize is not None and not isinstance(self.contentSize, str):
            self.contentSize = str(self.contentSize)

        super().__post_init__(**kwargs)


@dataclass
class Schedule(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDA.Schedule
    class_class_curie: ClassVar[str] = "rda:Schedule"
    class_name: ClassVar[str] = "Schedule"
    class_model_uri: ClassVar[URIRef] = RDA.Schedule

    repeatFrequency: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.repeatFrequency is not None and not isinstance(self.repeatFrequency, str):
            self.repeatFrequency = str(self.repeatFrequency)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.description = Slot(uri=RDA.description, name="description", curie=RDA.curie('description'),
                   model_uri=RDA.description, domain=None, range=str)

slots.name = Slot(uri=RDA.name, name="name", curie=RDA.curie('name'),
                   model_uri=RDA.name, domain=None, range=str)

slots.distribution.contentUrl = Slot(uri=RDA['distribution.contentUrl'], name="distribution.contentUrl", curie=RDA.curie('distribution.contentUrl'),
                   model_uri=RDA['distribution.contentUrl'], domain=None, range=Optional[Union[str, URIorCURIE]])

slots.identifier = Slot(uri=RDA.identifier, name="identifier", curie=RDA.curie('identifier'),
                   model_uri=RDA.identifier, domain=None, range=Optional[str])

slots.alternateName = Slot(uri=RDA.alternateName, name="alternateName", curie=RDA.curie('alternateName'),
                   model_uri=RDA.alternateName, domain=None, range=Optional[str])

slots.sameAs = Slot(uri=RDA.sameAs, name="sameAs", curie=RDA.curie('sameAs'),
                   model_uri=RDA.sameAs, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.url = Slot(uri=RDA.url, name="url", curie=RDA.curie('url'),
                   model_uri=RDA.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.citation = Slot(uri=RDA.citation, name="citation", curie=RDA.curie('citation'),
                   model_uri=RDA.citation, domain=None, range=Optional[str])

slots.keywords = Slot(uri=RDA.keywords, name="keywords", curie=RDA.curie('keywords'),
                   model_uri=RDA.keywords, domain=None, range=Optional[str])

slots.license = Slot(uri=RDA.license, name="license", curie=RDA.curie('license'),
                   model_uri=RDA.license, domain=None, range=Optional[str])

slots.creator = Slot(uri=RDA.creator, name="creator", curie=RDA.curie('creator'),
                   model_uri=RDA.creator, domain=None, range=Optional[str])

slots.isPartOf = Slot(uri=RDA.isPartOf, name="isPartOf", curie=RDA.curie('isPartOf'),
                   model_uri=RDA.isPartOf, domain=None, range=Optional[str])

slots.hasPart = Slot(uri=RDA.hasPart, name="hasPart", curie=RDA.curie('hasPart'),
                   model_uri=RDA.hasPart, domain=None, range=Optional[str])

slots.version = Slot(uri=RDA.version, name="version", curie=RDA.curie('version'),
                   model_uri=RDA.version, domain=None, range=Optional[str])

slots.temporalCoverage = Slot(uri=RDA.temporalCoverage, name="temporalCoverage", curie=RDA.curie('temporalCoverage'),
                   model_uri=RDA.temporalCoverage, domain=None, range=Optional[str])

slots.spatialCoverage = Slot(uri=RDA.spatialCoverage, name="spatialCoverage", curie=RDA.curie('spatialCoverage'),
                   model_uri=RDA.spatialCoverage, domain=None, range=Optional[str])

slots.measurementTechnique = Slot(uri=RDA.measurementTechnique, name="measurementTechnique", curie=RDA.curie('measurementTechnique'),
                   model_uri=RDA.measurementTechnique, domain=None, range=Optional[str])

slots.variableMeasured = Slot(uri=RDA.variableMeasured, name="variableMeasured", curie=RDA.curie('variableMeasured'),
                   model_uri=RDA.variableMeasured, domain=None, range=Optional[str])

slots.includedInDataCatalog = Slot(uri=RDA.includedInDataCatalog, name="includedInDataCatalog", curie=RDA.curie('includedInDataCatalog'),
                   model_uri=RDA.includedInDataCatalog, domain=None, range=Optional[str])

slots.distribution = Slot(uri=RDA.distribution, name="distribution", curie=RDA.curie('distribution'),
                   model_uri=RDA.distribution, domain=None, range=Optional[str])

slots.distribution.encodingFormat = Slot(uri=RDA['distribution.encodingFormat'], name="distribution.encodingFormat", curie=RDA.curie('distribution.encodingFormat'),
                   model_uri=RDA['distribution.encodingFormat'], domain=None, range=Optional[str])

slots.funder = Slot(uri=RDA.funder, name="funder", curie=RDA.curie('funder'),
                   model_uri=RDA.funder, domain=None, range=Optional[str])

slots.publisher = Slot(uri=RDA.publisher, name="publisher", curie=RDA.curie('publisher'),
                   model_uri=RDA.publisher, domain=None, range=Optional[str])

slots.contactPoint = Slot(uri=RDA.contactPoint, name="contactPoint", curie=RDA.curie('contactPoint'),
                   model_uri=RDA.contactPoint, domain=None, range=Optional[str])

slots.subjectOf = Slot(uri=RDA.subjectOf, name="subjectOf", curie=RDA.curie('subjectOf'),
                   model_uri=RDA.subjectOf, domain=None, range=Optional[str])

slots.inLanguage = Slot(uri=RDA.inLanguage, name="inLanguage", curie=RDA.curie('inLanguage'),
                   model_uri=RDA.inLanguage, domain=None, range=Optional[str])

slots.dateCreated = Slot(uri=RDA.dateCreated, name="dateCreated", curie=RDA.curie('dateCreated'),
                   model_uri=RDA.dateCreated, domain=None, range=Optional[str])

slots.datePublished = Slot(uri=RDA.datePublished, name="datePublished", curie=RDA.curie('datePublished'),
                   model_uri=RDA.datePublished, domain=None, range=Optional[Union[str, XSDDate]])

slots.dateModified = Slot(uri=RDA.dateModified, name="dateModified", curie=RDA.curie('dateModified'),
                   model_uri=RDA.dateModified, domain=None, range=Optional[str])

slots.copyrightHolder = Slot(uri=RDA.copyrightHolder, name="copyrightHolder", curie=RDA.curie('copyrightHolder'),
                   model_uri=RDA.copyrightHolder, domain=None, range=Optional[str])

slots.mentions = Slot(uri=RDA.mentions, name="mentions", curie=RDA.curie('mentions'),
                   model_uri=RDA.mentions, domain=None, range=Optional[str])

slots.isBasedOn = Slot(uri=RDA.isBasedOn, name="isBasedOn", curie=RDA.curie('isBasedOn'),
                   model_uri=RDA.isBasedOn, domain=None, range=Optional[str])

slots.isRelatedTo = Slot(uri=RDA.isRelatedTo, name="isRelatedTo", curie=RDA.curie('isRelatedTo'),
                   model_uri=RDA.isRelatedTo, domain=None, range=Optional[str])

slots.encodingFormat = Slot(uri=RDA.encodingFormat, name="encodingFormat", curie=RDA.curie('encodingFormat'),
                   model_uri=RDA.encodingFormat, domain=None, range=Optional[str])

slots.fileFormat_(superseded_by_encordingFormat) = Slot(uri=RDA['fileFormat_(superseded_by_encordingFormat)'], name="fileFormat (superseded by encordingFormat)", curie=RDA.curie('fileFormat_(superseded_by_encordingFormat)'),
                   model_uri=RDA['fileFormat_(superseded_by_encordingFormat)'], domain=None, range=Optional[str])

slots.contentURL = Slot(uri=RDA.contentURL, name="contentURL", curie=RDA.curie('contentURL'),
                   model_uri=RDA.contentURL, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.contentSize = Slot(uri=RDA.contentSize, name="contentSize", curie=RDA.curie('contentSize'),
                   model_uri=RDA.contentSize, domain=None, range=Optional[str])

slots.repeatFrequency = Slot(uri=RDA.repeatFrequency, name="repeatFrequency", curie=RDA.curie('repeatFrequency'),
                   model_uri=RDA.repeatFrequency, domain=None, range=Optional[str])

slots.contributor = Slot(uri=RDA.contributor, name="contributor", curie=RDA.curie('contributor'),
                   model_uri=RDA.contributor, domain=None, range=Optional[str])

slots.producer = Slot(uri=RDA.producer, name="producer", curie=RDA.curie('producer'),
                   model_uri=RDA.producer, domain=None, range=Optional[str])

slots.editor = Slot(uri=RDA.editor, name="editor", curie=RDA.curie('editor'),
                   model_uri=RDA.editor, domain=None, range=Optional[str])

slots.copyrightYear = Slot(uri=RDA.copyrightYear, name="copyrightYear", curie=RDA.curie('copyrightYear'),
                   model_uri=RDA.copyrightYear, domain=None, range=Optional[str])

slots.isAccessibleForFree = Slot(uri=RDA.isAccessibleForFree, name="isAccessibleForFree", curie=RDA.curie('isAccessibleForFree'),
                   model_uri=RDA.isAccessibleForFree, domain=None, range=Optional[Union[bool, Bool]])