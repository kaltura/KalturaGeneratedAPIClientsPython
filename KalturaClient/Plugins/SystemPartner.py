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
# Copyright (C) 2006-2019  Kaltura Inc.
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
from __future__ import absolute_import

from .Core import *
from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

########## enums ##########
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerUsageItem(KalturaObjectBase):
    def __init__(self,
            partnerId=NotImplemented,
            partnerName=NotImplemented,
            partnerStatus=NotImplemented,
            partnerPackage=NotImplemented,
            partnerCreatedAt=NotImplemented,
            views=NotImplemented,
            plays=NotImplemented,
            entriesCount=NotImplemented,
            totalEntriesCount=NotImplemented,
            videoEntriesCount=NotImplemented,
            imageEntriesCount=NotImplemented,
            audioEntriesCount=NotImplemented,
            mixEntriesCount=NotImplemented,
            bandwidth=NotImplemented,
            totalStorage=NotImplemented,
            storage=NotImplemented,
            peakStorage=NotImplemented,
            avgStorage=NotImplemented,
            combinedBandwidthStorage=NotImplemented,
            deletedStorage=NotImplemented,
            transcodingUsage=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Partner ID
        # @var int
        self.partnerId = partnerId

        # Partner name
        # @var string
        self.partnerName = partnerName

        # Partner status
        # @var KalturaPartnerStatus
        self.partnerStatus = partnerStatus

        # Partner package
        # @var int
        self.partnerPackage = partnerPackage

        # Partner creation date (Unix timestamp)
        # @var int
        self.partnerCreatedAt = partnerCreatedAt

        # Number of player loads in the specific date range
        # @var int
        self.views = views

        # Number of plays in the specific date range
        # @var int
        self.plays = plays

        # Number of new entries created during specific date range
        # @var int
        self.entriesCount = entriesCount

        # Total number of entries
        # @var int
        self.totalEntriesCount = totalEntriesCount

        # Number of new video entries created during specific date range
        # @var int
        self.videoEntriesCount = videoEntriesCount

        # Number of new image entries created during specific date range
        # @var int
        self.imageEntriesCount = imageEntriesCount

        # Number of new audio entries created during specific date range
        # @var int
        self.audioEntriesCount = audioEntriesCount

        # Number of new mix entries created during specific date range
        # @var int
        self.mixEntriesCount = mixEntriesCount

        # The total bandwidth usage during the given date range (in MB)
        # @var float
        self.bandwidth = bandwidth

        # The total storage consumption (in MB)
        # @var float
        self.totalStorage = totalStorage

        # The change in storage consumption (new uploads) during the given date range (in MB)
        # @var float
        self.storage = storage

        # The peak amount of storage consumption during the given date range for the specific publisher
        # @var float
        self.peakStorage = peakStorage

        # The average amount of storage consumption during the given date range for the specific publisher
        # @var float
        self.avgStorage = avgStorage

        # The combined amount of bandwidth and storage consumed during the given date range for the specific publisher
        # @var float
        self.combinedBandwidthStorage = combinedBandwidthStorage

        # Amount of deleted storage in MB
        # @var float
        self.deletedStorage = deletedStorage

        # Amount of transcoding usage in MB
        # @var float
        self.transcodingUsage = transcodingUsage


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'partnerName': getXmlNodeText, 
        'partnerStatus': (KalturaEnumsFactory.createInt, "KalturaPartnerStatus"), 
        'partnerPackage': getXmlNodeInt, 
        'partnerCreatedAt': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'plays': getXmlNodeInt, 
        'entriesCount': getXmlNodeInt, 
        'totalEntriesCount': getXmlNodeInt, 
        'videoEntriesCount': getXmlNodeInt, 
        'imageEntriesCount': getXmlNodeInt, 
        'audioEntriesCount': getXmlNodeInt, 
        'mixEntriesCount': getXmlNodeInt, 
        'bandwidth': getXmlNodeFloat, 
        'totalStorage': getXmlNodeFloat, 
        'storage': getXmlNodeFloat, 
        'peakStorage': getXmlNodeFloat, 
        'avgStorage': getXmlNodeFloat, 
        'combinedBandwidthStorage': getXmlNodeFloat, 
        'deletedStorage': getXmlNodeFloat, 
        'transcodingUsage': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageItem")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("partnerName", self.partnerName)
        kparams.addIntEnumIfDefined("partnerStatus", self.partnerStatus)
        kparams.addIntIfDefined("partnerPackage", self.partnerPackage)
        kparams.addIntIfDefined("partnerCreatedAt", self.partnerCreatedAt)
        kparams.addIntIfDefined("views", self.views)
        kparams.addIntIfDefined("plays", self.plays)
        kparams.addIntIfDefined("entriesCount", self.entriesCount)
        kparams.addIntIfDefined("totalEntriesCount", self.totalEntriesCount)
        kparams.addIntIfDefined("videoEntriesCount", self.videoEntriesCount)
        kparams.addIntIfDefined("imageEntriesCount", self.imageEntriesCount)
        kparams.addIntIfDefined("audioEntriesCount", self.audioEntriesCount)
        kparams.addIntIfDefined("mixEntriesCount", self.mixEntriesCount)
        kparams.addFloatIfDefined("bandwidth", self.bandwidth)
        kparams.addFloatIfDefined("totalStorage", self.totalStorage)
        kparams.addFloatIfDefined("storage", self.storage)
        kparams.addFloatIfDefined("peakStorage", self.peakStorage)
        kparams.addFloatIfDefined("avgStorage", self.avgStorage)
        kparams.addFloatIfDefined("combinedBandwidthStorage", self.combinedBandwidthStorage)
        kparams.addFloatIfDefined("deletedStorage", self.deletedStorage)
        kparams.addFloatIfDefined("transcodingUsage", self.transcodingUsage)
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getPartnerStatus(self):
        return self.partnerStatus

    def setPartnerStatus(self, newPartnerStatus):
        self.partnerStatus = newPartnerStatus

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getPartnerCreatedAt(self):
        return self.partnerCreatedAt

    def setPartnerCreatedAt(self, newPartnerCreatedAt):
        self.partnerCreatedAt = newPartnerCreatedAt

    def getViews(self):
        return self.views

    def setViews(self, newViews):
        self.views = newViews

    def getPlays(self):
        return self.plays

    def setPlays(self, newPlays):
        self.plays = newPlays

    def getEntriesCount(self):
        return self.entriesCount

    def setEntriesCount(self, newEntriesCount):
        self.entriesCount = newEntriesCount

    def getTotalEntriesCount(self):
        return self.totalEntriesCount

    def setTotalEntriesCount(self, newTotalEntriesCount):
        self.totalEntriesCount = newTotalEntriesCount

    def getVideoEntriesCount(self):
        return self.videoEntriesCount

    def setVideoEntriesCount(self, newVideoEntriesCount):
        self.videoEntriesCount = newVideoEntriesCount

    def getImageEntriesCount(self):
        return self.imageEntriesCount

    def setImageEntriesCount(self, newImageEntriesCount):
        self.imageEntriesCount = newImageEntriesCount

    def getAudioEntriesCount(self):
        return self.audioEntriesCount

    def setAudioEntriesCount(self, newAudioEntriesCount):
        self.audioEntriesCount = newAudioEntriesCount

    def getMixEntriesCount(self):
        return self.mixEntriesCount

    def setMixEntriesCount(self, newMixEntriesCount):
        self.mixEntriesCount = newMixEntriesCount

    def getBandwidth(self):
        return self.bandwidth

    def setBandwidth(self, newBandwidth):
        self.bandwidth = newBandwidth

    def getTotalStorage(self):
        return self.totalStorage

    def setTotalStorage(self, newTotalStorage):
        self.totalStorage = newTotalStorage

    def getStorage(self):
        return self.storage

    def setStorage(self, newStorage):
        self.storage = newStorage

    def getPeakStorage(self):
        return self.peakStorage

    def setPeakStorage(self, newPeakStorage):
        self.peakStorage = newPeakStorage

    def getAvgStorage(self):
        return self.avgStorage

    def setAvgStorage(self, newAvgStorage):
        self.avgStorage = newAvgStorage

    def getCombinedBandwidthStorage(self):
        return self.combinedBandwidthStorage

    def setCombinedBandwidthStorage(self, newCombinedBandwidthStorage):
        self.combinedBandwidthStorage = newCombinedBandwidthStorage

    def getDeletedStorage(self):
        return self.deletedStorage

    def setDeletedStorage(self, newDeletedStorage):
        self.deletedStorage = newDeletedStorage

    def getTranscodingUsage(self):
        return self.transcodingUsage

    def setTranscodingUsage(self, newTranscodingUsage):
        self.transcodingUsage = newTranscodingUsage


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerUsageFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            fromDate=NotImplemented,
            toDate=NotImplemented,
            timezoneOffset=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # Date range from
        # @var int
        self.fromDate = fromDate

        # Date range to
        # @var int
        self.toDate = toDate

        # Time zone offset
        # @var int
        self.timezoneOffset = timezoneOffset


    PROPERTY_LOADERS = {
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
        'timezoneOffset': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageFilter")
        kparams.addIntIfDefined("fromDate", self.fromDate)
        kparams.addIntIfDefined("toDate", self.toDate)
        kparams.addIntIfDefined("timezoneOffset", self.timezoneOffset)
        return kparams

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate

    def getTimezoneOffset(self):
        return self.timezoneOffset

    def setTimezoneOffset(self, newTimezoneOffset):
        self.timezoneOffset = newTimezoneOffset


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerUsageListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaSystemPartnerUsageItem
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSystemPartnerUsageItem'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerFilter(KalturaPartnerFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerPackageEqual=NotImplemented,
            partnerPackageGreaterThanOrEqual=NotImplemented,
            partnerPackageLessThanOrEqual=NotImplemented,
            partnerPackageIn=NotImplemented,
            partnerGroupTypeEqual=NotImplemented,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            idGreaterThan=NotImplemented,
            partnerParentIdEqual=NotImplemented,
            partnerParentIdIn=NotImplemented):
        KalturaPartnerFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            statusEqual,
            statusIn,
            partnerPackageEqual,
            partnerPackageGreaterThanOrEqual,
            partnerPackageLessThanOrEqual,
            partnerPackageIn,
            partnerGroupTypeEqual,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike,
            createdAtGreaterThanOrEqual,
            idGreaterThan)

        # @var int
        self.partnerParentIdEqual = partnerParentIdEqual

        # @var string
        self.partnerParentIdIn = partnerParentIdIn


    PROPERTY_LOADERS = {
        'partnerParentIdEqual': getXmlNodeInt, 
        'partnerParentIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPartnerFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerFilter.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerFilter")
        kparams.addIntIfDefined("partnerParentIdEqual", self.partnerParentIdEqual)
        kparams.addStringIfDefined("partnerParentIdIn", self.partnerParentIdIn)
        return kparams

    def getPartnerParentIdEqual(self):
        return self.partnerParentIdEqual

    def setPartnerParentIdEqual(self, newPartnerParentIdEqual):
        self.partnerParentIdEqual = newPartnerParentIdEqual

    def getPartnerParentIdIn(self):
        return self.partnerParentIdIn

    def setPartnerParentIdIn(self, newPartnerParentIdIn):
        self.partnerParentIdIn = newPartnerParentIdIn


########## services ##########
########## main ##########
class KalturaSystemPartnerClientPlugin(KalturaClientPlugin):
    # KalturaSystemPartnerClientPlugin
    instance = None

    # @return KalturaSystemPartnerClientPlugin
    @staticmethod
    def get():
        if KalturaSystemPartnerClientPlugin.instance == None:
            KalturaSystemPartnerClientPlugin.instance = KalturaSystemPartnerClientPlugin()
        return KalturaSystemPartnerClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaSystemPartnerUsageItem': KalturaSystemPartnerUsageItem,
            'KalturaSystemPartnerUsageFilter': KalturaSystemPartnerUsageFilter,
            'KalturaSystemPartnerUsageListResponse': KalturaSystemPartnerUsageListResponse,
            'KalturaSystemPartnerFilter': KalturaSystemPartnerFilter,
        }

    # @return string
    def getName(self):
        return 'systemPartner'

