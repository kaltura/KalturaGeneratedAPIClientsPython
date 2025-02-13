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

class KalturaCielo24Fidelity(object):
    MECHANICAL = "MECHANICAL"
    PREMIUM = "PREMIUM"
    PROFESSIONAL = "PROFESSIONAL"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaCielo24Priority(object):
    PRIORITY = "PRIORITY"
    STANDARD = "STANDARD"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaCielo24JobProviderData(KalturaIntegrationJobProviderData):
    entryId: str
    flavorAssetId: str
    captionAssetFormats: str
    priority: KalturaCielo24Priority
    fidelity: KalturaCielo24Fidelity
    username: str
    password: str
    baseUrl: str
    spokenLanguage: KalturaLanguage
    replaceMediaContent: bool
    additionalParameters: str
    def __init__(self,
            entryId: str = NotImplemented,
            flavorAssetId: str = NotImplemented,
            captionAssetFormats: str = NotImplemented,
            priority: KalturaCielo24Priority = NotImplemented,
            fidelity: KalturaCielo24Fidelity = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            baseUrl: str = NotImplemented,
            spokenLanguage: KalturaLanguage = NotImplemented,
            replaceMediaContent: bool = NotImplemented,
            additionalParameters: str = NotImplemented): ...

    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getFlavorAssetId(self) -> str: ...
    def setFlavorAssetId(self, newFlavorAssetId: str) -> None: ...
    def getCaptionAssetFormats(self) -> str: ...
    def setCaptionAssetFormats(self, newCaptionAssetFormats: str) -> None: ...
    def getPriority(self) -> KalturaCielo24Priority: ...
    def setPriority(self, newPriority: KalturaCielo24Priority) -> None: ...
    def getFidelity(self) -> KalturaCielo24Fidelity: ...
    def setFidelity(self, newFidelity: KalturaCielo24Fidelity) -> None: ...
    def getUsername(self) -> str: ...
    def getPassword(self) -> str: ...
    def getBaseUrl(self) -> str: ...
    def getSpokenLanguage(self) -> KalturaLanguage: ...
    def setSpokenLanguage(self, newSpokenLanguage: KalturaLanguage) -> None: ...
    def getReplaceMediaContent(self) -> bool: ...
    def setReplaceMediaContent(self, newReplaceMediaContent: bool) -> None: ...
    def getAdditionalParameters(self) -> str: ...
    def setAdditionalParameters(self, newAdditionalParameters: str) -> None: ...

class KalturaCielo24ClientPluginServicesProxy: