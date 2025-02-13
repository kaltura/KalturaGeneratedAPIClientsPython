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

class KalturaTag(KalturaObjectBase):
    id: int
    tag: str
    taggedObjectType: KalturaTaggedObjectType
    partnerId: int
    instanceCount: int
    createdAt: int
    updatedAt: int
    def __init__(self,
            id: int = NotImplemented,
            tag: str = NotImplemented,
            taggedObjectType: KalturaTaggedObjectType = NotImplemented,
            partnerId: int = NotImplemented,
            instanceCount: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented): ...

    def getId(self) -> int: ...
    def getTag(self) -> str: ...
    def getTaggedObjectType(self) -> KalturaTaggedObjectType: ...
    def getPartnerId(self) -> int: ...
    def getInstanceCount(self) -> int: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...

class KalturaIndexTagsByPrivacyContextJobData(KalturaJobData):
    changedCategoryId: int
    deletedPrivacyContexts: str
    addedPrivacyContexts: str
    def __init__(self,
            changedCategoryId: int = NotImplemented,
            deletedPrivacyContexts: str = NotImplemented,
            addedPrivacyContexts: str = NotImplemented): ...

    def getChangedCategoryId(self) -> int: ...
    def setChangedCategoryId(self, newChangedCategoryId: int) -> None: ...
    def getDeletedPrivacyContexts(self) -> str: ...
    def setDeletedPrivacyContexts(self, newDeletedPrivacyContexts: str) -> None: ...
    def getAddedPrivacyContexts(self) -> str: ...
    def setAddedPrivacyContexts(self, newAddedPrivacyContexts: str) -> None: ...

class KalturaTagFilter(KalturaFilter):
    objectTypeEqual: KalturaTaggedObjectType
    objectTypeIn: str
    tagEqual: str
    tagStartsWith: str
    instanceCountEqual: int
    instanceCountIn: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            objectTypeEqual: KalturaTaggedObjectType = NotImplemented,
            objectTypeIn: str = NotImplemented,
            tagEqual: str = NotImplemented,
            tagStartsWith: str = NotImplemented,
            instanceCountEqual: int = NotImplemented,
            instanceCountIn: int = NotImplemented): ...

    def getObjectTypeEqual(self) -> KalturaTaggedObjectType: ...
    def setObjectTypeEqual(self, newObjectTypeEqual: KalturaTaggedObjectType) -> None: ...
    def getObjectTypeIn(self) -> str: ...
    def setObjectTypeIn(self, newObjectTypeIn: str) -> None: ...
    def getTagEqual(self) -> str: ...
    def setTagEqual(self, newTagEqual: str) -> None: ...
    def getTagStartsWith(self) -> str: ...
    def setTagStartsWith(self, newTagStartsWith: str) -> None: ...
    def getInstanceCountEqual(self) -> int: ...
    def setInstanceCountEqual(self, newInstanceCountEqual: int) -> None: ...
    def getInstanceCountIn(self) -> int: ...
    def setInstanceCountIn(self, newInstanceCountIn: int) -> None: ...

class KalturaTagListResponse(KalturaListResponse):
    objects: List[KalturaTag]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaTag] = NotImplemented): ...

    def getObjects(self) -> List[KalturaTag]: ...

class KalturaTagService(KalturaServiceBase):
    def deletePending(self) -> int: ...
    def indexCategoryEntryTags(self, categoryId: int, pcToDecrement: str, pcToIncrement: str) -> None: ...
    def search(self, tagFilter: KalturaTagFilter, pager: KalturaFilterPager = NotImplemented) -> KalturaTagListResponse: ...

class KalturaTagSearchClientPluginServicesProxy:
    tag: KalturaTagService