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
class KalturaRainFocusDistributionProfileOrderBy(object):
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
class KalturaRainFocusDistributionProviderOrderBy(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionProvider(KalturaDistributionProvider):
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
        self.fromXmlImpl(node, KalturaRainFocusDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionProvider")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    def __init__(self,
            fieldValues = NotImplemented):
        KalturaConfigurableDistributionJobProviderData.__init__(self,
            fieldValues)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionJobProviderData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRainFocusDistributionJobProviderData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionJobProviderData.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionJobProviderData")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionProfile(KalturaConfigurableDistributionProfile):
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
            oauthTokenUrl = NotImplemented,
            videoPublishEndpointUrl = NotImplemented,
            oauthScope = NotImplemented,
            clientId = NotImplemented,
            clientSecretPrimary = NotImplemented,
            clientSecretSecondary = NotImplemented,
            activeSecret = NotImplemented,
            mediaType = NotImplemented,
            playerId = NotImplemented,
            metadataProfileId = NotImplemented,
            metadataFieldNames = NotImplemented):
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
        self.oauthTokenUrl = oauthTokenUrl

        # @var str
        self.videoPublishEndpointUrl = videoPublishEndpointUrl

        # @var str
        self.oauthScope = oauthScope

        # @var str
        self.clientId = clientId

        # @var str
        self.clientSecretPrimary = clientSecretPrimary

        # @var str
        self.clientSecretSecondary = clientSecretSecondary

        # @var str
        self.activeSecret = activeSecret

        # @var int
        self.mediaType = mediaType

        # @var str
        self.playerId = playerId

        # @var str
        self.metadataProfileId = metadataProfileId

        # @var str
        self.metadataFieldNames = metadataFieldNames


    PROPERTY_LOADERS = {
        'oauthTokenUrl': getXmlNodeText, 
        'videoPublishEndpointUrl': getXmlNodeText, 
        'oauthScope': getXmlNodeText, 
        'clientId': getXmlNodeText, 
        'clientSecretPrimary': getXmlNodeText, 
        'clientSecretSecondary': getXmlNodeText, 
        'activeSecret': getXmlNodeText, 
        'mediaType': getXmlNodeInt, 
        'playerId': getXmlNodeText, 
        'metadataProfileId': getXmlNodeText, 
        'metadataFieldNames': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRainFocusDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionProfile")
        kparams.addStringIfDefined("oauthTokenUrl", self.oauthTokenUrl)
        kparams.addStringIfDefined("videoPublishEndpointUrl", self.videoPublishEndpointUrl)
        kparams.addStringIfDefined("oauthScope", self.oauthScope)
        kparams.addStringIfDefined("clientId", self.clientId)
        kparams.addStringIfDefined("clientSecretPrimary", self.clientSecretPrimary)
        kparams.addStringIfDefined("clientSecretSecondary", self.clientSecretSecondary)
        kparams.addStringIfDefined("activeSecret", self.activeSecret)
        kparams.addIntIfDefined("mediaType", self.mediaType)
        kparams.addStringIfDefined("playerId", self.playerId)
        kparams.addStringIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addStringIfDefined("metadataFieldNames", self.metadataFieldNames)
        return kparams

    def getOauthTokenUrl(self):
        return self.oauthTokenUrl

    def setOauthTokenUrl(self, newOauthTokenUrl):
        self.oauthTokenUrl = newOauthTokenUrl

    def getVideoPublishEndpointUrl(self):
        return self.videoPublishEndpointUrl

    def setVideoPublishEndpointUrl(self, newVideoPublishEndpointUrl):
        self.videoPublishEndpointUrl = newVideoPublishEndpointUrl

    def getOauthScope(self):
        return self.oauthScope

    def setOauthScope(self, newOauthScope):
        self.oauthScope = newOauthScope

    def getClientId(self):
        return self.clientId

    def setClientId(self, newClientId):
        self.clientId = newClientId

    def getClientSecretPrimary(self):
        return self.clientSecretPrimary

    def setClientSecretPrimary(self, newClientSecretPrimary):
        self.clientSecretPrimary = newClientSecretPrimary

    def getClientSecretSecondary(self):
        return self.clientSecretSecondary

    def setClientSecretSecondary(self, newClientSecretSecondary):
        self.clientSecretSecondary = newClientSecretSecondary

    def getActiveSecret(self):
        return self.activeSecret

    def setActiveSecret(self, newActiveSecret):
        self.activeSecret = newActiveSecret

    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def getPlayerId(self):
        return self.playerId

    def setPlayerId(self, newPlayerId):
        self.playerId = newPlayerId

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getMetadataFieldNames(self):
        return self.metadataFieldNames

    def setMetadataFieldNames(self, newMetadataFieldNames):
        self.metadataFieldNames = newMetadataFieldNames


# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
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
        self.fromXmlImpl(node, KalturaRainFocusDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionProviderBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionProviderFilter(KalturaRainFocusDistributionProviderBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented):
        KalturaRainFocusDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRainFocusDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRainFocusDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRainFocusDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionProviderFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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
        self.fromXmlImpl(node, KalturaRainFocusDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionProfileBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRainFocusDistributionProfileFilter(KalturaRainFocusDistributionProfileBaseFilter):
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
        KalturaRainFocusDistributionProfileBaseFilter.__init__(self,
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
        KalturaRainFocusDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRainFocusDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRainFocusDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaRainFocusDistributionProfileFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaRainFocusDistributionClientPlugin(KalturaClientPlugin):
    # KalturaRainFocusDistributionClientPlugin
    instance = None

    # @return KalturaRainFocusDistributionClientPlugin
    @staticmethod
    def get():
        if KalturaRainFocusDistributionClientPlugin.instance == None:
            KalturaRainFocusDistributionClientPlugin.instance = KalturaRainFocusDistributionClientPlugin()
        return KalturaRainFocusDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaRainFocusDistributionProfileOrderBy': KalturaRainFocusDistributionProfileOrderBy,
            'KalturaRainFocusDistributionProviderOrderBy': KalturaRainFocusDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaRainFocusDistributionProvider': KalturaRainFocusDistributionProvider,
            'KalturaRainFocusDistributionJobProviderData': KalturaRainFocusDistributionJobProviderData,
            'KalturaRainFocusDistributionProfile': KalturaRainFocusDistributionProfile,
            'KalturaRainFocusDistributionProviderBaseFilter': KalturaRainFocusDistributionProviderBaseFilter,
            'KalturaRainFocusDistributionProviderFilter': KalturaRainFocusDistributionProviderFilter,
            'KalturaRainFocusDistributionProfileBaseFilter': KalturaRainFocusDistributionProfileBaseFilter,
            'KalturaRainFocusDistributionProfileFilter': KalturaRainFocusDistributionProfileFilter,
        }

    # @return string
    def getName(self):
        return 'rainFocusDistribution'

