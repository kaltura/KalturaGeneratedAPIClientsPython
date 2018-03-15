# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2018  Kaltura Inc.
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
class KalturaDeliveryProfileForensicWatermark(KalturaDeliveryProfile):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            type=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            streamerType=NotImplemented,
            url=NotImplemented,
            hostName=NotImplemented,
            status=NotImplemented,
            recognizer=NotImplemented,
            tokenizer=NotImplemented,
            isDefault=NotImplemented,
            parentId=NotImplemented,
            mediaProtocols=NotImplemented,
            priority=NotImplemented,
            extraParams=NotImplemented,
            supplementaryAssetsFilter=NotImplemented,
            internalUrl=NotImplemented,
            encryptionKey=NotImplemented,
            encryptionIv=NotImplemented,
            encryptionRegex=NotImplemented):
        KalturaDeliveryProfile.__init__(self,
            id,
            partnerId,
            name,
            type,
            systemName,
            description,
            createdAt,
            updatedAt,
            streamerType,
            url,
            hostName,
            status,
            recognizer,
            tokenizer,
            isDefault,
            parentId,
            mediaProtocols,
            priority,
            extraParams,
            supplementaryAssetsFilter)

        # The URL used to pull manifest from the server, keyed by dc id, asterisk means all dcs
        # @var array of KalturaKeyValue
        self.internalUrl = internalUrl

        # The key used to encrypt the URI (256 bits)
        # @var string
        self.encryptionKey = encryptionKey

        # The iv used to encrypt the URI (128 bits)
        # @var string
        self.encryptionIv = encryptionIv

        # The regex used to match the encrypted part of the URI (according to the 'encrypt' named group)
        # @var string
        self.encryptionRegex = encryptionRegex


    PROPERTY_LOADERS = {
        'internalUrl': (KalturaObjectFactory.createArray, 'KalturaKeyValue'), 
        'encryptionKey': getXmlNodeText, 
        'encryptionIv': getXmlNodeText, 
        'encryptionRegex': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDeliveryProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeliveryProfileForensicWatermark.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDeliveryProfile.toParams(self)
        kparams.put("objectType", "KalturaDeliveryProfileForensicWatermark")
        kparams.addArrayIfDefined("internalUrl", self.internalUrl)
        kparams.addStringIfDefined("encryptionKey", self.encryptionKey)
        kparams.addStringIfDefined("encryptionIv", self.encryptionIv)
        kparams.addStringIfDefined("encryptionRegex", self.encryptionRegex)
        return kparams

    def getInternalUrl(self):
        return self.internalUrl

    def setInternalUrl(self, newInternalUrl):
        self.internalUrl = newInternalUrl

    def getEncryptionKey(self):
        return self.encryptionKey

    def setEncryptionKey(self, newEncryptionKey):
        self.encryptionKey = newEncryptionKey

    def getEncryptionIv(self):
        return self.encryptionIv

    def setEncryptionIv(self, newEncryptionIv):
        self.encryptionIv = newEncryptionIv

    def getEncryptionRegex(self):
        return self.encryptionRegex

    def setEncryptionRegex(self, newEncryptionRegex):
        self.encryptionRegex = newEncryptionRegex


# @package Kaltura
# @subpackage Client
class KalturaForensicWatermarkAdvancedFilter(KalturaSearchItem):
    def __init__(self,
            watermarkId=NotImplemented):
        KalturaSearchItem.__init__(self)

        # @var int
        self.watermarkId = watermarkId


    PROPERTY_LOADERS = {
        'watermarkId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaForensicWatermarkAdvancedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaForensicWatermarkAdvancedFilter")
        kparams.addIntIfDefined("watermarkId", self.watermarkId)
        return kparams

    def getWatermarkId(self):
        return self.watermarkId

    def setWatermarkId(self, newWatermarkId):
        self.watermarkId = newWatermarkId


########## services ##########
########## main ##########
class KalturaForensicWatermarkClientPlugin(KalturaClientPlugin):
    # KalturaForensicWatermarkClientPlugin
    instance = None

    # @return KalturaForensicWatermarkClientPlugin
    @staticmethod
    def get():
        if KalturaForensicWatermarkClientPlugin.instance == None:
            KalturaForensicWatermarkClientPlugin.instance = KalturaForensicWatermarkClientPlugin()
        return KalturaForensicWatermarkClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaDeliveryProfileForensicWatermark': KalturaDeliveryProfileForensicWatermark,
            'KalturaForensicWatermarkAdvancedFilter': KalturaForensicWatermarkAdvancedFilter,
        }

    # @return string
    def getName(self):
        return 'forensicWatermark'

