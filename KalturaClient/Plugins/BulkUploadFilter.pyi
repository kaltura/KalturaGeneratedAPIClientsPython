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
from .BulkUpload import *
from .BulkUploadXml import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaBulkServiceFilterDataBase(KalturaBulkServiceData):
    filter: KalturaFilter
    def __init__(self,
            filter: KalturaFilter = NotImplemented): ...

    def getFilter(self) -> KalturaFilter: ...
    def setFilter(self, newFilter: KalturaFilter) -> None: ...

class KalturaBulkUploadResultJob(KalturaBulkUploadResult):
    jobObjectId: int
    def __init__(self,
            id: int = NotImplemented,
            bulkUploadJobId: int = NotImplemented,
            lineIndex: int = NotImplemented,
            partnerId: int = NotImplemented,
            status: KalturaBulkUploadResultStatus = NotImplemented,
            action: KalturaBulkUploadAction = NotImplemented,
            objectId: str = NotImplemented,
            objectStatus: int = NotImplemented,
            bulkUploadResultObjectType: KalturaBulkUploadObjectType = NotImplemented,
            rowData: str = NotImplemented,
            partnerData: str = NotImplemented,
            objectErrorDescription: str = NotImplemented,
            pluginsData: List[KalturaBulkUploadPluginData] = NotImplemented,
            errorDescription: str = NotImplemented,
            errorCode: str = NotImplemented,
            errorType: int = NotImplemented,
            jobObjectId: int = NotImplemented): ...

    def getJobObjectId(self) -> int: ...
    def setJobObjectId(self, newJobObjectId: int) -> None: ...

class KalturaBulkServiceFilterData(KalturaBulkServiceFilterDataBase):
    templateObject: KalturaObjectBase
    def __init__(self,
            filter: KalturaFilter = NotImplemented,
            templateObject: KalturaObjectBase = NotImplemented): ...

    def getTemplateObject(self) -> KalturaObjectBase: ...
    def setTemplateObject(self, newTemplateObject: KalturaObjectBase) -> None: ...

class KalturaBulkUploadFilterJobData(KalturaBulkUploadJobData):
    filter: KalturaFilter
    templateObject: KalturaObjectBase
    def __init__(self,
            userId: str = NotImplemented,
            uploadedBy: str = NotImplemented,
            conversionProfileId: int = NotImplemented,
            resultsFileLocalPath: str = NotImplemented,
            resultsFileUrl: str = NotImplemented,
            numOfEntries: int = NotImplemented,
            numOfObjects: int = NotImplemented,
            filePath: str = NotImplemented,
            bulkUploadObjectType: KalturaBulkUploadObjectType = NotImplemented,
            fileName: str = NotImplemented,
            objectData: KalturaBulkUploadObjectData = NotImplemented,
            type: KalturaBulkUploadType = NotImplemented,
            emailRecipients: str = NotImplemented,
            numOfErrorObjects: int = NotImplemented,
            privileges: str = NotImplemented,
            filter: KalturaFilter = NotImplemented,
            templateObject: KalturaObjectBase = NotImplemented): ...

    def getFilter(self) -> KalturaFilter: ...
    def setFilter(self, newFilter: KalturaFilter) -> None: ...
    def getTemplateObject(self) -> KalturaObjectBase: ...
    def setTemplateObject(self, newTemplateObject: KalturaObjectBase) -> None: ...

class KalturaBulkUploadFilterClientPluginServicesProxy: