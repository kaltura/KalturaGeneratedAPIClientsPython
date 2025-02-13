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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaKontikiStorageProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaKontikiStorageProfile(KalturaStorageProfile):
    serviceToken: str
    def __init__(self,
            id: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            desciption: str = NotImplemented,
            status: KalturaStorageProfileStatus = NotImplemented,
            protocol: KalturaStorageProfileProtocol = NotImplemented,
            storageUrl: str = NotImplemented,
            storageBaseDir: str = NotImplemented,
            pathPrefix: str = NotImplemented,
            storageUsername: str = NotImplemented,
            storagePassword: str = NotImplemented,
            storageFtpPassiveMode: bool = NotImplemented,
            minFileSize: int = NotImplemented,
            maxFileSize: int = NotImplemented,
            flavorParamsIds: str = NotImplemented,
            maxConcurrentConnections: int = NotImplemented,
            pathManagerClass: str = NotImplemented,
            pathManagerParams: List[KalturaKeyValue] = NotImplemented,
            trigger: int = NotImplemented,
            deliveryPriority: int = NotImplemented,
            deliveryStatus: KalturaStorageProfileDeliveryStatus = NotImplemented,
            readyBehavior: KalturaStorageProfileReadyBehavior = NotImplemented,
            allowAutoDelete: int = NotImplemented,
            createFileLink: bool = NotImplemented,
            rules: List[KalturaRule] = NotImplemented,
            deliveryProfileIds: List[KalturaKeyValue] = NotImplemented,
            privateKey: str = NotImplemented,
            publicKey: str = NotImplemented,
            passPhrase: str = NotImplemented,
            port: int = NotImplemented,
            shouldExportThumbs: bool = NotImplemented,
            packagerUrl: str = NotImplemented,
            exportPeriodically: bool = NotImplemented,
            excludedFlavorParamsIds: str = NotImplemented,
            shouldExportCaptions: bool = NotImplemented,
            excludedEntryTypes: str = NotImplemented,
            additionalInfo: List[KalturaKeyValue] = NotImplemented,
            serviceToken: str = NotImplemented): ...

    def getServiceToken(self) -> str: ...
    def setServiceToken(self, newServiceToken: str) -> None: ...

class KalturaKontikiStorageDeleteJobData(KalturaStorageDeleteJobData):
    contentMoid: str
    serviceToken: str
    def __init__(self,
            serverUrl: str = NotImplemented,
            serverUsername: str = NotImplemented,
            serverPassword: str = NotImplemented,
            serverPrivateKey: str = NotImplemented,
            serverPublicKey: str = NotImplemented,
            serverPassPhrase: str = NotImplemented,
            ftpPassiveMode: bool = NotImplemented,
            srcFileSyncLocalPath: str = NotImplemented,
            srcFileEncryptionKey: str = NotImplemented,
            srcFileSyncId: str = NotImplemented,
            destFileSyncStoredPath: str = NotImplemented,
            contentMoid: str = NotImplemented,
            serviceToken: str = NotImplemented): ...

    def getContentMoid(self) -> str: ...
    def setContentMoid(self, newContentMoid: str) -> None: ...
    def getServiceToken(self) -> str: ...
    def setServiceToken(self, newServiceToken: str) -> None: ...

class KalturaKontikiStorageExportJobData(KalturaStorageExportJobData):
    flavorAssetId: str
    contentMoid: str
    serviceToken: str
    def __init__(self,
            serverUrl: str = NotImplemented,
            serverUsername: str = NotImplemented,
            serverPassword: str = NotImplemented,
            serverPrivateKey: str = NotImplemented,
            serverPublicKey: str = NotImplemented,
            serverPassPhrase: str = NotImplemented,
            ftpPassiveMode: bool = NotImplemented,
            srcFileSyncLocalPath: str = NotImplemented,
            srcFileEncryptionKey: str = NotImplemented,
            srcFileSyncId: str = NotImplemented,
            destFileSyncStoredPath: str = NotImplemented,
            force: bool = NotImplemented,
            createLink: bool = NotImplemented,
            assetId: str = NotImplemented,
            externalUrl: str = NotImplemented,
            port: int = NotImplemented,
            flavorAssetId: str = NotImplemented,
            contentMoid: str = NotImplemented,
            serviceToken: str = NotImplemented): ...

    def getFlavorAssetId(self) -> str: ...
    def setFlavorAssetId(self, newFlavorAssetId: str) -> None: ...
    def getContentMoid(self) -> str: ...
    def setContentMoid(self, newContentMoid: str) -> None: ...
    def getServiceToken(self) -> str: ...
    def setServiceToken(self, newServiceToken: str) -> None: ...

class KalturaKontikiStorageProfileBaseFilter(KalturaStorageProfileFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaStorageProfileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            protocolEqual: KalturaStorageProfileProtocol = NotImplemented,
            protocolIn: str = NotImplemented): ...
        pass

class KalturaKontikiStorageProfileFilter(KalturaKontikiStorageProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaStorageProfileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            protocolEqual: KalturaStorageProfileProtocol = NotImplemented,
            protocolIn: str = NotImplemented): ...
        pass

class KalturaKontikiClientPluginServicesProxy: