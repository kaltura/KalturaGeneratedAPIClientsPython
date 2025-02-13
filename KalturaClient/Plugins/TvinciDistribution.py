# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platforms allow them to do with
# text.
#
# Copyright (C) 2006-2023  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package Kaltura
# @subpackage Client
from __future__ import absolute_import

from .Core import *
from .ContentDistribution import *
from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaTvinciAssetsType(object):
    REGULAR = 1
    VIRTUAL = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProviderOrderBy(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionTag(KalturaObjectBase):
    def __init__(self,
            tagname = NotImplemented,
            extension = NotImplemented,
            protocol = NotImplemented,
            format = NotImplemented,
            filename = NotImplemented,
            ppvmodule = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        self.tagname = tagname

        # @var str
        self.extension = extension

        # @var str
        self.protocol = protocol

        # @var str
        self.format = format

        # @var str
        self.filename = filename

        # @var str
        self.ppvmodule = ppvmodule


    PROPERTY_LOADERS = {
        'tagname': getXmlNodeText, 
        'extension': getXmlNodeText, 
        'protocol': getXmlNodeText, 
        'format': getXmlNodeText, 
        'filename': getXmlNodeText, 
        'ppvmodule': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionTag.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionTag")
        kparams.addStringIfDefined("tagname", self.tagname)
        kparams.addStringIfDefined("extension", self.extension)
        kparams.addStringIfDefined("protocol", self.protocol)
        kparams.addStringIfDefined("format", self.format)
        kparams.addStringIfDefined("filename", self.filename)
        kparams.addStringIfDefined("ppvmodule", self.ppvmodule)
        return kparams

    def getTagname(self):
        return self.tagname

    def setTagname(self, newTagname):
        self.tagname = newTagname

    def getExtension(self):
        return self.extension

    def setExtension(self, newExtension):
        self.extension = newExtension

    def getProtocol(self):
        return self.protocol

    def setProtocol(self, newProtocol):
        self.protocol = newProtocol

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getFilename(self):
        return self.filename

    def setFilename(self, newFilename):
        self.filename = newFilename

    def getPpvmodule(self):
        return self.ppvmodule

    def setPpvmodule(self, newPpvmodule):
        self.ppvmodule = newPpvmodule


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProvider(KalturaDistributionProvider):
    def __init__(self,
            type = NotImplemented,
            name = NotImplemented,
            scheduleUpdateEnabled = NotImplemented,
            availabilityUpdateEnabled = NotImplemented,
            deleteInsteadUpdate = NotImplemented,
            intervalBeforeSunrise = NotImplemented,
            intervalBeforeSunset = NotImplemented,
            updateRequiredEntryFields = NotImplemented,
            updateRequiredMetadataXPaths = NotImplemented):
        KalturaDistributionProvider.__init__(self,
            type,
            name,
            scheduleUpdateEnabled,
            availabilityUpdateEnabled,
            deleteInsteadUpdate,
            intervalBeforeSunrise,
            intervalBeforeSunset,
            updateRequiredEntryFields,
            updateRequiredMetadataXPaths)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProvider.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionProvider")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    def __init__(self,
            fieldValues = NotImplemented,
            xml = NotImplemented):
        KalturaConfigurableDistributionJobProviderData.__init__(self,
            fieldValues)

        # @var str
        self.xml = xml


    PROPERTY_LOADERS = {
        'xml': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionJobProviderData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionJobProviderData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionJobProviderData.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionJobProviderData")
        kparams.addStringIfDefined("xml", self.xml)
        return kparams

    def getXml(self):
        return self.xml

    def setXml(self, newXml):
        self.xml = newXml


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProfile(KalturaConfigurableDistributionProfile):
    def __init__(self,
            id = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            partnerId = NotImplemented,
            providerType = NotImplemented,
            name = NotImplemented,
            status = NotImplemented,
            submitEnabled = NotImplemented,
            updateEnabled = NotImplemented,
            deleteEnabled = NotImplemented,
            reportEnabled = NotImplemented,
            autoCreateFlavors = NotImplemented,
            autoCreateThumb = NotImplemented,
            optionalFlavorParamsIds = NotImplemented,
            requiredFlavorParamsIds = NotImplemented,
            optionalThumbDimensions = NotImplemented,
            requiredThumbDimensions = NotImplemented,
            optionalAssetDistributionRules = NotImplemented,
            requiredAssetDistributionRules = NotImplemented,
            sunriseDefaultOffset = NotImplemented,
            sunsetDefaultOffset = NotImplemented,
            recommendedStorageProfileForDownload = NotImplemented,
            recommendedDcForDownload = NotImplemented,
            recommendedDcForExecute = NotImplemented,
            distributeTrigger = NotImplemented,
            supportImageEntry = NotImplemented,
            fieldConfigArray = NotImplemented,
            itemXpathsToExtend = NotImplemented,
            useCategoryEntries = NotImplemented,
            ingestUrl = NotImplemented,
            username = NotImplemented,
            password = NotImplemented,
            tags = NotImplemented,
            xsltFile = NotImplemented,
            innerType = NotImplemented,
            assetsType = NotImplemented):
        KalturaConfigurableDistributionProfile.__init__(self,
            id,
            createdAt,
            updatedAt,
            partnerId,
            providerType,
            name,
            status,
            submitEnabled,
            updateEnabled,
            deleteEnabled,
            reportEnabled,
            autoCreateFlavors,
            autoCreateThumb,
            optionalFlavorParamsIds,
            requiredFlavorParamsIds,
            optionalThumbDimensions,
            requiredThumbDimensions,
            optionalAssetDistributionRules,
            requiredAssetDistributionRules,
            sunriseDefaultOffset,
            sunsetDefaultOffset,
            recommendedStorageProfileForDownload,
            recommendedDcForDownload,
            recommendedDcForExecute,
            distributeTrigger,
            supportImageEntry,
            fieldConfigArray,
            itemXpathsToExtend,
            useCategoryEntries)

        # @var str
        self.ingestUrl = ingestUrl

        # @var str
        self.username = username

        # @var str
        self.password = password

        # Tags array for Tvinci distribution
        # @var List[KalturaTvinciDistributionTag]
        self.tags = tags

        # @var str
        self.xsltFile = xsltFile

        # @var str
        self.innerType = innerType

        # @var KalturaTvinciAssetsType
        self.assetsType = assetsType


    PROPERTY_LOADERS = {
        'ingestUrl': getXmlNodeText, 
        'username': getXmlNodeText, 
        'password': getXmlNodeText, 
        'tags': (KalturaObjectFactory.createArray, 'KalturaTvinciDistributionTag'), 
        'xsltFile': getXmlNodeText, 
        'innerType': getXmlNodeText, 
        'assetsType': (KalturaEnumsFactory.createInt, "KalturaTvinciAssetsType"), 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionProfile")
        kparams.addStringIfDefined("ingestUrl", self.ingestUrl)
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("password", self.password)
        kparams.addArrayIfDefined("tags", self.tags)
        kparams.addStringIfDefined("xsltFile", self.xsltFile)
        kparams.addStringIfDefined("innerType", self.innerType)
        kparams.addIntEnumIfDefined("assetsType", self.assetsType)
        return kparams

    def getIngestUrl(self):
        return self.ingestUrl

    def setIngestUrl(self, newIngestUrl):
        self.ingestUrl = newIngestUrl

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getXsltFile(self):
        return self.xsltFile

    def setXsltFile(self, newXsltFile):
        self.xsltFile = newXsltFile

    def getInnerType(self):
        return self.innerType

    def setInnerType(self, newInnerType):
        self.innerType = newInnerType

    def getAssetsType(self):
        return self.assetsType

    def setAssetsType(self, newAssetsType):
        self.assetsType = newAssetsType


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented):
        KalturaDistributionProviderFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProviderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionProviderBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProviderFilter(KalturaTvinciDistributionProviderBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented):
        KalturaTvinciDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTvinciDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTvinciDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionProviderFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented):
        KalturaConfigurableDistributionProfileFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfileFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionProfileBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaTvinciDistributionProfileFilter(KalturaTvinciDistributionProfileBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented):
        KalturaTvinciDistributionProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTvinciDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTvinciDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTvinciDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaTvinciDistributionProfileFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaTvinciDistributionClientPlugin(KalturaClientPlugin):
    # KalturaTvinciDistributionClientPlugin
    instance = None

    # @return KalturaTvinciDistributionClientPlugin
    @staticmethod
    def get():
        if KalturaTvinciDistributionClientPlugin.instance == None:
            KalturaTvinciDistributionClientPlugin.instance = KalturaTvinciDistributionClientPlugin()
        return KalturaTvinciDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaTvinciAssetsType': KalturaTvinciAssetsType,
            'KalturaTvinciDistributionProfileOrderBy': KalturaTvinciDistributionProfileOrderBy,
            'KalturaTvinciDistributionProviderOrderBy': KalturaTvinciDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaTvinciDistributionTag': KalturaTvinciDistributionTag,
            'KalturaTvinciDistributionProvider': KalturaTvinciDistributionProvider,
            'KalturaTvinciDistributionJobProviderData': KalturaTvinciDistributionJobProviderData,
            'KalturaTvinciDistributionProfile': KalturaTvinciDistributionProfile,
            'KalturaTvinciDistributionProviderBaseFilter': KalturaTvinciDistributionProviderBaseFilter,
            'KalturaTvinciDistributionProviderFilter': KalturaTvinciDistributionProviderFilter,
            'KalturaTvinciDistributionProfileBaseFilter': KalturaTvinciDistributionProfileBaseFilter,
            'KalturaTvinciDistributionProfileFilter': KalturaTvinciDistributionProfileFilter,
        }

    # @return string
    def getName(self):
        return 'tvinciDistribution'

