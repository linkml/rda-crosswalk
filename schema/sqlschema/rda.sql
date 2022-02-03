

CREATE TABLE "Thing" (
	description TEXT NOT NULL, 
	name TEXT NOT NULL, 
	identifier TEXT, 
	"alternateName" TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	"contactPoint" TEXT, 
	"inLanguage" TEXT, 
	"isRelatedTo" TEXT, 
	PRIMARY KEY (description, name, identifier, "alternateName", "sameAs", url, "contactPoint", "inLanguage", "isRelatedTo")
);

CREATE TABLE "CreativeWork" (
	citation TEXT, 
	keywords TEXT, 
	license TEXT, 
	creator TEXT, 
	"isPartOf" TEXT, 
	"hasPart" TEXT, 
	version TEXT, 
	"temporalCoverage" TEXT, 
	"spatialCoverage" TEXT, 
	funder TEXT, 
	publisher TEXT, 
	"subjectOf" TEXT, 
	"dateCreated" TEXT, 
	"datePublished" DATE, 
	"dateModified" TEXT, 
	"copyrightHolder" TEXT, 
	mentions TEXT, 
	"isBasedOn" TEXT, 
	"encodingFormat" TEXT, 
	"fileFormat_(superseded_by_encordingFormat)" TEXT, 
	contributor TEXT, 
	producer TEXT, 
	editor TEXT, 
	"copyrightYear" TEXT, 
	"isAccessibleForFree" BOOLEAN, 
	PRIMARY KEY (citation, keywords, license, creator, "isPartOf", "hasPart", version, "temporalCoverage", "spatialCoverage", funder, publisher, "subjectOf", "dateCreated", "datePublished", "dateModified", "copyrightHolder", mentions, "isBasedOn", "encodingFormat", "fileFormat_(superseded_by_encordingFormat)", contributor, producer, editor, "copyrightYear", "isAccessibleForFree")
);

CREATE TABLE "DataCatalog" (
	"measurementTechnique" TEXT, 
	PRIMARY KEY ("measurementTechnique")
);

CREATE TABLE "DataDowload" (
	"measurementTechnique" TEXT, 
	PRIMARY KEY ("measurementTechnique")
);

CREATE TABLE "DataDownload" (
	"distribution.contentUrl" TEXT, 
	"distribution.encodingFormat" TEXT, 
	PRIMARY KEY ("distribution.contentUrl", "distribution.encodingFormat")
);

CREATE TABLE "Dataset" (
	"measurementTechnique" TEXT, 
	"variableMeasured" TEXT, 
	"includedInDataCatalog" TEXT, 
	distribution TEXT, 
	PRIMARY KEY ("measurementTechnique", "variableMeasured", "includedInDataCatalog", distribution)
);

CREATE TABLE "MediaObject" (
	"contentURL" TEXT, 
	"contentSize" TEXT, 
	PRIMARY KEY ("contentURL", "contentSize")
);

CREATE TABLE "Schedule" (
	"repeatFrequency" TEXT, 
	PRIMARY KEY ("repeatFrequency")
);
