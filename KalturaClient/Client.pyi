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
from typing import List
from KalturaClient import KalturaConfiguration
from KalturaClient.Plugins.Core import KalturaObject
from KalturaClient.Plugins.Core import KalturaAccessControlProfileService
from KalturaClient.Plugins.Core import KalturaAccessControlService
from KalturaClient.Plugins.Core import KalturaAdminUserService
from KalturaClient.Plugins.Core import KalturaAnalyticsService
from KalturaClient.Plugins.Core import KalturaAppTokenService
from KalturaClient.Plugins.Core import KalturaBaseEntryService
from KalturaClient.Plugins.Core import KalturaBulkUploadService
from KalturaClient.Plugins.Core import KalturaCategoryEntryService
from KalturaClient.Plugins.Core import KalturaCategoryService
from KalturaClient.Plugins.Core import KalturaCategoryUserService
from KalturaClient.Plugins.Core import KalturaConversionProfileAssetParamsService
from KalturaClient.Plugins.Core import KalturaConversionProfileService
from KalturaClient.Plugins.Core import KalturaDataService
from KalturaClient.Plugins.Core import KalturaDeliveryProfileService
from KalturaClient.Plugins.Core import KalturaEmailIngestionProfileService
from KalturaClient.Plugins.Core import KalturaEntryServerNodeService
from KalturaClient.Plugins.Core import KalturaExportcsvService
from KalturaClient.Plugins.Core import KalturaFileAssetService
from KalturaClient.Plugins.Core import KalturaFlavorAssetService
from KalturaClient.Plugins.Core import KalturaFlavorParamsOutputService
from KalturaClient.Plugins.Core import KalturaFlavorParamsService
from KalturaClient.Plugins.Core import KalturaGroupUserService
from KalturaClient.Plugins.Core import KalturaLiveChannelSegmentService
from KalturaClient.Plugins.Core import KalturaLiveChannelService
from KalturaClient.Plugins.Core import KalturaLiveReportsService
from KalturaClient.Plugins.Core import KalturaLiveStatsService
from KalturaClient.Plugins.Core import KalturaLiveStreamService
from KalturaClient.Plugins.Core import KalturaMediaInfoService
from KalturaClient.Plugins.Core import KalturaMediaService
from KalturaClient.Plugins.Core import KalturaMixingService
from KalturaClient.Plugins.Core import KalturaNotificationService
from KalturaClient.Plugins.Core import KalturaPartnerService
from KalturaClient.Plugins.Core import KalturaPermissionItemService
from KalturaClient.Plugins.Core import KalturaPermissionService
from KalturaClient.Plugins.Core import KalturaPlaylistService
from KalturaClient.Plugins.Core import KalturaReportService
from KalturaClient.Plugins.Core import KalturaResponseProfileService
from KalturaClient.Plugins.Core import KalturaSchemaService
from KalturaClient.Plugins.Core import KalturaSearchService
from KalturaClient.Plugins.Core import KalturaServerNodeService
from KalturaClient.Plugins.Core import KalturaSessionService
from KalturaClient.Plugins.Core import KalturaStatsService
from KalturaClient.Plugins.Core import KalturaStorageProfileService
from KalturaClient.Plugins.Core import KalturaSyndicationFeedService
from KalturaClient.Plugins.Core import KalturaSystemService
from KalturaClient.Plugins.Core import KalturaThumbAssetService
from KalturaClient.Plugins.Core import KalturaThumbParamsOutputService
from KalturaClient.Plugins.Core import KalturaThumbParamsService
from KalturaClient.Plugins.Core import KalturaUiConfService
from KalturaClient.Plugins.Core import KalturaUploadService
from KalturaClient.Plugins.Core import KalturaUploadTokenService
from KalturaClient.Plugins.Core import KalturaUserAppRoleService
from KalturaClient.Plugins.Core import KalturaUserEntryService
from KalturaClient.Plugins.Core import KalturaUserRoleService
from KalturaClient.Plugins.Core import KalturaUserService
from KalturaClient.Plugins.Core import KalturaWidgetService
from KalturaClient.Plugins.Metadata import KalturaMetadataClientPluginServicesProxy
from KalturaClient.Plugins.Document import KalturaDocumentClientPluginServicesProxy
from KalturaClient.Plugins.AdCuePoint import KalturaAdCuePointClientPluginServicesProxy
from KalturaClient.Plugins.Annotation import KalturaAnnotationClientPluginServicesProxy
from KalturaClient.Plugins.Aspera import KalturaAsperaClientPluginServicesProxy
from KalturaClient.Plugins.AttUverseDistribution import KalturaAttUverseDistributionClientPluginServicesProxy
from KalturaClient.Plugins.Attachment import KalturaAttachmentClientPluginServicesProxy
from KalturaClient.Plugins.Audit import KalturaAuditClientPluginServicesProxy
from KalturaClient.Plugins.AvnDistribution import KalturaAvnDistributionClientPluginServicesProxy
from KalturaClient.Plugins.BulkUpload import KalturaBulkUploadClientPluginServicesProxy
from KalturaClient.Plugins.BulkUploadCsv import KalturaBulkUploadCsvClientPluginServicesProxy
from KalturaClient.Plugins.BulkUploadXml import KalturaBulkUploadXmlClientPluginServicesProxy
from KalturaClient.Plugins.Bumper import KalturaBumperClientPluginServicesProxy
from KalturaClient.Plugins.Caption import KalturaCaptionClientPluginServicesProxy
from KalturaClient.Plugins.CaptionSearch import KalturaCaptionSearchClientPluginServicesProxy
from KalturaClient.Plugins.CaptureSpace import KalturaCaptureSpaceClientPluginServicesProxy
from KalturaClient.Plugins.CodeCuePoint import KalturaCodeCuePointClientPluginServicesProxy
from KalturaClient.Plugins.ThumbCuePoint import KalturaThumbCuePointClientPluginServicesProxy
from KalturaClient.Plugins.ComcastMrssDistribution import KalturaComcastMrssDistributionClientPluginServicesProxy
from KalturaClient.Plugins.ContentDistribution import KalturaContentDistributionClientPluginServicesProxy
from KalturaClient.Plugins.CrossKalturaDistribution import KalturaCrossKalturaDistributionClientPluginServicesProxy
from KalturaClient.Plugins.CuePoint import KalturaCuePointClientPluginServicesProxy
from KalturaClient.Plugins.DailymotionDistribution import KalturaDailymotionDistributionClientPluginServicesProxy
from KalturaClient.Plugins.DoubleClickDistribution import KalturaDoubleClickDistributionClientPluginServicesProxy
from KalturaClient.Plugins.DropFolder import KalturaDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.DropFolderXmlBulkUpload import KalturaDropFolderXmlBulkUploadClientPluginServicesProxy
from KalturaClient.Plugins.EmailNotification import KalturaEmailNotificationClientPluginServicesProxy
from KalturaClient.Plugins.EventNotification import KalturaEventNotificationClientPluginServicesProxy
from KalturaClient.Plugins.FeedDropFolder import KalturaFeedDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.HttpNotification import KalturaHttpNotificationClientPluginServicesProxy
from KalturaClient.Plugins.BooleanNotification import KalturaBooleanNotificationClientPluginServicesProxy
from KalturaClient.Plugins.PushNotification import KalturaPushNotificationClientPluginServicesProxy
from KalturaClient.Plugins.FileSync import KalturaFileSyncClientPluginServicesProxy
from KalturaClient.Plugins.FreewheelDistribution import KalturaFreewheelDistributionClientPluginServicesProxy
from KalturaClient.Plugins.FreewheelGenericDistribution import KalturaFreewheelGenericDistributionClientPluginServicesProxy
from KalturaClient.Plugins.FtpDistribution import KalturaFtpDistributionClientPluginServicesProxy
from KalturaClient.Plugins.HuluDistribution import KalturaHuluDistributionClientPluginServicesProxy
from KalturaClient.Plugins.IdeticDistribution import KalturaIdeticDistributionClientPluginServicesProxy
from KalturaClient.Plugins.KalturaSharepointExtension import KalturaKalturaSharepointExtensionClientPluginServicesProxy
from KalturaClient.Plugins.Like import KalturaLikeClientPluginServicesProxy
from KalturaClient.Plugins.MetroPcsDistribution import KalturaMetroPcsDistributionClientPluginServicesProxy
from KalturaClient.Plugins.MsnDistribution import KalturaMsnDistributionClientPluginServicesProxy
from KalturaClient.Plugins.MultiCenters import KalturaMultiCentersClientPluginServicesProxy
from KalturaClient.Plugins.NdnDistribution import KalturaNdnDistributionClientPluginServicesProxy
from KalturaClient.Plugins.PodcastDistribution import KalturaPodcastDistributionClientPluginServicesProxy
from KalturaClient.Plugins.QuickPlayDistribution import KalturaQuickPlayDistributionClientPluginServicesProxy
from KalturaClient.Plugins.ShortLink import KalturaShortLinkClientPluginServicesProxy
from KalturaClient.Plugins.SynacorHboDistribution import KalturaSynacorHboDistributionClientPluginServicesProxy
from KalturaClient.Plugins.TvComDistribution import KalturaTvComDistributionClientPluginServicesProxy
from KalturaClient.Plugins.TagSearch import KalturaTagSearchClientPluginServicesProxy
from KalturaClient.Plugins.TimeWarnerDistribution import KalturaTimeWarnerDistributionClientPluginServicesProxy
from KalturaClient.Plugins.UverseClickToOrderDistribution import KalturaUverseClickToOrderDistributionClientPluginServicesProxy
from KalturaClient.Plugins.UverseDistribution import KalturaUverseDistributionClientPluginServicesProxy
from KalturaClient.Plugins.VarConsole import KalturaVarConsoleClientPluginServicesProxy
from KalturaClient.Plugins.VerizonVcastDistribution import KalturaVerizonVcastDistributionClientPluginServicesProxy
from KalturaClient.Plugins.VirusScan import KalturaVirusScanClientPluginServicesProxy
from KalturaClient.Plugins.YahooDistribution import KalturaYahooDistributionClientPluginServicesProxy
from KalturaClient.Plugins.YouTubeDistribution import KalturaYouTubeDistributionClientPluginServicesProxy
from KalturaClient.Plugins.YoutubeApiDistribution import KalturaYoutubeApiDistributionClientPluginServicesProxy
from KalturaClient.Plugins.CortexApiDistribution import KalturaCortexApiDistributionClientPluginServicesProxy
from KalturaClient.Plugins.AbcScreenersWatermarkAccessControl import KalturaAbcScreenersWatermarkAccessControlClientPluginServicesProxy
from KalturaClient.Plugins.ExternalMedia import KalturaExternalMediaClientPluginServicesProxy
from KalturaClient.Plugins.Drm import KalturaDrmClientPluginServicesProxy
from KalturaClient.Plugins.Fairplay import KalturaFairplayClientPluginServicesProxy
from KalturaClient.Plugins.Widevine import KalturaWidevineClientPluginServicesProxy
from KalturaClient.Plugins.WebexDropFolder import KalturaWebexDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.Kontiki import KalturaKontikiClientPluginServicesProxy
from KalturaClient.Plugins.Velocix import KalturaVelocixClientPluginServicesProxy
from KalturaClient.Plugins.Wowza import KalturaWowzaClientPluginServicesProxy
from KalturaClient.Plugins.LiveCluster import KalturaLiveClusterClientPluginServicesProxy
from KalturaClient.Plugins.ScheduledTask import KalturaScheduledTaskClientPluginServicesProxy
from KalturaClient.Plugins.ScheduledTaskEventNotification import KalturaScheduledTaskEventNotificationClientPluginServicesProxy
from KalturaClient.Plugins.ScheduledTaskMetadata import KalturaScheduledTaskMetadataClientPluginServicesProxy
from KalturaClient.Plugins.ScheduledTaskContentDistribution import KalturaScheduledTaskContentDistributionClientPluginServicesProxy
from KalturaClient.Plugins.BulkUploadFilter import KalturaBulkUploadFilterClientPluginServicesProxy
from KalturaClient.Plugins.PlayReady import KalturaPlayReadyClientPluginServicesProxy
from KalturaClient.Plugins.TvinciDistribution import KalturaTvinciDistributionClientPluginServicesProxy
from KalturaClient.Plugins.UnicornDistribution import KalturaUnicornDistributionClientPluginServicesProxy
from KalturaClient.Plugins.EventCuePoint import KalturaEventCuePointClientPluginServicesProxy
from KalturaClient.Plugins.Integration import KalturaIntegrationClientPluginServicesProxy
from KalturaClient.Plugins.ExampleIntegration import KalturaExampleIntegrationClientPluginServicesProxy
from KalturaClient.Plugins.BpmEventNotificationIntegration import KalturaBpmEventNotificationIntegrationClientPluginServicesProxy
from KalturaClient.Plugins.BusinessProcessNotification import KalturaBusinessProcessNotificationClientPluginServicesProxy
from KalturaClient.Plugins.ActivitiBusinessProcessNotification import KalturaActivitiBusinessProcessNotificationClientPluginServicesProxy
from KalturaClient.Plugins.Quiz import KalturaQuizClientPluginServicesProxy
from KalturaClient.Plugins.Transcript import KalturaTranscriptClientPluginServicesProxy
from KalturaClient.Plugins.DexterIntegration import KalturaDexterIntegrationClientPluginServicesProxy
from KalturaClient.Plugins.Voicebase import KalturaVoicebaseClientPluginServicesProxy
from KalturaClient.Plugins.Cielo24 import KalturaCielo24ClientPluginServicesProxy
from KalturaClient.Plugins.FacebookDistribution import KalturaFacebookDistributionClientPluginServicesProxy
from KalturaClient.Plugins.Schedule import KalturaScheduleClientPluginServicesProxy
from KalturaClient.Plugins.ScheduleBulkUpload import KalturaScheduleBulkUploadClientPluginServicesProxy
from KalturaClient.Plugins.ScheduleDropFolder import KalturaScheduleDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.PushToNewsDistribution import KalturaPushToNewsDistributionClientPluginServicesProxy
from KalturaClient.Plugins.ViewHistory import KalturaViewHistoryClientPluginServicesProxy
from KalturaClient.Plugins.WatchLater import KalturaWatchLaterClientPluginServicesProxy
from KalturaClient.Plugins.EntryPermissionLevel import KalturaEntryPermissionLevelClientPluginServicesProxy
from KalturaClient.Plugins.Registration import KalturaRegistrationClientPluginServicesProxy
from KalturaClient.Plugins.Poll import KalturaPollClientPluginServicesProxy
from KalturaClient.Plugins.ElasticSearch import KalturaElasticSearchClientPluginServicesProxy
from KalturaClient.Plugins.Beacon import KalturaBeaconClientPluginServicesProxy
from KalturaClient.Plugins.TrRdsSyncDropFolder import KalturaTrRdsSyncDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.Reach import KalturaReachClientPluginServicesProxy
from KalturaClient.Plugins.Conference import KalturaConferenceClientPluginServicesProxy
from KalturaClient.Plugins.SearchHistory import KalturaSearchHistoryClientPluginServicesProxy
from KalturaClient.Plugins.Vendor import KalturaVendorClientPluginServicesProxy
from KalturaClient.Plugins.Group import KalturaGroupClientPluginServicesProxy
from KalturaClient.Plugins.Sip import KalturaSipClientPluginServicesProxy
from KalturaClient.Plugins.Thumbnail import KalturaThumbnailClientPluginServicesProxy
from KalturaClient.Plugins.Sso import KalturaSsoClientPluginServicesProxy
from KalturaClient.Plugins.ApFeedDropFolder import KalturaApFeedDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.Rating import KalturaRatingClientPluginServicesProxy
from KalturaClient.Plugins.ConfMaps import KalturaConfMapsClientPluginServicesProxy
from KalturaClient.Plugins.SystemPartner import KalturaSystemPartnerClientPluginServicesProxy
from KalturaClient.Plugins.Interactivity import KalturaInteractivityClientPluginServicesProxy
from KalturaClient.Plugins.S3DropFolder import KalturaS3DropFolderClientPluginServicesProxy
from KalturaClient.Plugins.ZoomDropFolder import KalturaZoomDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.MicrosoftTeamsDropFolder import KalturaMicrosoftTeamsDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.VirtualEvent import KalturaVirtualEventClientPluginServicesProxy
from KalturaClient.Plugins.Game import KalturaGameClientPluginServicesProxy
from KalturaClient.Plugins.KafkaNotification import KalturaKafkaNotificationClientPluginServicesProxy
from KalturaClient.Plugins.WebexAPIDropFolder import KalturaWebexAPIDropFolderClientPluginServicesProxy
from KalturaClient.Plugins.Room import KalturaRoomClientPluginServicesProxy
from KalturaClient.Plugins.SessionCuePoint import KalturaSessionCuePointClientPluginServicesProxy
from KalturaClient.Plugins.Rsvp import KalturaRsvpClientPluginServicesProxy

class MultiRequestSubResult(object):
    def __init__(self, value): ...
    def __getattr__(self, name) -> MultiRequestSubResult: ...
    def __getitem__(self, key) -> MultiRequestSubResult: ...

class KalturaClient:
    def __init__(self, config: KalturaConfiguration, remove_data_content: bool = False): ...
    def getKs(self) -> str: ...
    def setKs(self, ks: str): ...
    def getLanguage(self) -> str: ...
    def setLanguage(self, language: str): ...
    def getPartnerId(self) -> int: ...
    def setPartnerId(self, partner_id: int): ...
    def getClientTag(self) -> str: ...
    def setClientTag(self, client_tag: str): ...
    def getApiVersion(self) -> str: ...
    def setApiVersion(self, api_version: str): ...
    def getConfig(self) -> KalturaConfiguration: ...
    def setConfig(self, config: KalturaConfiguration): ...
    def startMultiRequest(self): ...
    def doMultiRequest(self) -> List[KalturaObject]: ...

    accessControlProfile: KalturaAccessControlProfileService
    accessControl: KalturaAccessControlService
    adminUser: KalturaAdminUserService
    analytics: KalturaAnalyticsService
    appToken: KalturaAppTokenService
    baseEntry: KalturaBaseEntryService
    bulkUpload: KalturaBulkUploadService
    categoryEntry: KalturaCategoryEntryService
    category: KalturaCategoryService
    categoryUser: KalturaCategoryUserService
    conversionProfileAssetParams: KalturaConversionProfileAssetParamsService
    conversionProfile: KalturaConversionProfileService
    data: KalturaDataService
    deliveryProfile: KalturaDeliveryProfileService
    EmailIngestionProfile: KalturaEmailIngestionProfileService
    entryServerNode: KalturaEntryServerNodeService
    exportcsv: KalturaExportcsvService
    fileAsset: KalturaFileAssetService
    flavorAsset: KalturaFlavorAssetService
    flavorParamsOutput: KalturaFlavorParamsOutputService
    flavorParams: KalturaFlavorParamsService
    groupUser: KalturaGroupUserService
    liveChannelSegment: KalturaLiveChannelSegmentService
    liveChannel: KalturaLiveChannelService
    liveReports: KalturaLiveReportsService
    liveStats: KalturaLiveStatsService
    liveStream: KalturaLiveStreamService
    mediaInfo: KalturaMediaInfoService
    media: KalturaMediaService
    mixing: KalturaMixingService
    notification: KalturaNotificationService
    partner: KalturaPartnerService
    permissionItem: KalturaPermissionItemService
    permission: KalturaPermissionService
    playlist: KalturaPlaylistService
    report: KalturaReportService
    responseProfile: KalturaResponseProfileService
    schema: KalturaSchemaService
    search: KalturaSearchService
    serverNode: KalturaServerNodeService
    session: KalturaSessionService
    stats: KalturaStatsService
    storageProfile: KalturaStorageProfileService
    syndicationFeed: KalturaSyndicationFeedService
    system: KalturaSystemService
    thumbAsset: KalturaThumbAssetService
    thumbParamsOutput: KalturaThumbParamsOutputService
    thumbParams: KalturaThumbParamsService
    uiConf: KalturaUiConfService
    upload: KalturaUploadService
    uploadToken: KalturaUploadTokenService
    userAppRole: KalturaUserAppRoleService
    userEntry: KalturaUserEntryService
    userRole: KalturaUserRoleService
    user: KalturaUserService
    widget: KalturaWidgetService
    metadata: KalturaMetadataClientPluginServicesProxy
    document: KalturaDocumentClientPluginServicesProxy
    adCuePoint: KalturaAdCuePointClientPluginServicesProxy
    annotation: KalturaAnnotationClientPluginServicesProxy
    aspera: KalturaAsperaClientPluginServicesProxy
    attUverseDistribution: KalturaAttUverseDistributionClientPluginServicesProxy
    attachment: KalturaAttachmentClientPluginServicesProxy
    audit: KalturaAuditClientPluginServicesProxy
    avnDistribution: KalturaAvnDistributionClientPluginServicesProxy
    bulkUpload: KalturaBulkUploadClientPluginServicesProxy
    bulkUploadCsv: KalturaBulkUploadCsvClientPluginServicesProxy
    bulkUploadXml: KalturaBulkUploadXmlClientPluginServicesProxy
    bumper: KalturaBumperClientPluginServicesProxy
    caption: KalturaCaptionClientPluginServicesProxy
    captionSearch: KalturaCaptionSearchClientPluginServicesProxy
    captureSpace: KalturaCaptureSpaceClientPluginServicesProxy
    codeCuePoint: KalturaCodeCuePointClientPluginServicesProxy
    thumbCuePoint: KalturaThumbCuePointClientPluginServicesProxy
    comcastMrssDistribution: KalturaComcastMrssDistributionClientPluginServicesProxy
    contentDistribution: KalturaContentDistributionClientPluginServicesProxy
    crossKalturaDistribution: KalturaCrossKalturaDistributionClientPluginServicesProxy
    cuePoint: KalturaCuePointClientPluginServicesProxy
    dailymotionDistribution: KalturaDailymotionDistributionClientPluginServicesProxy
    doubleClickDistribution: KalturaDoubleClickDistributionClientPluginServicesProxy
    dropFolder: KalturaDropFolderClientPluginServicesProxy
    dropFolderXmlBulkUpload: KalturaDropFolderXmlBulkUploadClientPluginServicesProxy
    emailNotification: KalturaEmailNotificationClientPluginServicesProxy
    eventNotification: KalturaEventNotificationClientPluginServicesProxy
    FeedDropFolder: KalturaFeedDropFolderClientPluginServicesProxy
    httpNotification: KalturaHttpNotificationClientPluginServicesProxy
    booleanNotification: KalturaBooleanNotificationClientPluginServicesProxy
    pushNotification: KalturaPushNotificationClientPluginServicesProxy
    fileSync: KalturaFileSyncClientPluginServicesProxy
    freewheelDistribution: KalturaFreewheelDistributionClientPluginServicesProxy
    freewheelGenericDistribution: KalturaFreewheelGenericDistributionClientPluginServicesProxy
    ftpDistribution: KalturaFtpDistributionClientPluginServicesProxy
    huluDistribution: KalturaHuluDistributionClientPluginServicesProxy
    ideticDistribution: KalturaIdeticDistributionClientPluginServicesProxy
    KalturaSharepointExtension: KalturaKalturaSharepointExtensionClientPluginServicesProxy
    like: KalturaLikeClientPluginServicesProxy
    metroPcsDistribution: KalturaMetroPcsDistributionClientPluginServicesProxy
    msnDistribution: KalturaMsnDistributionClientPluginServicesProxy
    multiCenters: KalturaMultiCentersClientPluginServicesProxy
    ndnDistribution: KalturaNdnDistributionClientPluginServicesProxy
    podcastDistribution: KalturaPodcastDistributionClientPluginServicesProxy
    quickPlayDistribution: KalturaQuickPlayDistributionClientPluginServicesProxy
    shortLink: KalturaShortLinkClientPluginServicesProxy
    synacorHboDistribution: KalturaSynacorHboDistributionClientPluginServicesProxy
    tvComDistribution: KalturaTvComDistributionClientPluginServicesProxy
    tagSearch: KalturaTagSearchClientPluginServicesProxy
    timeWarnerDistribution: KalturaTimeWarnerDistributionClientPluginServicesProxy
    uverseClickToOrderDistribution: KalturaUverseClickToOrderDistributionClientPluginServicesProxy
    uverseDistribution: KalturaUverseDistributionClientPluginServicesProxy
    varConsole: KalturaVarConsoleClientPluginServicesProxy
    verizonVcastDistribution: KalturaVerizonVcastDistributionClientPluginServicesProxy
    virusScan: KalturaVirusScanClientPluginServicesProxy
    yahooDistribution: KalturaYahooDistributionClientPluginServicesProxy
    youTubeDistribution: KalturaYouTubeDistributionClientPluginServicesProxy
    youtubeApiDistribution: KalturaYoutubeApiDistributionClientPluginServicesProxy
    cortexApiDistribution: KalturaCortexApiDistributionClientPluginServicesProxy
    abcScreenersWatermarkAccessControl: KalturaAbcScreenersWatermarkAccessControlClientPluginServicesProxy
    externalMedia: KalturaExternalMediaClientPluginServicesProxy
    drm: KalturaDrmClientPluginServicesProxy
    fairplay: KalturaFairplayClientPluginServicesProxy
    widevine: KalturaWidevineClientPluginServicesProxy
    WebexDropFolder: KalturaWebexDropFolderClientPluginServicesProxy
    kontiki: KalturaKontikiClientPluginServicesProxy
    velocix: KalturaVelocixClientPluginServicesProxy
    wowza: KalturaWowzaClientPluginServicesProxy
    liveCluster: KalturaLiveClusterClientPluginServicesProxy
    scheduledTask: KalturaScheduledTaskClientPluginServicesProxy
    scheduledTaskEventNotification: KalturaScheduledTaskEventNotificationClientPluginServicesProxy
    scheduledTaskMetadata: KalturaScheduledTaskMetadataClientPluginServicesProxy
    scheduledTaskContentDistribution: KalturaScheduledTaskContentDistributionClientPluginServicesProxy
    bulkUploadFilter: KalturaBulkUploadFilterClientPluginServicesProxy
    playReady: KalturaPlayReadyClientPluginServicesProxy
    tvinciDistribution: KalturaTvinciDistributionClientPluginServicesProxy
    unicornDistribution: KalturaUnicornDistributionClientPluginServicesProxy
    eventCuePoint: KalturaEventCuePointClientPluginServicesProxy
    integration: KalturaIntegrationClientPluginServicesProxy
    exampleIntegration: KalturaExampleIntegrationClientPluginServicesProxy
    bpmEventNotificationIntegration: KalturaBpmEventNotificationIntegrationClientPluginServicesProxy
    businessProcessNotification: KalturaBusinessProcessNotificationClientPluginServicesProxy
    activitiBusinessProcessNotification: KalturaActivitiBusinessProcessNotificationClientPluginServicesProxy
    quiz: KalturaQuizClientPluginServicesProxy
    transcript: KalturaTranscriptClientPluginServicesProxy
    dexterIntegration: KalturaDexterIntegrationClientPluginServicesProxy
    voicebase: KalturaVoicebaseClientPluginServicesProxy
    cielo24: KalturaCielo24ClientPluginServicesProxy
    facebookDistribution: KalturaFacebookDistributionClientPluginServicesProxy
    schedule: KalturaScheduleClientPluginServicesProxy
    scheduleBulkUpload: KalturaScheduleBulkUploadClientPluginServicesProxy
    scheduleDropFolder: KalturaScheduleDropFolderClientPluginServicesProxy
    pushToNewsDistribution: KalturaPushToNewsDistributionClientPluginServicesProxy
    viewHistory: KalturaViewHistoryClientPluginServicesProxy
    watchLater: KalturaWatchLaterClientPluginServicesProxy
    entryPermissionLevel: KalturaEntryPermissionLevelClientPluginServicesProxy
    registration: KalturaRegistrationClientPluginServicesProxy
    poll: KalturaPollClientPluginServicesProxy
    elasticSearch: KalturaElasticSearchClientPluginServicesProxy
    beacon: KalturaBeaconClientPluginServicesProxy
    TrRdsSyncDropFolder: KalturaTrRdsSyncDropFolderClientPluginServicesProxy
    reach: KalturaReachClientPluginServicesProxy
    conference: KalturaConferenceClientPluginServicesProxy
    searchHistory: KalturaSearchHistoryClientPluginServicesProxy
    vendor: KalturaVendorClientPluginServicesProxy
    group: KalturaGroupClientPluginServicesProxy
    sip: KalturaSipClientPluginServicesProxy
    thumbnail: KalturaThumbnailClientPluginServicesProxy
    sso: KalturaSsoClientPluginServicesProxy
    ApFeedDropFolder: KalturaApFeedDropFolderClientPluginServicesProxy
    rating: KalturaRatingClientPluginServicesProxy
    confMaps: KalturaConfMapsClientPluginServicesProxy
    systemPartner: KalturaSystemPartnerClientPluginServicesProxy
    interactivity: KalturaInteractivityClientPluginServicesProxy
    S3DropFolder: KalturaS3DropFolderClientPluginServicesProxy
    ZoomDropFolder: KalturaZoomDropFolderClientPluginServicesProxy
    MicrosoftTeamsDropFolder: KalturaMicrosoftTeamsDropFolderClientPluginServicesProxy
    virtualEvent: KalturaVirtualEventClientPluginServicesProxy
    game: KalturaGameClientPluginServicesProxy
    kafkaNotification: KalturaKafkaNotificationClientPluginServicesProxy
    WebexAPIDropFolder: KalturaWebexAPIDropFolderClientPluginServicesProxy
    room: KalturaRoomClientPluginServicesProxy
    sessionCuePoint: KalturaSessionCuePointClientPluginServicesProxy
    rsvp: KalturaRsvpClientPluginServicesProxy