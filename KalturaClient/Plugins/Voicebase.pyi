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
from typing import List, IO, Any
from .Core import *
from .Integration import *
from .Transcript import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaVoicebaseJobProviderData(KalturaIntegrationJobProviderData):
    entryId: str
    flavorAssetId: str
    transcriptId: str
    captionAssetFormats: str
    apiKey: str
    apiPassword: str
    spokenLanguage: KalturaLanguage
    fileLocation: str
    replaceMediaContent: bool
    additionalParameters: str
    def __init__(self,
            entryId: str = NotImplemented,
            flavorAssetId: str = NotImplemented,
            transcriptId: str = NotImplemented,
            captionAssetFormats: str = NotImplemented,
            apiKey: str = NotImplemented,
            apiPassword: str = NotImplemented,
            spokenLanguage: KalturaLanguage = NotImplemented,
            fileLocation: str = NotImplemented,
            replaceMediaContent: bool = NotImplemented,
            additionalParameters: str = NotImplemented): ...

    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getFlavorAssetId(self) -> str: ...
    def setFlavorAssetId(self, newFlavorAssetId: str) -> None: ...
    def getTranscriptId(self) -> str: ...
    def setTranscriptId(self, newTranscriptId: str) -> None: ...
    def getCaptionAssetFormats(self) -> str: ...
    def setCaptionAssetFormats(self, newCaptionAssetFormats: str) -> None: ...
    def getApiKey(self) -> str: ...
    def getApiPassword(self) -> str: ...
    def getSpokenLanguage(self) -> KalturaLanguage: ...
    def setSpokenLanguage(self, newSpokenLanguage: KalturaLanguage) -> None: ...
    def getFileLocation(self) -> str: ...
    def getReplaceMediaContent(self) -> bool: ...
    def setReplaceMediaContent(self, newReplaceMediaContent: bool) -> None: ...
    def getAdditionalParameters(self) -> str: ...

class KalturaVoicebaseClientPluginServicesProxy: