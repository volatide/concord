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
PySide2.Qt3DExtras, except for defaults which are replaced by "...".
"""

# Module PySide2.Qt3DExtras
import PySide2
import typing

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtGui
import PySide2.Qt3DCore
import PySide2.Qt3DRender
import PySide2.Qt3DExtras


class Qt3DExtras(Shiboken.Object):

    class QAbstractCameraController(PySide2.Qt3DCore.QEntity):

        class InputState(Shiboken.Object):

            @typing.overload
            def __init__(self) -> None: ...
            @typing.overload
            def __init__(self, InputState:PySide2.Qt3DExtras.Qt3DExtras.QAbstractCameraController.InputState) -> None: ...

            @staticmethod
            def __copy__() -> None: ...

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def acceleration(self) -> float: ...
        def camera(self) -> PySide2.Qt3DRender.Qt3DRender.QCamera: ...
        def deceleration(self) -> float: ...
        def linearSpeed(self) -> float: ...
        def lookSpeed(self) -> float: ...
        def setAcceleration(self, acceleration:float) -> None: ...
        def setCamera(self, camera:PySide2.Qt3DRender.Qt3DRender.QCamera) -> None: ...
        def setDeceleration(self, deceleration:float) -> None: ...
        def setLinearSpeed(self, linearSpeed:float) -> None: ...
        def setLookSpeed(self, lookSpeed:float) -> None: ...

    class QAbstractSpriteSheet(PySide2.Qt3DCore.QNode):
        def currentIndex(self) -> int: ...
        def setCurrentIndex(self, currentIndex:int) -> None: ...
        def setTexture(self, texture:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def texture(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureTransform(self) -> PySide2.QtGui.QMatrix3x3: ...

    class QConeGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def bottomRadius(self) -> float: ...
        def hasBottomEndcap(self) -> bool: ...
        def hasTopEndcap(self) -> bool: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def length(self) -> float: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def rings(self) -> int: ...
        def setBottomRadius(self, bottomRadius:float) -> None: ...
        def setHasBottomEndcap(self, hasBottomEndcap:bool) -> None: ...
        def setHasTopEndcap(self, hasTopEndcap:bool) -> None: ...
        def setLength(self, length:float) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def setTopRadius(self, topRadius:float) -> None: ...
        def slices(self) -> int: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def topRadius(self) -> float: ...
        def updateIndices(self) -> None: ...
        def updateVertices(self) -> None: ...

    class QConeMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def bottomRadius(self) -> float: ...
        def hasBottomEndcap(self) -> bool: ...
        def hasTopEndcap(self) -> bool: ...
        def length(self) -> float: ...
        def rings(self) -> int: ...
        def setBottomRadius(self, bottomRadius:float) -> None: ...
        def setFirstInstance(self, firstInstance:int) -> None: ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry) -> None: ...
        def setHasBottomEndcap(self, hasBottomEndcap:bool) -> None: ...
        def setHasTopEndcap(self, hasTopEndcap:bool) -> None: ...
        def setIndexOffset(self, indexOffset:int) -> None: ...
        def setInstanceCount(self, instanceCount:int) -> None: ...
        def setLength(self, length:float) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled:bool) -> None: ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType) -> None: ...
        def setRestartIndexValue(self, index:int) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def setTopRadius(self, topRadius:float) -> None: ...
        def setVertexCount(self, vertexCount:int) -> None: ...
        def slices(self) -> int: ...
        def topRadius(self) -> float: ...

    class QCuboidGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def setXExtent(self, xExtent:float) -> None: ...
        def setXYMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setXZMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setYExtent(self, yExtent:float) -> None: ...
        def setYZMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setZExtent(self, zExtent:float) -> None: ...
        def tangentAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self) -> None: ...
        def updateVertices(self) -> None: ...
        def xExtent(self) -> float: ...
        def xyMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def xzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def yExtent(self) -> float: ...
        def yzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def zExtent(self) -> float: ...

    class QCuboidMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def setFirstInstance(self, firstInstance:int) -> None: ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry) -> None: ...
        def setIndexOffset(self, indexOffset:int) -> None: ...
        def setInstanceCount(self, instanceCount:int) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled:bool) -> None: ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType) -> None: ...
        def setRestartIndexValue(self, index:int) -> None: ...
        def setVertexCount(self, vertexCount:int) -> None: ...
        def setXExtent(self, xExtent:float) -> None: ...
        def setXYMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setXZMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setYExtent(self, yExtent:float) -> None: ...
        def setYZMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setZExtent(self, zExtent:float) -> None: ...
        def xExtent(self) -> float: ...
        def xyMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def xzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def yExtent(self) -> float: ...
        def yzMeshResolution(self) -> PySide2.QtCore.QSize: ...
        def zExtent(self) -> float: ...

    class QCylinderGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def length(self) -> float: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setLength(self, length:float) -> None: ...
        def setRadius(self, radius:float) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def slices(self) -> int: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self) -> None: ...
        def updateVertices(self) -> None: ...

    class QCylinderMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def length(self) -> float: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setFirstInstance(self, firstInstance:int) -> None: ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry) -> None: ...
        def setIndexOffset(self, indexOffset:int) -> None: ...
        def setInstanceCount(self, instanceCount:int) -> None: ...
        def setLength(self, length:float) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled:bool) -> None: ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType) -> None: ...
        def setRadius(self, radius:float) -> None: ...
        def setRestartIndexValue(self, index:int) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def setVertexCount(self, vertexCount:int) -> None: ...
        def slices(self) -> int: ...

    class QDiffuseMapMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, color:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.QtGui.QColor) -> None: ...
        def setTextureScale(self, textureScale:float) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...
        def textureScale(self) -> float: ...

    class QDiffuseSpecularMapMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setTextureScale(self, textureScale:float) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureScale(self) -> float: ...

    class QDiffuseSpecularMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> typing.Any: ...
        def isAlphaBlendingEnabled(self) -> bool: ...
        def normal(self) -> typing.Any: ...
        def setAlphaBlendingEnabled(self, enabled:bool) -> None: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:typing.Any) -> None: ...
        def setNormal(self, normal:typing.Any) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:typing.Any) -> None: ...
        def setTextureScale(self, textureScale:float) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> typing.Any: ...
        def textureScale(self) -> float: ...

    class QExtrudedTextGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def extrusionLength(self) -> float: ...
        def font(self) -> PySide2.QtGui.QFont: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def setDepth(self, extrusionLength:float) -> None: ...
        def setFont(self, font:PySide2.QtGui.QFont) -> None: ...
        def setText(self, text:str) -> None: ...
        def text(self) -> str: ...

    class QExtrudedTextMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def depth(self) -> float: ...
        def font(self) -> PySide2.QtGui.QFont: ...
        def setDepth(self, depth:float) -> None: ...
        def setFont(self, font:PySide2.QtGui.QFont) -> None: ...
        def setText(self, text:str) -> None: ...
        def text(self) -> str: ...

    class QFirstPersonCameraController(PySide2.Qt3DExtras.QAbstractCameraController):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...


    class QForwardRenderer(PySide2.Qt3DRender.QTechniqueFilter):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def buffersToClear(self) -> PySide2.Qt3DRender.Qt3DRender.QClearBuffers.BufferType: ...
        def camera(self) -> PySide2.Qt3DCore.Qt3DCore.QEntity: ...
        def clearColor(self) -> PySide2.QtGui.QColor: ...
        def externalRenderTargetSize(self) -> PySide2.QtCore.QSize: ...
        def gamma(self) -> float: ...
        def isFrustumCullingEnabled(self) -> bool: ...
        def setBuffersToClear(self, arg__1:PySide2.Qt3DRender.Qt3DRender.QClearBuffers.BufferType) -> None: ...
        def setCamera(self, camera:PySide2.Qt3DCore.Qt3DCore.QEntity) -> None: ...
        def setClearColor(self, clearColor:PySide2.QtGui.QColor) -> None: ...
        def setExternalRenderTargetSize(self, size:PySide2.QtCore.QSize) -> None: ...
        def setFrustumCullingEnabled(self, enabled:bool) -> None: ...
        def setGamma(self, gamma:float) -> None: ...
        def setShowDebugOverlay(self, showDebugOverlay:bool) -> None: ...
        def setSurface(self, surface:PySide2.QtCore.QObject) -> None: ...
        def setViewportRect(self, viewportRect:PySide2.QtCore.QRectF) -> None: ...
        def showDebugOverlay(self) -> bool: ...
        def surface(self) -> PySide2.QtCore.QObject: ...
        def viewportRect(self) -> PySide2.QtCore.QRectF: ...

    class QGoochMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def alpha(self) -> float: ...
        def beta(self) -> float: ...
        def cool(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def setAlpha(self, alpha:float) -> None: ...
        def setBeta(self, beta:float) -> None: ...
        def setCool(self, cool:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.QtGui.QColor) -> None: ...
        def setWarm(self, warm:PySide2.QtGui.QColor) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...
        def warm(self) -> PySide2.QtGui.QColor: ...

    class QMetalRoughMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambientOcclusion(self) -> typing.Any: ...
        def baseColor(self) -> typing.Any: ...
        def metalness(self) -> typing.Any: ...
        def normal(self) -> typing.Any: ...
        def roughness(self) -> typing.Any: ...
        def setAmbientOcclusion(self, ambientOcclusion:typing.Any) -> None: ...
        def setBaseColor(self, baseColor:typing.Any) -> None: ...
        def setMetalness(self, metalness:typing.Any) -> None: ...
        def setNormal(self, normal:typing.Any) -> None: ...
        def setRoughness(self, roughness:typing.Any) -> None: ...
        def setTextureScale(self, textureScale:float) -> None: ...
        def textureScale(self) -> float: ...

    class QMorphPhongMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def interpolator(self) -> float: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor) -> None: ...
        def setInterpolator(self, interpolator:float) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.QtGui.QColor) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...

    class QNormalDiffuseMapAlphaMaterial(PySide2.Qt3DExtras.QNormalDiffuseMapMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...


    class QNormalDiffuseMapMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def normal(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setNormal(self, normal:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.QtGui.QColor) -> None: ...
        def setTextureScale(self, textureScale:float) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...
        def textureScale(self) -> float: ...

    class QNormalDiffuseSpecularMapMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def normal(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setNormal(self, normal:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setTextureScale(self, textureScale:float) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureScale(self) -> float: ...

    class QOrbitCameraController(PySide2.Qt3DExtras.QAbstractCameraController):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def setZoomInLimit(self, zoomInLimit:float) -> None: ...
        def zoomInLimit(self) -> float: ...

    class QPerVertexColorMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...


    class QPhongAlphaMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def alpha(self) -> float: ...
        def ambient(self) -> PySide2.QtGui.QColor: ...
        def blendFunctionArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction: ...
        def destinationAlphaArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def destinationRgbArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def setAlpha(self, alpha:float) -> None: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setBlendFunctionArg(self, blendFunctionArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquation.BlendFunction) -> None: ...
        def setDestinationAlphaArg(self, destinationAlphaArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending) -> None: ...
        def setDestinationRgbArg(self, destinationRgbArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending) -> None: ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSourceAlphaArg(self, sourceAlphaArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending) -> None: ...
        def setSourceRgbArg(self, sourceRgbArg:PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending) -> None: ...
        def setSpecular(self, specular:PySide2.QtGui.QColor) -> None: ...
        def shininess(self) -> float: ...
        def sourceAlphaArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def sourceRgbArg(self) -> PySide2.Qt3DRender.Qt3DRender.QBlendEquationArguments.Blending: ...
        def specular(self) -> PySide2.QtGui.QColor: ...

    class QPhongMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def ambient(self) -> PySide2.QtGui.QColor: ...
        def diffuse(self) -> PySide2.QtGui.QColor: ...
        def setAmbient(self, ambient:PySide2.QtGui.QColor) -> None: ...
        def setDiffuse(self, diffuse:PySide2.QtGui.QColor) -> None: ...
        def setShininess(self, shininess:float) -> None: ...
        def setSpecular(self, specular:PySide2.QtGui.QColor) -> None: ...
        def shininess(self) -> float: ...
        def specular(self) -> PySide2.QtGui.QColor: ...

    class QPlaneGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def height(self) -> float: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def mirrored(self) -> bool: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def resolution(self) -> PySide2.QtCore.QSize: ...
        def setHeight(self, height:float) -> None: ...
        def setMirrored(self, mirrored:bool) -> None: ...
        def setResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setWidth(self, width:float) -> None: ...
        def tangentAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self) -> None: ...
        def updateVertices(self) -> None: ...
        def width(self) -> float: ...

    class QPlaneMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def height(self) -> float: ...
        def meshResolution(self) -> PySide2.QtCore.QSize: ...
        def mirrored(self) -> bool: ...
        def setFirstInstance(self, firstInstance:int) -> None: ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry) -> None: ...
        def setHeight(self, height:float) -> None: ...
        def setIndexOffset(self, indexOffset:int) -> None: ...
        def setInstanceCount(self, instanceCount:int) -> None: ...
        def setMeshResolution(self, resolution:PySide2.QtCore.QSize) -> None: ...
        def setMirrored(self, mirrored:bool) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled:bool) -> None: ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType) -> None: ...
        def setRestartIndexValue(self, index:int) -> None: ...
        def setVertexCount(self, vertexCount:int) -> None: ...
        def setWidth(self, width:float) -> None: ...
        def width(self) -> float: ...

    class QSkyboxEntity(PySide2.Qt3DCore.QEntity):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def baseName(self) -> str: ...
        def extension(self) -> str: ...
        def isGammaCorrectEnabled(self) -> bool: ...
        def setBaseName(self, path:str) -> None: ...
        def setExtension(self, extension:str) -> None: ...
        def setGammaCorrectEnabled(self, enabled:bool) -> None: ...

    class QSphereGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def generateTangents(self) -> bool: ...
        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setGenerateTangents(self, gen:bool) -> None: ...
        def setRadius(self, radius:float) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def slices(self) -> int: ...
        def tangentAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self) -> None: ...
        def updateVertices(self) -> None: ...

    class QSphereMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def generateTangents(self) -> bool: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setFirstInstance(self, firstInstance:int) -> None: ...
        def setGenerateTangents(self, gen:bool) -> None: ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry) -> None: ...
        def setIndexOffset(self, indexOffset:int) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled:bool) -> None: ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType) -> None: ...
        def setRadius(self, radius:float) -> None: ...
        def setRestartIndexValue(self, index:int) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def setVertexCount(self, vertexCount:int) -> None: ...
        def slices(self) -> int: ...

    class QSpriteGrid(PySide2.Qt3DExtras.QAbstractSpriteSheet):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def columns(self) -> int: ...
        def rows(self) -> int: ...
        def setColumns(self, columns:int) -> None: ...
        def setRows(self, rows:int) -> None: ...

    class QSpriteSheet(PySide2.Qt3DExtras.QAbstractSpriteSheet):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        @typing.overload
        def addSprite(self, sprite:PySide2.Qt3DExtras.Qt3DExtras.QSpriteSheetItem) -> None: ...
        @typing.overload
        def addSprite(self, x:int, y:int, width:int, height:int) -> PySide2.Qt3DExtras.Qt3DExtras.QSpriteSheetItem: ...
        def removeSprite(self, sprite:PySide2.Qt3DExtras.Qt3DExtras.QSpriteSheetItem) -> None: ...
        def setSprites(self, sprites:typing.List) -> None: ...
        def sprites(self) -> typing.List: ...

    class QSpriteSheetItem(PySide2.Qt3DCore.QNode):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def height(self) -> int: ...
        def setHeight(self, height:int) -> None: ...
        def setWidth(self, width:int) -> None: ...
        def setX(self, x:int) -> None: ...
        def setY(self, y:int) -> None: ...
        def width(self) -> int: ...
        def x(self) -> int: ...
        def y(self) -> int: ...

    class QText2DEntity(PySide2.Qt3DCore.QEntity):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def color(self) -> PySide2.QtGui.QColor: ...
        def font(self) -> PySide2.QtGui.QFont: ...
        def height(self) -> float: ...
        def setColor(self, color:PySide2.QtGui.QColor) -> None: ...
        def setFont(self, font:PySide2.QtGui.QFont) -> None: ...
        def setHeight(self, height:float) -> None: ...
        def setText(self, text:str) -> None: ...
        def setWidth(self, width:float) -> None: ...
        def text(self) -> str: ...
        def width(self) -> float: ...

    class QTextureMaterial(PySide2.Qt3DRender.QMaterial):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def isAlphaBlendingEnabled(self) -> bool: ...
        def setAlphaBlendingEnabled(self, enabled:bool) -> None: ...
        def setTexture(self, texture:PySide2.Qt3DRender.Qt3DRender.QAbstractTexture) -> None: ...
        def setTextureOffset(self, textureOffset:PySide2.QtGui.QVector2D) -> None: ...
        def setTextureTransform(self, matrix:PySide2.QtGui.QMatrix3x3) -> None: ...
        def texture(self) -> PySide2.Qt3DRender.Qt3DRender.QAbstractTexture: ...
        def textureOffset(self) -> PySide2.QtGui.QVector2D: ...
        def textureTransform(self) -> PySide2.QtGui.QMatrix3x3: ...

    class QTorusGeometry(PySide2.Qt3DRender.QGeometry):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def indexAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def minorRadius(self) -> float: ...
        def normalAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def positionAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setMinorRadius(self, minorRadius:float) -> None: ...
        def setRadius(self, radius:float) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def slices(self) -> int: ...
        def texCoordAttribute(self) -> PySide2.Qt3DRender.Qt3DRender.QAttribute: ...
        def updateIndices(self) -> None: ...
        def updateVertices(self) -> None: ...

    class QTorusMesh(PySide2.Qt3DRender.QGeometryRenderer):

        def __init__(self, parent:typing.Optional[PySide2.Qt3DCore.Qt3DCore.QNode]=...) -> None: ...

        def minorRadius(self) -> float: ...
        def radius(self) -> float: ...
        def rings(self) -> int: ...
        def setFirstInstance(self, firstInstance:int) -> None: ...
        def setGeometry(self, geometry:PySide2.Qt3DRender.Qt3DRender.QGeometry) -> None: ...
        def setIndexOffset(self, indexOffset:int) -> None: ...
        def setInstanceCount(self, instanceCount:int) -> None: ...
        def setMinorRadius(self, minorRadius:float) -> None: ...
        def setPrimitiveRestartEnabled(self, enabled:bool) -> None: ...
        def setPrimitiveType(self, primitiveType:PySide2.Qt3DRender.Qt3DRender.QGeometryRenderer.PrimitiveType) -> None: ...
        def setRadius(self, radius:float) -> None: ...
        def setRestartIndexValue(self, index:int) -> None: ...
        def setRings(self, rings:int) -> None: ...
        def setSlices(self, slices:int) -> None: ...
        def setVertexCount(self, vertexCount:int) -> None: ...
        def slices(self) -> int: ...

    class Qt3DWindow(PySide2.QtGui.QWindow):

        def __init__(self, screen:typing.Optional[PySide2.QtGui.QScreen]=..., arg__2:PySide2.Qt3DRender.Qt3DRender.API=...) -> None: ...

        def activeFrameGraph(self) -> PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode: ...
        def camera(self) -> PySide2.Qt3DRender.Qt3DRender.QCamera: ...
        def defaultFrameGraph(self) -> PySide2.Qt3DExtras.Qt3DExtras.QForwardRenderer: ...
        def event(self, e:PySide2.QtCore.QEvent) -> bool: ...
        @typing.overload
        def registerAspect(self, aspect:PySide2.Qt3DCore.Qt3DCore.QAbstractAspect) -> None: ...
        @typing.overload
        def registerAspect(self, name:str) -> None: ...
        def renderSettings(self) -> PySide2.Qt3DRender.Qt3DRender.QRenderSettings: ...
        def resizeEvent(self, arg__1:PySide2.QtGui.QResizeEvent) -> None: ...
        def setActiveFrameGraph(self, activeFrameGraph:PySide2.Qt3DRender.Qt3DRender.QFrameGraphNode) -> None: ...
        def setRootEntity(self, root:PySide2.Qt3DCore.Qt3DCore.QEntity) -> None: ...
        def showEvent(self, e:PySide2.QtGui.QShowEvent) -> None: ...
    @staticmethod
    def setupWindowSurface(window:PySide2.QtGui.QWindow, arg__2:PySide2.Qt3DRender.Qt3DRender.API) -> None: ...

# eof
