from __future__ import annotations
from datetime import datetime
from typing import Any, Literal, Optional, List, Tuple, Union
from dataclasses import dataclass

MessageNotificationLevel = Literal[0, 1]

ExplicitContentFilterLevel = Literal[
    "DISABLED",
    "MEMBERS_WITHOUT_ROLES",
    "ALL_MEMBERS"]

MFALevel = Literal[0, 1]

VerificationLevel = Literal[0, 1, 2, 3, 4]

PremiumTier = Literal[0, 1, 2, 3]

PremiumType = Literal[0, 1, 2]
ChannelType = Literal[0, 1, 2, 3, 4, 5, 6]
ActivityType = Literal[0, 1, 2, 3, 4, 5]
MessageType = Literal[
    0, 1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12,
    13, 14, 15, 19, 20]
MessageActivityType = Literal[1, 2, 3, 5]
EmbedType = Literal[
    "rich",
    "image",
    "video",
    "gifv",
    "article",
    "link"]
StickerType = Literal[1, 2, 3]

SystemChannelFlags = Literal[
    1 << 0, 1 << 1,
    1 << 0 | 1 << 1, 0]

Status = Literal["idle", "dnd", "online", "offline"]

GuildFeature = Literal[
    "INVITE_SPLASH", "VIP_REGIONS",
    "VANITY_URL", "VERIFIED",
    "PARTNERED", "COMMUNITY",
    "COMMERCE", "NEWS",
    "DISCOVERABLE", "FEATURABLE",
    "ANIMATED_ICON", "BANNER",
    "WELCOME_SCREEN_ENABLED",
    "MEMBER_VERIFICATION_GATE_ENABLED",
    "PREVIEW_ENABLED"]

UserFlags = int
ActivityFlags = int
MessageFlags = int

Snowflake = str


@dataclass
class RoleTags:
    bot_id: Optional[Snowflake] = None
    integration_id: Optional[Snowflake] = None
    premium_subscriber: Optional[None] = None


@dataclass
class Role:
    id: Snowflake
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    tags: Optional[RoleTags] = None


WebhookUser = Any


@dataclass
class User:
    id: Snowflake
    username: str
    discriminator: str
    avatar: Optional[str]
    bot: Optional[bool] = None
    system: Optional[bool] = None
    mfa_enabled: Optional[bool] = None
    locale: Optional[str] = None
    verified: Optional[bool] = None
    email: Optional[str] = None
    flags: Optional[UserFlags] = None
    premium_type: Optional[PremiumType] = None
    public_flags: Optional[UserFlags] = None


@dataclass
class Member:
    nick: Optional[str]
    roles: List[Snowflake]
    joined_at: datetime
    premium_since: datetime
    deaf: bool
    mute: bool
    user: Optional[User] = None
    pending: Optional[bool] = None
    permissions: Optional[int] = None  # pbs


@dataclass
class ActivityEmoji:
    name: str
    id: Optional[Snowflake] = None
    animated: Optional[bool] = None


@dataclass
class Emoji:
    id: Optional[Snowflake]
    name: Optional[str]
    roles: Optional[List[Role]] = None
    user: Optional[User] = None
    require_colons: Optional[bool] = None
    managed: Optional[bool] = None
    animated: Optional[bool] = None
    available: Optional[bool] = None


@dataclass
class VoiceState:
    channel_id: Optional[Snowflake]
    user_id: Snowflake
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_video: bool
    suppress: bool
    guild_id: Optional[Snowflake] = None
    member: Optional[Member] = None
    self_stream: Optional[bool] = None


@dataclass
class Overwrite:
    id: Snowflake
    type: Literal[0, 1]
    allow: str  # pbs
    deny: str  # pbs


@dataclass
class Channel:
    id: Snowflake
    type: ChannelType
    guild_id: Optional[Snowflake] = None
    position: Optional[int] = None
    permission_overwrites: Optional[List[Overwrite]] = None
    name: Optional[str] = None
    topic: Optional[str] = None
    nsfw: Optional[bool] = None
    last_message_id: Optional[Snowflake] = None
    bitrate: Optional[int] = None
    user_limit: Optional[int] = None
    rate_limit_per_user: Optional[int] = None
    recipients: Optional[List[User]] = None
    icon: Optional[str] = None
    owner_id: Optional[Snowflake] = None
    application_id: Optional[Snowflake] = None
    parent_id: Optional[Snowflake] = None
    last_pin_timestamp: Optional[datetime] = None


@dataclass
class ActivityTimestamps:
    start: Optional[int] = None
    end: Optional[int] = None


@dataclass
class ActivityParty:
    id: Optional[str] = None
    size: Optional[Tuple[int, int]] = None


class ActivityAssets:
    large_image: Optional[str] = None
    large_text: Optional[str] = None
    small_image: Optional[str] = None
    small_text: Optional[str] = None


class ActivitySecrets:
    join: Optional[str] = None
    spectate: Optional[str] = None
    match: Optional[str] = None


@dataclass
class Activity:
    name: str
    type: ActivityType
    created_at: int
    url: Optional[str] = None
    timestamps: Optional[ActivityTimestamps] = None
    application_id: Optional[Snowflake] = None
    details: Optional[str] = None
    state: Optional[str] = None
    emoji: Optional[ActivityEmoji] = None
    party: Optional[ActivityParty] = None
    assets: Optional[ActivityAssets] = None
    secrets: Optional[ActivitySecrets] = None
    instance: Optional[bool] = None
    flags: Optional[ActivityFlags] = None


@dataclass
class ClientStatus:
    """
    Note: A status of offline or invisible will never appear
    """
    desktop: Optional[Status] = None
    mobile: Optional[Status] = None
    web: Optional[Status] = None


@dataclass
class PresenceUpdate:
    user: User
    guild_id: Snowflake
    status: Status
    activities = List[Activity]
    client_status: ClientStatus


@dataclass
class WelcomeScreenChannel:
    channel_id: Snowflake
    description: str
    emoji_id: Optional[Snowflake]
    emoji_name: Optional[str]


@dataclass
class WelcomeScreen:
    description: Optional[str]
    welcome_channels: List[WelcomeScreenChannel]


@dataclass
class UnavailableGuild:
    id: Snowflake
    unavailable: bool


@dataclass
class Guild:
    """
    Represents a discord guild object
    """

    id: Snowflake
    name: str
    icon: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner_id: Snowflake
    region: str
    afk_channel_id: Optional[Snowflake]
    afk_timeout: int
    verification_level: VerificationLevel
    default_message_notifications: MessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: List[Role]
    emojis: List[Emoji]
    features: List[GuildFeature]
    mfa_level: MFALevel
    application_id: Optional[Snowflake]
    system_channel_id: Optional[Snowflake]
    system_channel_flags: SystemChannelFlags
    rules_channel_id: Optional[Snowflake]
    vanity_url_code: Optional[str]
    description: Optional[str]
    banner: Optional[str]
    premium_tier: PremiumTier
    preferred_locale: str
    public_updates_channel_id: Optional[Snowflake]

    icon_hash: Optional[str] = None
    owner: Optional[bool] = None
    permissions: Optional[str] = None  # pbs
    widget_enabled: bool = False
    widget_channel_id: Optional[Snowflake] = None
    joined_at: Optional[str] = None
    large: Optional[bool] = None
    unavailable: Optional[bool] = None
    member_count: Optional[int] = None
    voice_states: Optional[List[VoiceState]] = None
    members: Optional[List[Member]] = None
    channels: Optional[List[Channel]] = None
    presences: Optional[List[PresenceUpdate]] = None
    max_presences: Optional[int] = None
    max_members: Optional[int] = None
    premium_subscription_count: Optional[int] = None
    max_video_channel_users: Optional[int] = None
    approximate_member_count: Optional[int] = None
    approximate_presence_count: Optional[int] = None
    welcome_screen: Optional[WelcomeScreen] = None


@dataclass
class Attachment:
    id: Snowflake
    filename: str
    size: int
    url: str
    proxy_url: str
    height: Optional[int]
    width: Optional[int]


@dataclass
class _EmbedObjBase:
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None


@dataclass
class EmbedThumbnail(_EmbedObjBase):
    pass


@dataclass
class EmbedVideo(_EmbedObjBase):
    pass


@dataclass
class EmbedImage(_EmbedObjBase):
    pass


@dataclass
class EmbedProvider:
    name: Optional[str] = None
    url: Optional[str] = None


@dataclass
class EmbedAuthor:
    name: Optional[str] = None
    url: Optional[str] = None
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None


@dataclass
class EmbedFooter:
    text: str
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None


@dataclass
class EmbedField:
    name: str
    value: str
    inline: Optional[bool] = None


@dataclass
class Embed:
    title: Optional[str] = None
    type: Optional[EmbedType] = None
    description: Optional[str] = None
    url: Optional[str] = None
    timestamp: Optional[datetime] = None
    color: Optional[int] = None
    footer: Optional[EmbedFooter] = None
    image: Optional[EmbedImage] = None
    thumbnail: Optional[EmbedThumbnail] = None
    video: Optional[EmbedVideo] = None
    provider: Optional[EmbedProvider] = None
    author: Optional[EmbedAuthor] = None
    fields: Optional[List[EmbedField]] = None


@dataclass
class ChannelMention:
    id: Snowflake
    guild_id: Snowflake
    type: ChannelType
    name: str


@dataclass
class Reaction:
    count: int
    me: bool
    emoji: Emoji  # ?


@dataclass
class MessageActivity:
    type: MessageActivityType
    party_id: Optional[str] = None


@dataclass
class MessageApplication:
    id: Snowflake
    description: str
    icon: Optional[str]
    name: str
    cover_image: Optional[str] = None


@dataclass
class MessageReference:
    message_id: Optional[Snowflake] = None
    channel_id: Optional[Snowflake] = None
    guild_id: Optional[Snowflake] = None


@dataclass
class Sticker:
    id: Snowflake
    pack_id: Snowflake
    name: str
    description: str
    asset: str
    preview_asset: Optional[str]
    format_type: StickerType
    tags: Optional[str] = None


@dataclass
class Message:
    id: Snowflake
    channel_id: Snowflake
    author: User# Union[User, WebhookUser]  # ?
    content: str
    timestamp: datetime
    edited_timestamp: Optional[datetime]
    tts: bool
    mention_everyone: bool
    mentions: List[User]  # ?
    attachments: List[Attachment]
    embeds: List[Embed]
    pinned: bool
    type: MessageType
    guild_id: Optional[Snowflake] = None
    member: Optional[Member] = None
    mention_channels: Optional[List[ChannelMention]] = None
    reactions: Optional[Reaction] = None
    nonce: Optional[Any] = None
    webhook_id: Optional[Snowflake] = None
    activity: Optional[MessageActivity] = None
    application: Optional[MessageApplication] = None
    message_reference: Optional[MessageReference] = None
    flags: Optional[MessageFlags] = None
    stickers: Optional[List[Sticker]] = None
    referenced_message: Optional[Message] = None  # ?
