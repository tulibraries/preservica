<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:oai_qdc="http://worldcat.org/xmlschemas/qdc-1.0/"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <!-- This transform takes an XML metadata file generated from an OAI-PMH harvest of an entire set, using the oai_qdc metadata prefix,
    and splits it into multiple files, 1 file per record. The resulting individual XML files will use the dc:identifier field as filename. -->
    
    <xsl:template match="/">
        <xsl:for-each select="//record">
            <xsl:result-document method="xml" href="{metadata/*/dc:identifier[1]}.xml">
                <xsl:copy-of select="."/>            
            </xsl:result-document>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>