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
from .Integration import *
from .Voicebase import *
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
class KalturaDexterIntegrationJobProviderData(KalturaIntegrationJobProviderData):
    def __init__(self,
            metadataProfileId = NotImplemented,
            transcriptAssetId = NotImplemented,
            entryId = NotImplemented,
            voicebaseApiKey = NotImplemented,
            voicebaseApiPassword = NotImplemented):
        KalturaIntegrationJobProviderData.__init__(self)

        # ID of the metadata profile for the extracted term metadata
        # @var int
        self.metadataProfileId = metadataProfileId

        # ID of the transcript asset
        # @var str
        self.transcriptAssetId = transcriptAssetId

        # ID of the entry
        # @var str
        self.entryId = entryId

        # Voicebase API key to fetch transcript tokens
        # @var str
        self.voicebaseApiKey = voicebaseApiKey

        # Voicebase API password to fetch transcript tokens
        # @var str
        self.voicebaseApiPassword = voicebaseApiPassword


    PROPERTY_LOADERS = {
        'metadataProfileId': getXmlNodeInt, 
        'transcriptAssetId': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'voicebaseApiKey': getXmlNodeText, 
        'voicebaseApiPassword': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaIntegrationJobProviderData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDexterIntegrationJobProviderData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaIntegrationJobProviderData.toParams(self)
        kparams.put("objectType", "KalturaDexterIntegrationJobProviderData")
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addStringIfDefined("transcriptAssetId", self.transcriptAssetId)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("voicebaseApiKey", self.voicebaseApiKey)
        kparams.addStringIfDefined("voicebaseApiPassword", self.voicebaseApiPassword)
        return kparams

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getTranscriptAssetId(self):
        return self.transcriptAssetId

    def setTranscriptAssetId(self, newTranscriptAssetId):
        self.transcriptAssetId = newTranscriptAssetId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getVoicebaseApiKey(self):
        return self.voicebaseApiKey

    def setVoicebaseApiKey(self, newVoicebaseApiKey):
        self.voicebaseApiKey = newVoicebaseApiKey

    def getVoicebaseApiPassword(self):
        return self.voicebaseApiPassword

    def setVoicebaseApiPassword(self, newVoicebaseApiPassword):
        self.voicebaseApiPassword = newVoicebaseApiPassword


########## services ##########
########## main ##########
class KalturaDexterIntegrationClientPlugin(KalturaClientPlugin):
    # KalturaDexterIntegrationClientPlugin
    instance = None

    # @return KalturaDexterIntegrationClientPlugin
    @staticmethod
    def get():
        if KalturaDexterIntegrationClientPlugin.instance == None:
            KalturaDexterIntegrationClientPlugin.instance = KalturaDexterIntegrationClientPlugin()
        return KalturaDexterIntegrationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaDexterIntegrationJobProviderData': KalturaDexterIntegrationJobProviderData,
        }

    # @return string
    def getName(self):
        return 'dexterIntegration'

