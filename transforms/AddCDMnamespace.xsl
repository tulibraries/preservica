<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:cdm="http://www.contentdm.org">
    
    <!-- This transform will add a CONTENTdm namespace prefix to a CONTENTdm Custom XML Export record (in which the elements are not currently prefixed).
        
        For example,
        
        <record>
            <title>Title</title>
            <author>Author</author>
        </record>
        
        will transform to
        
        <cdm:record>
            <cdm:title>Title</cdm:title>
            <cdm:author>Author</cdm:author>
        </cdm:record>
        
        Preservica requires that all incoming XML metadata has a namespace. After this transform is applied, a CONTENTdm Custom XML Export record can be added to 
        a Preservica entity via the Preservica API.
        
        Sample pyPreservica snippet to apply the transformed XML export to a Preservica asset:
        
        >>> with open("export.xml", 'r', encoding="UTF-8") as md:
        >>>     asset = client.add_metadata(asset, "http://www.contentdm.org", md)
         
    -->
    
    <!-- Identity template to copy all nodes and attributes -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
    
    <!-- Transform record element to include cdm namespace prefix -->
    <xsl:template match="record">
        <cdm:record xmlns:cdm="http://www.contentdm.org">
            <xsl:apply-templates select="@*|node()"/>
        </cdm:record>
    </xsl:template>
    
    <!-- Add namespace prefix to all child elements of record -->
    <xsl:template match="record//*">
        <xsl:element name="cdm:{local-name()}" namespace="http://www.contentdm.org">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>
    
</xsl:stylesheet>
