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
from .Transcript import *
from .Metadata import *
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
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaPushToNewsDistributionProvider(KalturaDistributionProvider):
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
        self.fromXmlImpl(node, KalturaPushToNewsDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaPushToNewsDistributionProvider")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPushToNewsDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    def __init__(self,
            fieldValues = NotImplemented,
            currentVersion = NotImplemented,
            bodyParamContent = NotImplemented):
        KalturaConfigurableDistributionJobProviderData.__init__(self,
            fieldValues)

        # @var int
        self.currentVersion = currentVersion

        # @var str
        self.bodyParamContent = bodyParamContent


    PROPERTY_LOADERS = {
        'currentVersion': getXmlNodeInt, 
        'bodyParamContent': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionJobProviderData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushToNewsDistributionJobProviderData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionJobProviderData.toParams(self)
        kparams.put("objectType", "KalturaPushToNewsDistributionJobProviderData")
        kparams.addIntIfDefined("currentVersion", self.currentVersion)
        kparams.addStringIfDefined("bodyParamContent", self.bodyParamContent)
        return kparams

    def getCurrentVersion(self):
        return self.currentVersion

    def setCurrentVersion(self, newCurrentVersion):
        self.currentVersion = newCurrentVersion

    def getBodyParamContent(self):
        return self.bodyParamContent

    def setBodyParamContent(self, newBodyParamContent):
        self.bodyParamContent = newBodyParamContent


# @package Kaltura
# @subpackage Client
class KalturaPushToNewsDistributionProfile(KalturaConfigurableDistributionProfile):
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
            protocol = NotImplemented,
            host = NotImplemented,
            ips = NotImplemented,
            port = NotImplemented,
            basePath = NotImplemented,
            username = NotImplemented,
            password = NotImplemented,
            namedItem = NotImplemented,
            certificateKey = NotImplemented,
            bodyXslt = NotImplemented,
            recentNewsTimeInterval = NotImplemented):
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

        # @var KalturaDistributionProtocol
        # @insertonly
        self.protocol = protocol

        # @var str
        self.host = host

        # @var str
        self.ips = ips

        # @var int
        self.port = port

        # @var str
        self.basePath = basePath

        # @var str
        self.username = username

        # @var str
        self.password = password

        # @var str
        self.namedItem = namedItem

        # @var str
        self.certificateKey = certificateKey

        # @var str
        self.bodyXslt = bodyXslt

        # @var int
        self.recentNewsTimeInterval = recentNewsTimeInterval


    PROPERTY_LOADERS = {
        'protocol': (KalturaEnumsFactory.createInt, "KalturaDistributionProtocol"), 
        'host': getXmlNodeText, 
        'ips': getXmlNodeText, 
        'port': getXmlNodeInt, 
        'basePath': getXmlNodeText, 
        'username': getXmlNodeText, 
        'password': getXmlNodeText, 
        'namedItem': getXmlNodeText, 
        'certificateKey': getXmlNodeText, 
        'bodyXslt': getXmlNodeText, 
        'recentNewsTimeInterval': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushToNewsDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaPushToNewsDistributionProfile")
        kparams.addIntEnumIfDefined("protocol", self.protocol)
        kparams.addStringIfDefined("host", self.host)
        kparams.addStringIfDefined("ips", self.ips)
        kparams.addIntIfDefined("port", self.port)
        kparams.addStringIfDefined("basePath", self.basePath)
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("password", self.password)
        kparams.addStringIfDefined("namedItem", self.namedItem)
        kparams.addStringIfDefined("certificateKey", self.certificateKey)
        kparams.addStringIfDefined("bodyXslt", self.bodyXslt)
        kparams.addIntIfDefined("recentNewsTimeInterval", self.recentNewsTimeInterval)
        return kparams

    def getProtocol(self):
        return self.protocol

    def setProtocol(self, newProtocol):
        self.protocol = newProtocol

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getIps(self):
        return self.ips

    def setIps(self, newIps):
        self.ips = newIps

    def getPort(self):
        return self.port

    def setPort(self, newPort):
        self.port = newPort

    def getBasePath(self):
        return self.basePath

    def setBasePath(self, newBasePath):
        self.basePath = newBasePath

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getNamedItem(self):
        return self.namedItem

    def setNamedItem(self, newNamedItem):
        self.namedItem = newNamedItem

    def getCertificateKey(self):
        return self.certificateKey

    def setCertificateKey(self, newCertificateKey):
        self.certificateKey = newCertificateKey

    def getBodyXslt(self):
        return self.bodyXslt

    def setBodyXslt(self, newBodyXslt):
        self.bodyXslt = newBodyXslt

    def getRecentNewsTimeInterval(self):
        return self.recentNewsTimeInterval

    def setRecentNewsTimeInterval(self, newRecentNewsTimeInterval):
        self.recentNewsTimeInterval = newRecentNewsTimeInterval


########## services ##########
########## main ##########
class KalturaPushToNewsDistributionClientPlugin(KalturaClientPlugin):
    # KalturaPushToNewsDistributionClientPlugin
    instance = None

    # @return KalturaPushToNewsDistributionClientPlugin
    @staticmethod
    def get():
        if KalturaPushToNewsDistributionClientPlugin.instance == None:
            KalturaPushToNewsDistributionClientPlugin.instance = KalturaPushToNewsDistributionClientPlugin()
        return KalturaPushToNewsDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaPushToNewsDistributionProvider': KalturaPushToNewsDistributionProvider,
            'KalturaPushToNewsDistributionJobProviderData': KalturaPushToNewsDistributionJobProviderData,
            'KalturaPushToNewsDistributionProfile': KalturaPushToNewsDistributionProfile,
        }

    # @return string
    def getName(self):
        return 'pushToNewsDistribution'

