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

class KalturaBumper(KalturaObjectBase):
    entryId: str
    url: str
    sources: List[KalturaPlaybackSource]
    def __init__(self,
            entryId: str = NotImplemented,
            url: str = NotImplemented,
            sources: List[KalturaPlaybackSource] = NotImplemented): ...

    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getUrl(self) -> str: ...
    def setUrl(self, newUrl: str) -> None: ...
    def getSources(self) -> List[KalturaPlaybackSource]: ...

class KalturaBumperService(KalturaServiceBase):
    def add(self, entryId: str, bumper: KalturaBumper) -> KalturaBumper: ...
    def delete(self, entryId: str) -> KalturaBumper: ...
    def get(self, entryId: str) -> KalturaBumper: ...
    def update(self, entryId: str, bumper: KalturaBumper) -> KalturaBumper: ...

class KalturaBumperClientPluginServicesProxy:
    bumper: KalturaBumperService