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
class KalturaCortexApiDistributionCaptionAction(object):
    UPDATE_ACTION = 1
    SUBMIT_ACTION = 2
    DELETE_ACTION = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProfileOrderBy(object):
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
class KalturaCortexApiDistributionProviderOrderBy(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaCortexApiCaptionDistributionInfo(KalturaObjectBase):
    def __init__(self,
            language = NotImplemented,
            label = NotImplemented,
            filePath = NotImplemented,
            remoteId = NotImplemented,
            action = NotImplemented,
            version = NotImplemented,
            assetId = NotImplemented,
            fileExt = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        self.language = language

        # @var str
        self.label = label

        # @var str
        self.filePath = filePath

        # @var str
        self.remoteId = remoteId

        # @var KalturaCortexApiDistributionCaptionAction
        self.action = action

        # @var str
        self.version = version

        # @var str
        self.assetId = assetId

        # @var str
        self.fileExt = fileExt


    PROPERTY_LOADERS = {
        'language': getXmlNodeText, 
        'label': getXmlNodeText, 
        'filePath': getXmlNodeText, 
        'remoteId': getXmlNodeText, 
        'action': (KalturaEnumsFactory.createInt, "KalturaCortexApiDistributionCaptionAction"), 
        'version': getXmlNodeText, 
        'assetId': getXmlNodeText, 
        'fileExt': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCortexApiCaptionDistributionInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCortexApiCaptionDistributionInfo")
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("label", self.label)
        kparams.addStringIfDefined("filePath", self.filePath)
        kparams.addStringIfDefined("remoteId", self.remoteId)
        kparams.addIntEnumIfDefined("action", self.action)
        kparams.addStringIfDefined("version", self.version)
        kparams.addStringIfDefined("assetId", self.assetId)
        kparams.addStringIfDefined("fileExt", self.fileExt)
        return kparams

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getLabel(self):
        return self.label

    def setLabel(self, newLabel):
        self.label = newLabel

    def getFilePath(self):
        return self.filePath

    def setFilePath(self, newFilePath):
        self.filePath = newFilePath

    def getRemoteId(self):
        return self.remoteId

    def setRemoteId(self, newRemoteId):
        self.remoteId = newRemoteId

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getVersion(self):
        return self.version

    def setVersion(self, newVersion):
        self.version = newVersion

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getFileExt(self):
        return self.fileExt

    def setFileExt(self, newFileExt):
        self.fileExt = newFileExt


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProvider(KalturaDistributionProvider):
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
        self.fromXmlImpl(node, KalturaCortexApiDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionProvider")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    def __init__(self,
            fieldValues = NotImplemented,
            videoAssetFilePath = NotImplemented,
            thumbAssetFilePath = NotImplemented,
            captionsInfo = NotImplemented):
        KalturaConfigurableDistributionJobProviderData.__init__(self,
            fieldValues)

        # @var str
        self.videoAssetFilePath = videoAssetFilePath

        # @var str
        self.thumbAssetFilePath = thumbAssetFilePath

        # @var List[KalturaCortexApiCaptionDistributionInfo]
        self.captionsInfo = captionsInfo


    PROPERTY_LOADERS = {
        'videoAssetFilePath': getXmlNodeText, 
        'thumbAssetFilePath': getXmlNodeText, 
        'captionsInfo': (KalturaObjectFactory.createArray, 'KalturaCortexApiCaptionDistributionInfo'), 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionJobProviderData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCortexApiDistributionJobProviderData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionJobProviderData.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionJobProviderData")
        kparams.addStringIfDefined("videoAssetFilePath", self.videoAssetFilePath)
        kparams.addStringIfDefined("thumbAssetFilePath", self.thumbAssetFilePath)
        kparams.addArrayIfDefined("captionsInfo", self.captionsInfo)
        return kparams

    def getVideoAssetFilePath(self):
        return self.videoAssetFilePath

    def setVideoAssetFilePath(self, newVideoAssetFilePath):
        self.videoAssetFilePath = newVideoAssetFilePath

    def getThumbAssetFilePath(self):
        return self.thumbAssetFilePath

    def setThumbAssetFilePath(self, newThumbAssetFilePath):
        self.thumbAssetFilePath = newThumbAssetFilePath

    def getCaptionsInfo(self):
        return self.captionsInfo

    def setCaptionsInfo(self, newCaptionsInfo):
        self.captionsInfo = newCaptionsInfo


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProfile(KalturaConfigurableDistributionProfile):
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
            username = NotImplemented,
            host = NotImplemented,
            password = NotImplemented,
            folderrecordid = NotImplemented,
            metadataprofileid = NotImplemented,
            metadataprofileidpushing = NotImplemented):
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
        self.username = username

        # @var str
        self.host = host

        # @var str
        self.password = password

        # @var str
        self.folderrecordid = folderrecordid

        # @var str
        self.metadataprofileid = metadataprofileid

        # @var str
        self.metadataprofileidpushing = metadataprofileidpushing


    PROPERTY_LOADERS = {
        'username': getXmlNodeText, 
        'host': getXmlNodeText, 
        'password': getXmlNodeText, 
        'folderrecordid': getXmlNodeText, 
        'metadataprofileid': getXmlNodeText, 
        'metadataprofileidpushing': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCortexApiDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionProfile")
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("host", self.host)
        kparams.addStringIfDefined("password", self.password)
        kparams.addStringIfDefined("folderrecordid", self.folderrecordid)
        kparams.addStringIfDefined("metadataprofileid", self.metadataprofileid)
        kparams.addStringIfDefined("metadataprofileidpushing", self.metadataprofileidpushing)
        return kparams

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getFolderrecordid(self):
        return self.folderrecordid

    def setFolderrecordid(self, newFolderrecordid):
        self.folderrecordid = newFolderrecordid

    def getMetadataprofileid(self):
        return self.metadataprofileid

    def setMetadataprofileid(self, newMetadataprofileid):
        self.metadataprofileid = newMetadataprofileid

    def getMetadataprofileidpushing(self):
        return self.metadataprofileidpushing

    def setMetadataprofileidpushing(self, newMetadataprofileidpushing):
        self.metadataprofileidpushing = newMetadataprofileidpushing


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
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
        self.fromXmlImpl(node, KalturaCortexApiDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionProviderBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProviderFilter(KalturaCortexApiDistributionProviderBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented):
        KalturaCortexApiDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaCortexApiDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCortexApiDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCortexApiDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionProviderFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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
        self.fromXmlImpl(node, KalturaCortexApiDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionProfileBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaCortexApiDistributionProfileFilter(KalturaCortexApiDistributionProfileBaseFilter):
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
        KalturaCortexApiDistributionProfileBaseFilter.__init__(self,
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
        KalturaCortexApiDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCortexApiDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCortexApiDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCortexApiDistributionProfileFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaCortexApiDistributionClientPlugin(KalturaClientPlugin):
    # KalturaCortexApiDistributionClientPlugin
    instance = None

    # @return KalturaCortexApiDistributionClientPlugin
    @staticmethod
    def get():
        if KalturaCortexApiDistributionClientPlugin.instance == None:
            KalturaCortexApiDistributionClientPlugin.instance = KalturaCortexApiDistributionClientPlugin()
        return KalturaCortexApiDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaCortexApiDistributionCaptionAction': KalturaCortexApiDistributionCaptionAction,
            'KalturaCortexApiDistributionProfileOrderBy': KalturaCortexApiDistributionProfileOrderBy,
            'KalturaCortexApiDistributionProviderOrderBy': KalturaCortexApiDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaCortexApiCaptionDistributionInfo': KalturaCortexApiCaptionDistributionInfo,
            'KalturaCortexApiDistributionProvider': KalturaCortexApiDistributionProvider,
            'KalturaCortexApiDistributionJobProviderData': KalturaCortexApiDistributionJobProviderData,
            'KalturaCortexApiDistributionProfile': KalturaCortexApiDistributionProfile,
            'KalturaCortexApiDistributionProviderBaseFilter': KalturaCortexApiDistributionProviderBaseFilter,
            'KalturaCortexApiDistributionProviderFilter': KalturaCortexApiDistributionProviderFilter,
            'KalturaCortexApiDistributionProfileBaseFilter': KalturaCortexApiDistributionProfileBaseFilter,
            'KalturaCortexApiDistributionProfileFilter': KalturaCortexApiDistributionProfileFilter,
        }

    # @return string
    def getName(self):
        return 'cortexApiDistribution'

