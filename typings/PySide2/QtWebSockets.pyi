# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtWebSockets, except for defaults which are replaced by "...".
"""

# Module PySide2.QtWebSockets
import PySide2
import typing

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtNetwork
import PySide2.QtWebSockets


class QMaskGenerator(PySide2.QtCore.QObject):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def nextMask(self) -> int: ...
    def seed(self) -> bool: ...


class QWebSocket(PySide2.QtCore.QObject):

    def __init__(self, origin:str=..., version:PySide2.QtWebSockets.QWebSocketProtocol.Version=..., parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def abort(self) -> None: ...
    def bytesToWrite(self) -> int: ...
    def close(self, closeCode:PySide2.QtWebSockets.QWebSocketProtocol.CloseCode=..., reason:str=...) -> None: ...
    def closeCode(self) -> PySide2.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def closeReason(self) -> str: ...
    def error(self) -> PySide2.QtNetwork.QAbstractSocket.SocketError: ...
    def errorString(self) -> str: ...
    def flush(self) -> bool: ...
    def isValid(self) -> bool: ...
    def localAddress(self) -> PySide2.QtNetwork.QHostAddress: ...
    def localPort(self) -> int: ...
    def maskGenerator(self) -> PySide2.QtWebSockets.QMaskGenerator: ...
    def maxAllowedIncomingFrameSize(self) -> int: ...
    def maxAllowedIncomingMessageSize(self) -> int: ...
    @staticmethod
    def maxIncomingFrameSize() -> int: ...
    @staticmethod
    def maxIncomingMessageSize() -> int: ...
    @staticmethod
    def maxOutgoingFrameSize() -> int: ...
    @typing.overload
    def open(self, request:PySide2.QtNetwork.QNetworkRequest) -> None: ...
    @typing.overload
    def open(self, url:PySide2.QtCore.QUrl) -> None: ...
    def origin(self) -> str: ...
    def outgoingFrameSize(self) -> int: ...
    def pauseMode(self) -> PySide2.QtNetwork.QAbstractSocket.PauseModes: ...
    def peerAddress(self) -> PySide2.QtNetwork.QHostAddress: ...
    def peerName(self) -> str: ...
    def peerPort(self) -> int: ...
    def ping(self, payload:PySide2.QtCore.QByteArray=...) -> None: ...
    def proxy(self) -> PySide2.QtNetwork.QNetworkProxy: ...
    def readBufferSize(self) -> int: ...
    def request(self) -> PySide2.QtNetwork.QNetworkRequest: ...
    def requestUrl(self) -> PySide2.QtCore.QUrl: ...
    def resourceName(self) -> str: ...
    def resume(self) -> None: ...
    def sendBinaryMessage(self, data:PySide2.QtCore.QByteArray) -> int: ...
    def sendTextMessage(self, message:str) -> int: ...
    def setMaskGenerator(self, maskGenerator:PySide2.QtWebSockets.QMaskGenerator) -> None: ...
    def setMaxAllowedIncomingFrameSize(self, maxAllowedIncomingFrameSize:int) -> None: ...
    def setMaxAllowedIncomingMessageSize(self, maxAllowedIncomingMessageSize:int) -> None: ...
    def setOutgoingFrameSize(self, outgoingFrameSize:int) -> None: ...
    def setPauseMode(self, pauseMode:PySide2.QtNetwork.QAbstractSocket.PauseModes) -> None: ...
    def setProxy(self, networkProxy:PySide2.QtNetwork.QNetworkProxy) -> None: ...
    def setReadBufferSize(self, size:int) -> None: ...
    def state(self) -> PySide2.QtNetwork.QAbstractSocket.SocketState: ...
    def version(self) -> PySide2.QtWebSockets.QWebSocketProtocol.Version: ...

    aboutToClose: PySide2.QtCore.Signal
    binaryFrameReceived: PySide2.QtCore.Signal
    binaryMessageReceived: PySide2.QtCore.Signal
    bytesWritten: PySide2.QtCore.Signal
    connected: PySide2.QtCore.Signal
    disconnected: PySide2.QtCore.Signal
    error: PySide2.QtCore.Signal
    pong: PySide2.QtCore.Signal
    preSharedKeyAuthenticationRequired: PySide2.QtCore.Signal
    proxyAuthenticationRequired: PySide2.QtCore.Signal
    readChannelFinished: PySide2.QtCore.Signal
    stateChanged: PySide2.QtCore.Signal
    textFrameReceived: PySide2.QtCore.Signal
    textMessageReceived: PySide2.QtCore.Signal


class QWebSocketCorsAuthenticator(Shiboken.Object):

    @typing.overload
    def __init__(self, origin:str) -> None: ...
    @typing.overload
    def __init__(self, other:PySide2.QtWebSockets.QWebSocketCorsAuthenticator) -> None: ...

    def allowed(self) -> bool: ...
    def origin(self) -> str: ...
    def setAllowed(self, allowed:bool) -> None: ...
    def swap(self, other:PySide2.QtWebSockets.QWebSocketCorsAuthenticator) -> None: ...


class QWebSocketProtocol(Shiboken.Object):
    VersionUnknown           : QWebSocketProtocol = ... # -0x1
    Version0                 : QWebSocketProtocol = ... # 0x0
    Version4                 : QWebSocketProtocol = ... # 0x4
    Version5                 : QWebSocketProtocol = ... # 0x5
    Version6                 : QWebSocketProtocol = ... # 0x6
    Version7                 : QWebSocketProtocol = ... # 0x7
    Version8                 : QWebSocketProtocol = ... # 0x8
    Version13                : QWebSocketProtocol = ... # 0xd
    VersionLatest            : QWebSocketProtocol = ... # 0xd
    CloseCodeNormal          : QWebSocketProtocol = ... # 0x3e8
    CloseCodeGoingAway       : QWebSocketProtocol = ... # 0x3e9
    CloseCodeProtocolError   : QWebSocketProtocol = ... # 0x3ea
    CloseCodeDatatypeNotSupported: QWebSocketProtocol = ... # 0x3eb
    CloseCodeReserved1004    : QWebSocketProtocol = ... # 0x3ec
    CloseCodeMissingStatusCode: QWebSocketProtocol = ... # 0x3ed
    CloseCodeAbnormalDisconnection: QWebSocketProtocol = ... # 0x3ee
    CloseCodeWrongDatatype   : QWebSocketProtocol = ... # 0x3ef
    CloseCodePolicyViolated  : QWebSocketProtocol = ... # 0x3f0
    CloseCodeTooMuchData     : QWebSocketProtocol = ... # 0x3f1
    CloseCodeMissingExtension: QWebSocketProtocol = ... # 0x3f2
    CloseCodeBadOperation    : QWebSocketProtocol = ... # 0x3f3
    CloseCodeTlsHandshakeFailed: QWebSocketProtocol = ... # 0x3f7

    class CloseCode(object):
        CloseCodeNormal          : QWebSocketProtocol.CloseCode = ... # 0x3e8
        CloseCodeGoingAway       : QWebSocketProtocol.CloseCode = ... # 0x3e9
        CloseCodeProtocolError   : QWebSocketProtocol.CloseCode = ... # 0x3ea
        CloseCodeDatatypeNotSupported: QWebSocketProtocol.CloseCode = ... # 0x3eb
        CloseCodeReserved1004    : QWebSocketProtocol.CloseCode = ... # 0x3ec
        CloseCodeMissingStatusCode: QWebSocketProtocol.CloseCode = ... # 0x3ed
        CloseCodeAbnormalDisconnection: QWebSocketProtocol.CloseCode = ... # 0x3ee
        CloseCodeWrongDatatype   : QWebSocketProtocol.CloseCode = ... # 0x3ef
        CloseCodePolicyViolated  : QWebSocketProtocol.CloseCode = ... # 0x3f0
        CloseCodeTooMuchData     : QWebSocketProtocol.CloseCode = ... # 0x3f1
        CloseCodeMissingExtension: QWebSocketProtocol.CloseCode = ... # 0x3f2
        CloseCodeBadOperation    : QWebSocketProtocol.CloseCode = ... # 0x3f3
        CloseCodeTlsHandshakeFailed: QWebSocketProtocol.CloseCode = ... # 0x3f7

    class Version(object):
        VersionUnknown           : QWebSocketProtocol.Version = ... # -0x1
        Version0                 : QWebSocketProtocol.Version = ... # 0x0
        Version4                 : QWebSocketProtocol.Version = ... # 0x4
        Version5                 : QWebSocketProtocol.Version = ... # 0x5
        Version6                 : QWebSocketProtocol.Version = ... # 0x6
        Version7                 : QWebSocketProtocol.Version = ... # 0x7
        Version8                 : QWebSocketProtocol.Version = ... # 0x8
        Version13                : QWebSocketProtocol.Version = ... # 0xd
        VersionLatest            : QWebSocketProtocol.Version = ... # 0xd


class QWebSocketServer(PySide2.QtCore.QObject):
    SecureMode               : QWebSocketServer = ... # 0x0
    NonSecureMode            : QWebSocketServer = ... # 0x1

    class SslMode(object):
        SecureMode               : QWebSocketServer.SslMode = ... # 0x0
        NonSecureMode            : QWebSocketServer.SslMode = ... # 0x1

    def __init__(self, serverName:str, secureMode:PySide2.QtWebSockets.QWebSocketServer.SslMode, parent:typing.Optional[PySide2.QtCore.QObject]=...) -> None: ...

    def close(self) -> None: ...
    def error(self) -> PySide2.QtWebSockets.QWebSocketProtocol.CloseCode: ...
    def errorString(self) -> str: ...
    def handleConnection(self, socket:PySide2.QtNetwork.QTcpSocket) -> None: ...
    def handshakeTimeoutMS(self) -> int: ...
    def hasPendingConnections(self) -> bool: ...
    def isListening(self) -> bool: ...
    def listen(self, address:PySide2.QtNetwork.QHostAddress=..., port:int=...) -> bool: ...
    def maxPendingConnections(self) -> int: ...
    def nativeDescriptor(self) -> int: ...
    def nextPendingConnection(self) -> PySide2.QtWebSockets.QWebSocket: ...
    def pauseAccepting(self) -> None: ...
    def proxy(self) -> PySide2.QtNetwork.QNetworkProxy: ...
    def resumeAccepting(self) -> None: ...
    def secureMode(self) -> PySide2.QtWebSockets.QWebSocketServer.SslMode: ...
    def serverAddress(self) -> PySide2.QtNetwork.QHostAddress: ...
    def serverName(self) -> str: ...
    def serverPort(self) -> int: ...
    def serverUrl(self) -> PySide2.QtCore.QUrl: ...
    def setHandshakeTimeout(self, msec:int) -> None: ...
    def setMaxPendingConnections(self, numConnections:int) -> None: ...
    def setNativeDescriptor(self, descriptor:int) -> bool: ...
    def setProxy(self, networkProxy:PySide2.QtNetwork.QNetworkProxy) -> None: ...
    def setServerName(self, serverName:str) -> None: ...
    def setSocketDescriptor(self, socketDescriptor:int) -> bool: ...
    def socketDescriptor(self) -> int: ...
    def supportedVersions(self) -> typing.List: ...

# eof
