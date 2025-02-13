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
from .ContentDistribution import *
from .Transcript import *
from .Metadata import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaPushToNewsDistributionProvider(KalturaDistributionProvider):
    def __init__(self,
            type: KalturaDistributionProviderType = NotImplemented,
            name: str = NotImplemented,
            scheduleUpdateEnabled: bool = NotImplemented,
            availabilityUpdateEnabled: bool = NotImplemented,
            deleteInsteadUpdate: bool = NotImplemented,
            intervalBeforeSunrise: int = NotImplemented,
            intervalBeforeSunset: int = NotImplemented,
            updateRequiredEntryFields: str = NotImplemented,
            updateRequiredMetadataXPaths: str = NotImplemented): ...
        pass

class KalturaPushToNewsDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    currentVersion: int
    bodyParamContent: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            currentVersion: int = NotImplemented,
            bodyParamContent: str = NotImplemented): ...

    def getCurrentVersion(self) -> int: ...
    def setCurrentVersion(self, newCurrentVersion: int) -> None: ...
    def getBodyParamContent(self) -> str: ...
    def setBodyParamContent(self, newBodyParamContent: str) -> None: ...

class KalturaPushToNewsDistributionProfile(KalturaConfigurableDistributionProfile):
    protocol: KalturaDistributionProtocol
    host: str
    ips: str
    port: int
    basePath: str
    username: str
    password: str
    namedItem: str
    certificateKey: str
    bodyXslt: str
    recentNewsTimeInterval: int
    def __init__(self,
            id: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerId: int = NotImplemented,
            providerType: KalturaDistributionProviderType = NotImplemented,
            name: str = NotImplemented,
            status: KalturaDistributionProfileStatus = NotImplemented,
            submitEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            updateEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            deleteEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            reportEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            autoCreateFlavors: str = NotImplemented,
            autoCreateThumb: str = NotImplemented,
            optionalFlavorParamsIds: str = NotImplemented,
            requiredFlavorParamsIds: str = NotImplemented,
            optionalThumbDimensions: List[KalturaDistributionThumbDimensions] = NotImplemented,
            requiredThumbDimensions: List[KalturaDistributionThumbDimensions] = NotImplemented,
            optionalAssetDistributionRules: List[KalturaAssetDistributionRule] = NotImplemented,
            requiredAssetDistributionRules: List[KalturaAssetDistributionRule] = NotImplemented,
            sunriseDefaultOffset: int = NotImplemented,
            sunsetDefaultOffset: int = NotImplemented,
            recommendedStorageProfileForDownload: int = NotImplemented,
            recommendedDcForDownload: int = NotImplemented,
            recommendedDcForExecute: int = NotImplemented,
            distributeTrigger: KalturaDistributeTrigger = NotImplemented,
            supportImageEntry: bool = NotImplemented,
            fieldConfigArray: List[KalturaDistributionFieldConfig] = NotImplemented,
            itemXpathsToExtend: List[KalturaExtendingItemMrssParameter] = NotImplemented,
            useCategoryEntries: bool = NotImplemented,
            protocol: KalturaDistributionProtocol = NotImplemented,
            host: str = NotImplemented,
            ips: str = NotImplemented,
            port: int = NotImplemented,
            basePath: str = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            namedItem: str = NotImplemented,
            certificateKey: str = NotImplemented,
            bodyXslt: str = NotImplemented,
            recentNewsTimeInterval: int = NotImplemented): ...

    def getProtocol(self) -> KalturaDistributionProtocol: ...
    def setProtocol(self, newProtocol: KalturaDistributionProtocol) -> None: ...
    def getHost(self) -> str: ...
    def setHost(self, newHost: str) -> None: ...
    def getIps(self) -> str: ...
    def setIps(self, newIps: str) -> None: ...
    def getPort(self) -> int: ...
    def setPort(self, newPort: int) -> None: ...
    def getBasePath(self) -> str: ...
    def setBasePath(self, newBasePath: str) -> None: ...
    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getNamedItem(self) -> str: ...
    def setNamedItem(self, newNamedItem: str) -> None: ...
    def getCertificateKey(self) -> str: ...
    def setCertificateKey(self, newCertificateKey: str) -> None: ...
    def getBodyXslt(self) -> str: ...
    def setBodyXslt(self, newBodyXslt: str) -> None: ...
    def getRecentNewsTimeInterval(self) -> int: ...
    def setRecentNewsTimeInterval(self, newRecentNewsTimeInterval: int) -> None: ...

class KalturaPushToNewsDistributionClientPluginServicesProxy: