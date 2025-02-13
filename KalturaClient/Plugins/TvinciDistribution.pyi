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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaTvinciAssetsType(object):
    REGULAR = 1
    VIRTUAL = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaTvinciDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaTvinciDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaTvinciDistributionTag(KalturaObjectBase):
    tagname: str
    extension: str
    protocol: str
    format: str
    filename: str
    ppvmodule: str
    def __init__(self,
            tagname: str = NotImplemented,
            extension: str = NotImplemented,
            protocol: str = NotImplemented,
            format: str = NotImplemented,
            filename: str = NotImplemented,
            ppvmodule: str = NotImplemented): ...

    def getTagname(self) -> str: ...
    def setTagname(self, newTagname: str) -> None: ...
    def getExtension(self) -> str: ...
    def setExtension(self, newExtension: str) -> None: ...
    def getProtocol(self) -> str: ...
    def setProtocol(self, newProtocol: str) -> None: ...
    def getFormat(self) -> str: ...
    def setFormat(self, newFormat: str) -> None: ...
    def getFilename(self) -> str: ...
    def setFilename(self, newFilename: str) -> None: ...
    def getPpvmodule(self) -> str: ...
    def setPpvmodule(self, newPpvmodule: str) -> None: ...

class KalturaTvinciDistributionProvider(KalturaDistributionProvider):
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

class KalturaTvinciDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    xml: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            xml: str = NotImplemented): ...

    def getXml(self) -> str: ...
    def setXml(self, newXml: str) -> None: ...

class KalturaTvinciDistributionProfile(KalturaConfigurableDistributionProfile):
    ingestUrl: str
    username: str
    password: str
    tags: List[KalturaTvinciDistributionTag]
    xsltFile: str
    innerType: str
    assetsType: KalturaTvinciAssetsType
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
            ingestUrl: str = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            tags: List[KalturaTvinciDistributionTag] = NotImplemented,
            xsltFile: str = NotImplemented,
            innerType: str = NotImplemented,
            assetsType: KalturaTvinciAssetsType = NotImplemented): ...

    def getIngestUrl(self) -> str: ...
    def setIngestUrl(self, newIngestUrl: str) -> None: ...
    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getTags(self) -> List[KalturaTvinciDistributionTag]: ...
    def setTags(self, newTags: List[KalturaTvinciDistributionTag]) -> None: ...
    def getXsltFile(self) -> str: ...
    def setXsltFile(self, newXsltFile: str) -> None: ...
    def getInnerType(self) -> str: ...
    def setInnerType(self, newInnerType: str) -> None: ...
    def getAssetsType(self) -> KalturaTvinciAssetsType: ...
    def setAssetsType(self, newAssetsType: KalturaTvinciAssetsType) -> None: ...

class KalturaTvinciDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaTvinciDistributionProviderFilter(KalturaTvinciDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaTvinciDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaDistributionProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaTvinciDistributionProfileFilter(KalturaTvinciDistributionProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaDistributionProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaTvinciDistributionClientPluginServicesProxy: