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
from .FileSync import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaBaseInteractivity(KalturaObjectBase):
    data: str
    version: int
    entryId: str
    updatedAt: int
    def __init__(self,
            data: str = NotImplemented,
            version: int = NotImplemented,
            entryId: str = NotImplemented,
            updatedAt: int = NotImplemented): ...

    def getData(self) -> str: ...
    def setData(self, newData: str) -> None: ...
    def getVersion(self) -> int: ...
    def getEntryId(self) -> str: ...
    def getUpdatedAt(self) -> int: ...

class KalturaInteractivityDataFieldsFilter(KalturaObjectBase):
    fields: str
    def __init__(self,
            fields: str = NotImplemented): ...

    def getFields(self) -> str: ...
    def setFields(self, newFields: str) -> None: ...

class KalturaInteractivityRootFilter(KalturaInteractivityDataFieldsFilter):
    def __init__(self,
            fields: str = NotImplemented): ...
        pass

class KalturaInteractivityNodeFilter(KalturaInteractivityDataFieldsFilter):
    def __init__(self,
            fields: str = NotImplemented): ...
        pass

class KalturaInteractivityInteractionFilter(KalturaInteractivityDataFieldsFilter):
    def __init__(self,
            fields: str = NotImplemented): ...
        pass

class KalturaInteractivityDataFilter(KalturaObjectBase):
    rootFilter: KalturaInteractivityRootFilter
    nodeFilter: KalturaInteractivityNodeFilter
    interactionFilter: KalturaInteractivityInteractionFilter
    def __init__(self,
            rootFilter: KalturaInteractivityRootFilter = NotImplemented,
            nodeFilter: KalturaInteractivityNodeFilter = NotImplemented,
            interactionFilter: KalturaInteractivityInteractionFilter = NotImplemented): ...

    def getRootFilter(self) -> KalturaInteractivityRootFilter: ...
    def setRootFilter(self, newRootFilter: KalturaInteractivityRootFilter) -> None: ...
    def getNodeFilter(self) -> KalturaInteractivityNodeFilter: ...
    def setNodeFilter(self, newNodeFilter: KalturaInteractivityNodeFilter) -> None: ...
    def getInteractionFilter(self) -> KalturaInteractivityInteractionFilter: ...
    def setInteractionFilter(self, newInteractionFilter: KalturaInteractivityInteractionFilter) -> None: ...

class KalturaInteractivity(KalturaBaseInteractivity):
    def __init__(self,
            data: str = NotImplemented,
            version: int = NotImplemented,
            entryId: str = NotImplemented,
            updatedAt: int = NotImplemented): ...
        pass

class KalturaVolatileInteractivity(KalturaBaseInteractivity):
    def __init__(self,
            data: str = NotImplemented,
            version: int = NotImplemented,
            entryId: str = NotImplemented,
            updatedAt: int = NotImplemented): ...
        pass

class KalturaInteractivityService(KalturaServiceBase):
    def add(self, entryId: str, kalturaInteractivity: KalturaInteractivity) -> KalturaInteractivity: ...
    def delete(self, entryId: str) -> None: ...
    def get(self, entryId: str, dataFilter: KalturaInteractivityDataFilter = NotImplemented) -> KalturaInteractivity: ...
    def update(self, entryId: str, version: int, kalturaInteractivity: KalturaInteractivity) -> KalturaInteractivity: ...

class KalturaVolatileInteractivityService(KalturaServiceBase):
    def add(self, entryId: str, kalturaVolatileInteractivity: KalturaVolatileInteractivity) -> KalturaVolatileInteractivity: ...
    def delete(self, entryId: str) -> None: ...
    def get(self, entryId: str) -> KalturaVolatileInteractivity: ...
    def update(self, entryId: str, version: int, kalturaVolatileInteractivity: KalturaVolatileInteractivity) -> KalturaVolatileInteractivity: ...

class KalturaInteractivityClientPluginServicesProxy:
    interactivity: KalturaInteractivityService
    volatileInteractivity: KalturaVolatileInteractivityService