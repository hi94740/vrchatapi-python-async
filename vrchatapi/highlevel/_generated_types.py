"""Generated raw-response types; do not edit manually."""

from __future__ import annotations

from typing import Any, TypedDict


class AccountDeletionLog(TypedDict, total=False):
    dateTime: str
    deletionScheduled: str | None
    message: str


class Badge(TypedDict, total=False):
    assignedAt: str | None
    badgeDescription: str
    badgeId: str
    badgeImageUrl: str
    badgeName: str
    hidden: bool | None
    isQuantifiable: bool
    showcased: bool
    updatedAt: str | None


class CurrentUser(TypedDict, total=False):
    acceptedPrivacyVersion: int
    acceptedTOSVersion: int
    accountDeletionDate: str | None
    accountDeletionLog: list[AccountDeletionLog] | None
    activeFriends: list[str]
    ageVerificationStatus: str
    ageVerified: bool
    allowAvatarCopying: bool
    appleDetails: dict[str, Any]
    appleId: str
    authToken: str
    bannerColor: str
    bannerType: str
    bannerUrl: str
    completedTutorials: list[str]
    contentFilters: list[str]
    currentAvatar: str
    currentAvatarImageUrl: str
    currentAvatarTags: list[str]
    currentAvatarThumbnailImageUrl: str
    date_joined: str
    developerType: str
    discordDetails: DiscordDetails
    discordId: str
    displayName: str
    emailVerified: bool
    fallbackAvatar: str
    friendGroupNames: list[str]
    friendKey: str
    friendRequestStatus: str
    friends: list[str]
    googleDetails: dict[str, Any]
    googleId: str
    hasBirthday: bool
    hasDiscordFriendsOptOut: bool
    hasEmail: bool
    hasLoggedInFromClient: bool
    hasPendingEmail: bool
    hasSharedConnectionsOptOut: bool
    hideContentFilterSettings: bool
    homeLocation: str
    iconFrame: str
    iconUrl: str
    id: str
    instanceId: str
    isAdult: bool
    isBoopingEnabled: bool
    isEconomyCreator: bool
    isFriend: bool
    isTemporary: bool
    last_activity: str
    last_login: str
    last_mobile: str | None
    last_platform: str
    location: str
    nameplateEffect: str
    note: str
    obfuscatedEmail: str
    obfuscatedPendingEmail: str
    oculusId: str
    offlineFriends: list[str]
    onlineFriends: list[str]
    pastDisplayNames: list[PastDisplayName]
    personalizationOptOut: bool
    picoId: str
    platform: str
    platform_history: list[CurrentUserPlatformHistoryInner]
    presence: CurrentUserPresence
    profileEffect: str
    pronouns: str
    pronounsHistory: list[str]
    queuedInstance: str | None
    receiveMobileInvitations: bool
    state: str
    status: str
    statusDescription: str
    statusFirstTime: bool
    statusHistory: list[str]
    steamDetails: dict[str, Any]
    steamId: str
    tags: list[str]
    temporaryExpiryDate: Any
    travelingToInstance: str
    travelingToLocation: str
    travelingToWorld: str
    twitchDetails: dict[str, Any]
    twitchId: str
    twoFactorAuthEnabled: bool
    twoFactorAuthEnabledDate: str | None
    unsubscribe: bool
    updated_at: str
    userLanguage: str | None
    userLanguageCode: str | None
    username: str
    usesGeneratedPassword: bool
    viveId: str
    worldId: str


class DiscordDetails(TypedDict, total=False):
    global_name: str
    id: str


class PastDisplayName(TypedDict, total=False):
    displayName: str
    reverted: bool
    updated_at: str


class CurrentUserPlatformHistoryInner(TypedDict, total=False):
    isMobile: bool
    platform: str | None
    recorded: str


class CurrentUserPresence(TypedDict, total=False):
    avatarImageUrl: str
    avatarThumbnail: str | None
    banner: str
    bannerColor: str
    bannerType: str
    bannerUrl: str
    currentAvatarTags: str
    debugflag: str
    displayName: str
    groups: list[str] | None
    iconFrame: str
    iconUrl: str
    id: str
    instance: str | None
    instanceType: str | None
    isRejoining: str | None
    nameplateEffect: str
    platform: str | None
    profileEffect: str
    profilePicOverride: str | None
    status: str | None
    travelingToInstance: str | None
    travelingToWorld: str | None
    userIcon: str | None
    world: str | None


class InstanceContentSettings(TypedDict, total=False):
    drones: bool
    emoji: bool
    pedestals: bool
    prints: bool
    props: bool
    stickers: bool


class User(TypedDict, total=False):
    acceptedPrivacyVersion: int
    acceptedTOSVersion: int
    accountDeletionDate: str | None
    accountDeletionLog: list[Any] | None
    ageVerificationStatus: str
    ageVerified: bool
    allowAvatarCopying: bool
    appleDetails: dict[str, Any]
    bannerColor: str
    bannerType: str
    bannerUrl: str
    date_joined: str
    developerType: str
    displayName: str
    friendKey: str
    friendRequestStatus: str
    iconFrame: str
    iconUrl: str
    id: str
    instanceId: str
    isEconomyCreator: bool
    isFriend: bool
    last_activity: str
    last_login: str
    last_mobile: str | None
    last_platform: str
    location: str
    nameplateEffect: str
    note: str
    platform: str
    profileEffect: str
    pronouns: str
    state: str
    status: str
    statusDescription: str
    tags: list[str]
    travelingToInstance: str
    travelingToLocation: str
    travelingToWorld: str
    worldId: str


class World(TypedDict, total=False):
    authorId: str
    authorName: str
    capacity: int
    created_at: str
    defaultContentSettings: InstanceContentSettings
    description: str
    disabledPropAbilities: list[Any]
    favorites: int
    featured: bool
    heat: int
    id: str
    imageUrl: str
    instances: list[list[Any]]
    isHypeTrainEligible: bool
    labsPublicationDate: str
    name: str
    namespace: str
    occupants: int
    organization: str
    popularity: int
    previewYoutubeId: str | None
    privateOccupants: int
    publicOccupants: int
    publicationDate: str
    recommendedCapacity: int
    releaseStatus: str
    slimInstances: list[Any]
    storeId: str
    tags: list[str]
    thumbnailImageUrl: str
    udonProducts: list[str]
    unityPackages: list[UnityPackage]
    updated_at: str
    urlList: list[str]
    version: int
    visits: int


class UnityPackage(TypedDict, total=False):
    assetUrl: str | None
    assetUrlObject: dict[str, Any]
    assetVersion: int
    created_at: str | None
    id: str
    impostorUrl: str | None
    impostorizerVersion: str
    performanceRating: str
    platform: str
    pluginUrl: str
    pluginUrlObject: dict[str, Any]
    scanStatus: str
    unitySortNumber: int
    unityVersion: str
    variant: str
    worldSignature: str | None


__all__ = [
    "AccountDeletionLog",
    "Badge",
    "CurrentUser",
    "DiscordDetails",
    "PastDisplayName",
    "CurrentUserPlatformHistoryInner",
    "CurrentUserPresence",
    "InstanceContentSettings",
    "User",
    "World",
    "UnityPackage",
]
