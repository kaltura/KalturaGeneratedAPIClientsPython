# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2015  Kaltura Inc.
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
# @package Kaltura
# @subpackage Client
from Core import *
from ..Base import *

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaScheduledTaskProfileStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3
    SUSPENDED = 4
    DRY_RUN_ONLY = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaScheduledTaskProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    LAST_EXECUTION_STARTED_AT_ASC = "+lastExecutionStartedAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    LAST_EXECUTION_STARTED_AT_DESC = "-lastExecutionStartedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaScheduledTaskJobData(KalturaJobData):
    def __init__(self,
            maxResults=NotImplemented,
            resultsFilePath=NotImplemented,
            referenceTime=NotImplemented):
        KalturaJobData.__init__(self)

        # @var int
        self.maxResults = maxResults

        # @var string
        self.resultsFilePath = resultsFilePath

        # @var int
        self.referenceTime = referenceTime


    PROPERTY_LOADERS = {
        'maxResults': getXmlNodeInt, 
        'resultsFilePath': getXmlNodeText, 
        'referenceTime': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScheduledTaskJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaScheduledTaskJobData")
        kparams.addIntIfDefined("maxResults", self.maxResults)
        kparams.addStringIfDefined("resultsFilePath", self.resultsFilePath)
        kparams.addIntIfDefined("referenceTime", self.referenceTime)
        return kparams

    def getMaxResults(self):
        return self.maxResults

    def setMaxResults(self, newMaxResults):
        self.maxResults = newMaxResults

    def getResultsFilePath(self):
        return self.resultsFilePath

    def setResultsFilePath(self, newResultsFilePath):
        self.resultsFilePath = newResultsFilePath

    def getReferenceTime(self):
        return self.referenceTime

    def setReferenceTime(self, newReferenceTime):
        self.referenceTime = newReferenceTime


# @package Kaltura
# @subpackage Client
class KalturaScheduledTaskProfileBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            lastExecutionStartedAtGreaterThanOrEqual=NotImplemented,
            lastExecutionStartedAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var string
        self.systemNameEqual = systemNameEqual

        # @var string
        self.systemNameIn = systemNameIn

        # @var KalturaScheduledTaskProfileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.lastExecutionStartedAtGreaterThanOrEqual = lastExecutionStartedAtGreaterThanOrEqual

        # @var int
        self.lastExecutionStartedAtLessThanOrEqual = lastExecutionStartedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'systemNameEqual': getXmlNodeText, 
        'systemNameIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaScheduledTaskProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'lastExecutionStartedAtGreaterThanOrEqual': getXmlNodeInt, 
        'lastExecutionStartedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScheduledTaskProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaScheduledTaskProfileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfDefined("systemNameEqual", self.systemNameEqual)
        kparams.addStringIfDefined("systemNameIn", self.systemNameIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("lastExecutionStartedAtGreaterThanOrEqual", self.lastExecutionStartedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("lastExecutionStartedAtLessThanOrEqual", self.lastExecutionStartedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getSystemNameEqual(self):
        return self.systemNameEqual

    def setSystemNameEqual(self, newSystemNameEqual):
        self.systemNameEqual = newSystemNameEqual

    def getSystemNameIn(self):
        return self.systemNameIn

    def setSystemNameIn(self, newSystemNameIn):
        self.systemNameIn = newSystemNameIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getLastExecutionStartedAtGreaterThanOrEqual(self):
        return self.lastExecutionStartedAtGreaterThanOrEqual

    def setLastExecutionStartedAtGreaterThanOrEqual(self, newLastExecutionStartedAtGreaterThanOrEqual):
        self.lastExecutionStartedAtGreaterThanOrEqual = newLastExecutionStartedAtGreaterThanOrEqual

    def getLastExecutionStartedAtLessThanOrEqual(self):
        return self.lastExecutionStartedAtLessThanOrEqual

    def setLastExecutionStartedAtLessThanOrEqual(self, newLastExecutionStartedAtLessThanOrEqual):
        self.lastExecutionStartedAtLessThanOrEqual = newLastExecutionStartedAtLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaScheduledTaskProfileFilter(KalturaScheduledTaskProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            lastExecutionStartedAtGreaterThanOrEqual=NotImplemented,
            lastExecutionStartedAtLessThanOrEqual=NotImplemented):
        KalturaScheduledTaskProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            systemNameEqual,
            systemNameIn,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            lastExecutionStartedAtGreaterThanOrEqual,
            lastExecutionStartedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaScheduledTaskProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScheduledTaskProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaScheduledTaskProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaScheduledTaskProfileFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaScheduledTaskClientPlugin(KalturaClientPlugin):
    # KalturaScheduledTaskClientPlugin
    instance = None

    # @return KalturaScheduledTaskClientPlugin
    @staticmethod
    def get():
        if KalturaScheduledTaskClientPlugin.instance == None:
            KalturaScheduledTaskClientPlugin.instance = KalturaScheduledTaskClientPlugin()
        return KalturaScheduledTaskClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaScheduledTaskProfileStatus': KalturaScheduledTaskProfileStatus,
            'KalturaScheduledTaskProfileOrderBy': KalturaScheduledTaskProfileOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaScheduledTaskJobData': KalturaScheduledTaskJobData,
            'KalturaScheduledTaskProfileBaseFilter': KalturaScheduledTaskProfileBaseFilter,
            'KalturaScheduledTaskProfileFilter': KalturaScheduledTaskProfileFilter,
        }

    # @return string
    def getName(self):
        return 'scheduledTask'

