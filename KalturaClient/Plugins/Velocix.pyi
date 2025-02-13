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

class KalturaVelocixProvisionJobData(KalturaProvisionJobData):
    provisioningParams: List[KalturaKeyValue]
    userName: str
    password: str
    def __init__(self,
            streamID: str = NotImplemented,
            backupStreamID: str = NotImplemented,
            rtmp: str = NotImplemented,
            encoderIP: str = NotImplemented,
            backupEncoderIP: str = NotImplemented,
            encoderPassword: str = NotImplemented,
            encoderUsername: str = NotImplemented,
            endDate: int = NotImplemented,
            returnVal: str = NotImplemented,
            mediaType: int = NotImplemented,
            primaryBroadcastingUrl: str = NotImplemented,
            secondaryBroadcastingUrl: str = NotImplemented,
            streamName: str = NotImplemented,
            provisioningParams: List[KalturaKeyValue] = NotImplemented,
            userName: str = NotImplemented,
            password: str = NotImplemented): ...

    def getProvisioningParams(self) -> List[KalturaKeyValue]: ...
    def setProvisioningParams(self, newProvisioningParams: List[KalturaKeyValue]) -> None: ...
    def getUserName(self) -> str: ...
    def setUserName(self, newUserName: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...

class KalturaVelocixClientPluginServicesProxy: