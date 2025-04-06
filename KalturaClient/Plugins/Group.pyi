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
from .ElasticSearch import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaGroupProcessStatus(object):
    NONE = 0
    PROCESSING = 1

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaESearchGroupFieldName(object):
    CAPABILITIES = "capabilities"
    COMPANY = "company"
    COUNTRY = "country"
    CREATED_AT = "created_at"
    EMAIL = "email"
    EXTERNAL_ID = "external_id"
    FIRST_NAME = "first_name"
    FULL_NAME = "full_name"
    GROUP_IDS = "group_ids"
    IS_ADMIN = "is_admin"
    IS_HASHED = "is_hashed"
    LAST_NAME = "last_name"
    LOGIN_ENABLED = "login_enabled"
    PERMISSION_NAMES = "permission_names"
    ROLE_IDS = "role_ids"
    SCREEN_NAME = "screen_name"
    TAGS = "tags"
    TITLE = "title"
    UPDATED_AT = "updated_at"
    USER_ID = "user_id"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaESearchGroupOrderByFieldName(object):
    CREATED_AT = "created_at"
    FULL_NAME = "full_name"
    MEMBERS_COUNT = "members_count"
    USER_ID = "puser_id"
    SCREEN_NAME = "screen_name"
    UPDATED_AT = "updated_at"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaESearchGroupBaseItem(KalturaESearchBaseItem):
    def __init__(self): ...
        pass

class KalturaGroup(KalturaBaseUser):
    membersCount: int
    processStatus: KalturaGroupProcessStatus
    groupType: KalturaGroupType
    def __init__(self,
            id: str = NotImplemented,
            partnerId: int = NotImplemented,
            screenName: str = NotImplemented,
            fullName: str = NotImplemented,
            email: str = NotImplemented,
            country: str = NotImplemented,
            state: str = NotImplemented,
            city: str = NotImplemented,
            zip: str = NotImplemented,
            thumbnailUrl: str = NotImplemented,
            description: str = NotImplemented,
            tags: str = NotImplemented,
            adminTags: str = NotImplemented,
            status: KalturaUserStatus = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerData: str = NotImplemented,
            indexedPartnerDataInt: int = NotImplemented,
            indexedPartnerDataString: str = NotImplemented,
            storageSize: int = NotImplemented,
            language: KalturaLanguageCode = NotImplemented,
            lastLoginTime: int = NotImplemented,
            statusUpdatedAt: int = NotImplemented,
            deletedAt: int = NotImplemented,
            allowedPartnerIds: str = NotImplemented,
            allowedPartnerPackages: str = NotImplemented,
            userMode: KalturaUserMode = NotImplemented,
            capabilities: List[KalturaUserCapability] = NotImplemented,
            membersCount: int = NotImplemented,
            processStatus: KalturaGroupProcessStatus = NotImplemented,
            groupType: KalturaGroupType = NotImplemented): ...

    def getMembersCount(self) -> int: ...
    def getProcessStatus(self) -> KalturaGroupProcessStatus: ...
    def setProcessStatus(self, newProcessStatus: KalturaGroupProcessStatus) -> None: ...
    def getGroupType(self) -> KalturaGroupType: ...
    def setGroupType(self, newGroupType: KalturaGroupType) -> None: ...

class KalturaESearchGroupOperator(KalturaESearchGroupBaseItem):
    operator: KalturaESearchOperatorType
    searchItems: List[KalturaESearchGroupBaseItem]
    def __init__(self,
            operator: KalturaESearchOperatorType = NotImplemented,
            searchItems: List[KalturaESearchGroupBaseItem] = NotImplemented): ...

    def getOperator(self) -> KalturaESearchOperatorType: ...
    def setOperator(self, newOperator: KalturaESearchOperatorType) -> None: ...
    def getSearchItems(self) -> List[KalturaESearchGroupBaseItem]: ...
    def setSearchItems(self, newSearchItems: List[KalturaESearchGroupBaseItem]) -> None: ...

class KalturaGroupListResponse(KalturaListResponse):
    objects: List[KalturaGroup]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaGroup] = NotImplemented): ...

    def getObjects(self) -> List[KalturaGroup]: ...

class KalturaESearchAbstractGroupItem(KalturaESearchGroupBaseItem):
    searchTerm: str
    itemType: KalturaESearchItemType
    range: KalturaESearchRange
    addHighlight: bool
    def __init__(self,
            searchTerm: str = NotImplemented,
            itemType: KalturaESearchItemType = NotImplemented,
            range: KalturaESearchRange = NotImplemented,
            addHighlight: bool = NotImplemented): ...

    def getSearchTerm(self) -> str: ...
    def setSearchTerm(self, newSearchTerm: str) -> None: ...
    def getItemType(self) -> KalturaESearchItemType: ...
    def setItemType(self, newItemType: KalturaESearchItemType) -> None: ...
    def getRange(self) -> KalturaESearchRange: ...
    def setRange(self, newRange: KalturaESearchRange) -> None: ...
    def getAddHighlight(self) -> bool: ...
    def setAddHighlight(self, newAddHighlight: bool) -> None: ...

class KalturaESearchGroupItem(KalturaESearchAbstractGroupItem):
    fieldName: KalturaESearchGroupFieldName
    def __init__(self,
            searchTerm: str = NotImplemented,
            itemType: KalturaESearchItemType = NotImplemented,
            range: KalturaESearchRange = NotImplemented,
            addHighlight: bool = NotImplemented,
            fieldName: KalturaESearchGroupFieldName = NotImplemented): ...

    def getFieldName(self) -> KalturaESearchGroupFieldName: ...
    def setFieldName(self, newFieldName: KalturaESearchGroupFieldName) -> None: ...

class KalturaESearchGroupMetadataItem(KalturaESearchAbstractGroupItem):
    xpath: str
    metadataProfileId: int
    metadataFieldId: int
    def __init__(self,
            searchTerm: str = NotImplemented,
            itemType: KalturaESearchItemType = NotImplemented,
            range: KalturaESearchRange = NotImplemented,
            addHighlight: bool = NotImplemented,
            xpath: str = NotImplemented,
            metadataProfileId: int = NotImplemented,
            metadataFieldId: int = NotImplemented): ...

    def getXpath(self) -> str: ...
    def setXpath(self, newXpath: str) -> None: ...
    def getMetadataProfileId(self) -> int: ...
    def setMetadataProfileId(self, newMetadataProfileId: int) -> None: ...
    def getMetadataFieldId(self) -> int: ...
    def setMetadataFieldId(self, newMetadataFieldId: int) -> None: ...

class KalturaGroupFilter(KalturaUserFilter):
    groupType: KalturaGroupType
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            screenNameLike: str = NotImplemented,
            screenNameStartsWith: str = NotImplemented,
            emailLike: str = NotImplemented,
            emailStartsWith: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            statusEqual: KalturaUserStatus = NotImplemented,
            statusIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            typeEqual: KalturaUserType = NotImplemented,
            typeIn: str = NotImplemented,
            isAdminEqual: KalturaNullableBoolean = NotImplemented,
            firstNameStartsWith: str = NotImplemented,
            lastNameStartsWith: str = NotImplemented,
            idOrScreenNameStartsWith: str = NotImplemented,
            loginEnabledEqual: KalturaNullableBoolean = NotImplemented,
            roleIdEqual: str = NotImplemented,
            roleIdsEqual: str = NotImplemented,
            roleIdsIn: str = NotImplemented,
            firstNameOrLastNameStartsWith: str = NotImplemented,
            permissionNamesMultiLikeOr: str = NotImplemented,
            permissionNamesMultiLikeAnd: str = NotImplemented,
            groupType: KalturaGroupType = NotImplemented): ...

    def getGroupType(self) -> KalturaGroupType: ...
    def setGroupType(self, newGroupType: KalturaGroupType) -> None: ...

class KalturaGroupService(KalturaServiceBase):
    def add(self, group: KalturaGroup) -> KalturaGroup: ...
    def clone(self, originalGroupId: str, newGroupId: str, newGroupName: str = NotImplemented) -> KalturaGroup: ...
    def delete(self, groupId: str) -> KalturaGroup: ...
    def get(self, groupId: str) -> KalturaGroup: ...
    def list(self, filter: KalturaGroupFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaGroupListResponse: ...
    def update(self, groupId: str, group: KalturaGroup) -> KalturaGroup: ...

class KalturaGroupClientPluginServicesProxy:
    group: KalturaGroupService