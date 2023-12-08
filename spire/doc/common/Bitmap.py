from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

class Bitmap (  Image) :
    """

    """
#    @staticmethod
#
#    def FromHicon(hicon:'IntPtr')->'Bitmap':
#        """
#
#        """
#        intPtrhicon:c_void_p = hicon.Ptr
#
#        dlllib.Bitmap_FromHicon.argtypes=[ c_void_p]
#        dlllib.Bitmap_FromHicon.restype=c_void_p
#        intPtr = dlllib.Bitmap_FromHicon( intPtrhicon)
#        ret = None if intPtr==None else Bitmap(intPtr)
#        return ret
#


#    @staticmethod
#
#    def FromResource(hinstance:'IntPtr',bitmapName:str)->'Bitmap':
#        """
#
#        """
#        intPtrhinstance:c_void_p = hinstance.Ptr
#
#        dlllib.Bitmap_FromResource.argtypes=[ c_void_p,c_void_p]
#        dlllib.Bitmap_FromResource.restype=c_void_p
#        intPtr = dlllib.Bitmap_FromResource( intPtrhinstance,bitmapName)
#        ret = None if intPtr==None else Bitmap(intPtr)
#        return ret
#


#    @dispatch
#
#    def GetHbitmap(self)->IntPtr:
#        """
#
#        """
#        dlllib.Bitmap_GetHbitmap.argtypes=[c_void_p]
#        dlllib.Bitmap_GetHbitmap.restype=c_void_p
#        intPtr = dlllib.Bitmap_GetHbitmap(self.Ptr)
#        ret = None if intPtr==None else IntPtr(intPtr)
#        return ret
#


#    @dispatch
#
#    def GetHbitmap(self ,background:Color)->IntPtr:
#        """
#
#        """
#        intPtrbackground:c_void_p = background.Ptr
#
#        dlllib.Bitmap_GetHbitmapB.argtypes=[c_void_p ,c_void_p]
#        dlllib.Bitmap_GetHbitmapB.restype=c_void_p
#        intPtr = dlllib.Bitmap_GetHbitmapB(self.Ptr, intPtrbackground)
#        ret = None if intPtr==None else IntPtr(intPtr)
#        return ret
#


#
#    def GetHicon(self)->'IntPtr':
#        """
#
#        """
#        dlllib.Bitmap_GetHicon.argtypes=[c_void_p]
#        dlllib.Bitmap_GetHicon.restype=c_void_p
#        intPtr = dlllib.Bitmap_GetHicon(self.Ptr)
#        ret = None if intPtr==None else IntPtr(intPtr)
#        return ret
#


    @dispatch

    def Clone(self ,rect:Rectangle,format:PixelFormat)->'Bitmap':
        """

        """
        intPtrrect:c_void_p = rect.Ptr
        enumformat:c_int = format.value

        dlllib.Bitmap_Clone.argtypes=[c_void_p ,c_void_p,c_int]
        dlllib.Bitmap_Clone.restype=c_void_p
        intPtr = dlllib.Bitmap_Clone(self.Ptr, intPtrrect,enumformat)
        ret = None if intPtr==None else Bitmap(intPtr)
        return ret


    @dispatch

    def Clone(self ,rect:RectangleF,format:PixelFormat)->'Bitmap':
        """

        """
        intPtrrect:c_void_p = rect.Ptr
        enumformat:c_int = format.value

        dlllib.Bitmap_CloneRF.argtypes=[c_void_p ,c_void_p,c_int]
        dlllib.Bitmap_CloneRF.restype=c_void_p
        intPtr = dlllib.Bitmap_CloneRF(self.Ptr, intPtrrect,enumformat)
        ret = None if intPtr==None else Bitmap(intPtr)
        return ret


    @dispatch
    def MakeTransparent(self):
        """

        """
        dlllib.Bitmap_MakeTransparent.argtypes=[c_void_p]
        dlllib.Bitmap_MakeTransparent(self.Ptr)

    @dispatch

    def MakeTransparent(self ,transparentColor:Color):
        """

        """
        intPtrtransparentColor:c_void_p = transparentColor.Ptr

        dlllib.Bitmap_MakeTransparentT.argtypes=[c_void_p ,c_void_p]
        dlllib.Bitmap_MakeTransparentT(self.Ptr, intPtrtransparentColor)

#    @dispatch
#
#    def LockBits(self ,rect:Rectangle,flags:'ImageLockMode',format:PixelFormat)->BitmapData:
#        """
#
#        """
#        intPtrrect:c_void_p = rect.Ptr
#        enumflags:c_int = flags.value
#        enumformat:c_int = format.value
#
#        dlllib.Bitmap_LockBits.argtypes=[c_void_p ,c_void_p,c_int,c_int]
#        dlllib.Bitmap_LockBits.restype=c_void_p
#        intPtr = dlllib.Bitmap_LockBits(self.Ptr, intPtrrect,enumflags,enumformat)
#        ret = None if intPtr==None else BitmapData(intPtr)
#        return ret
#


#    @dispatch
#
#    def LockBits(self ,rect:Rectangle,flags:'ImageLockMode',format:PixelFormat,bitmapData:'BitmapData')->BitmapData:
#        """
#
#        """
#        intPtrrect:c_void_p = rect.Ptr
#        enumflags:c_int = flags.value
#        enumformat:c_int = format.value
#        intPtrbitmapData:c_void_p = bitmapData.Ptr
#
#        dlllib.Bitmap_LockBitsRFFB.argtypes=[c_void_p ,c_void_p,c_int,c_int,c_void_p]
#        dlllib.Bitmap_LockBitsRFFB.restype=c_void_p
#        intPtr = dlllib.Bitmap_LockBitsRFFB(self.Ptr, intPtrrect,enumflags,enumformat,intPtrbitmapData)
#        ret = None if intPtr==None else BitmapData(intPtr)
#        return ret
#


#
#    def UnlockBits(self ,bitmapdata:'BitmapData'):
#        """
#
#        """
#        intPtrbitmapdata:c_void_p = bitmapdata.Ptr
#
#        dlllib.Bitmap_UnlockBits.argtypes=[c_void_p ,c_void_p]
#        dlllib.Bitmap_UnlockBits(self.Ptr, intPtrbitmapdata)



    def GetPixel(self ,x:int,y:int)->'Color':
        """

        """
        
        dlllib.Bitmap_GetPixel.argtypes=[c_void_p ,c_int,c_int]
        dlllib.Bitmap_GetPixel.restype=c_void_p
        intPtr = dlllib.Bitmap_GetPixel(self.Ptr, x,y)
        ret = None if intPtr==None else Color(intPtr)
        return ret



    def SetPixel(self ,x:int,y:int,color:'Color'):
        """

        """
        intPtrcolor:c_void_p = color.Ptr

        dlllib.Bitmap_SetPixel.argtypes=[c_void_p ,c_int,c_int,c_void_p]
        dlllib.Bitmap_SetPixel(self.Ptr, x,y,intPtrcolor)


    def SetResolution(self ,xDpi:float,yDpi:float):
        """

        """
        
        dlllib.Bitmap_SetResolution.argtypes=[c_void_p ,c_float,c_float]
        dlllib.Bitmap_SetResolution(self.Ptr, xDpi,yDpi)

