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

class Font (SpireObject) :
    """

    """
#    @staticmethod
#
#    def FromHfont(hfont:'IntPtr')->'Font':
#        """
#
#        """
#        intPtrhfont:c_void_p = hfont.Ptr
#
#        dlllib.Font_FromHfont.argtypes=[ c_void_p]
#        dlllib.Font_FromHfont.restype=c_void_p
#        intPtr = dlllib.Font_FromHfont( intPtrhfont)
#        ret = None if intPtr==None else Font(intPtr)
#        return ret
#


#    @property
#
#    def FontFamily(self)->'FontFamily':
#        """
#
#        """
#        dlllib.Font_get_FontFamily.argtypes=[c_void_p]
#        dlllib.Font_get_FontFamily.restype=c_void_p
#        intPtr = dlllib.Font_get_FontFamily(self.Ptr)
#        ret = None if intPtr==None else FontFamily(intPtr)
#        return ret
#


    @property
    def GdiCharSet(self)->int:
        """

        """
        dlllib.Font_get_GdiCharSet.argtypes=[c_void_p]
        dlllib.Font_get_GdiCharSet.restype=c_int
        ret = dlllib.Font_get_GdiCharSet(self.Ptr)
        return ret

    @property
    def GdiVerticalFont(self)->bool:
        """

        """
        dlllib.Font_get_GdiVerticalFont.argtypes=[c_void_p]
        dlllib.Font_get_GdiVerticalFont.restype=c_bool
        ret = dlllib.Font_get_GdiVerticalFont(self.Ptr)
        return ret

    @property
    def Italic(self)->bool:
        """

        """
        dlllib.Font_get_Italic.argtypes=[c_void_p]
        dlllib.Font_get_Italic.restype=c_bool
        ret = dlllib.Font_get_Italic(self.Ptr)
        return ret

    @property

    def OriginalFontName(self)->str:
        """

        """
        dlllib.Font_get_OriginalFontName.argtypes=[c_void_p]
        dlllib.Font_get_OriginalFontName.restype=c_void_p
        ret = PtrToStr(dlllib.Font_get_OriginalFontName(self.Ptr))
        return ret


    @dispatch

    def ToLogFont(self ,logFont:SpireObject):
        """

        """
        intPtrlogFont:c_void_p = logFont.Ptr

        dlllib.Font_ToLogFont.argtypes=[c_void_p ,c_void_p]
        dlllib.Font_ToLogFont(self.Ptr, intPtrlogFont)

#    @dispatch
#
#    def ToLogFont(self ,logFont:SpireObject,graphics:'Graphics'):
#        """
#
#        """
#        intPtrlogFont:c_void_p = logFont.Ptr
#        intPtrgraphics:c_void_p = graphics.Ptr
#
#        dlllib.Font_ToLogFontLG.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Font_ToLogFontLG(self.Ptr, intPtrlogFont,intPtrgraphics)


#
#    def ToHfont(self)->'IntPtr':
#        """
#
#        """
#        dlllib.Font_ToHfont.argtypes=[c_void_p]
#        dlllib.Font_ToHfont.restype=c_void_p
#        intPtr = dlllib.Font_ToHfont(self.Ptr)
#        ret = None if intPtr==None else IntPtr(intPtr)
#        return ret
#


    @property

    def Style(self)->'FontStyle':
        """

        """
        dlllib.Font_get_Style.argtypes=[c_void_p]
        dlllib.Font_get_Style.restype=c_int
        ret = dlllib.Font_get_Style(self.Ptr)
        objwraped = FontStyle(ret)
        return objwraped

    @property
    def Size(self)->float:
        """

        """
        dlllib.Font_get_Size.argtypes=[c_void_p]
        dlllib.Font_get_Size.restype=c_float
        ret = dlllib.Font_get_Size(self.Ptr)
        return ret

    @property
    def SizeInPoints(self)->float:
        """

        """
        dlllib.Font_get_SizeInPoints.argtypes=[c_void_p]
        dlllib.Font_get_SizeInPoints.restype=c_float
        ret = dlllib.Font_get_SizeInPoints(self.Ptr)
        return ret

    @property

    def Unit(self)->'GraphicsUnit':
        """

        """
        dlllib.Font_get_Unit.argtypes=[c_void_p]
        dlllib.Font_get_Unit.restype=c_int
        ret = dlllib.Font_get_Unit(self.Ptr)
        objwraped = GraphicsUnit(ret)
        return objwraped

    @property
    def Height(self)->int:
        """

        """
        dlllib.Font_get_Height.argtypes=[c_void_p]
        dlllib.Font_get_Height.restype=c_int
        ret = dlllib.Font_get_Height(self.Ptr)
        return ret

#    @staticmethod
#    @dispatch
#
#    def FromLogFont(lf:SpireObject,hdc:'IntPtr')->'Font':
#        """
#
#        """
#        intPtrlf:c_void_p = lf.Ptr
#        intPtrhdc:c_void_p = hdc.Ptr
#
#        dlllib.Font_FromLogFont.argtypes=[ c_void_p,c_void_p]
#        dlllib.Font_FromLogFont.restype=c_void_p
#        intPtr = dlllib.Font_FromLogFont( intPtrlf,intPtrhdc)
#        ret = None if intPtr==None else Font(intPtr)
#        return ret
#


    @staticmethod
    @dispatch

    def FromLogFont(lf:SpireObject)->'Font':
        """

        """
        intPtrlf:c_void_p = lf.Ptr

        dlllib.Font_FromLogFontL.argtypes=[ c_void_p]
        dlllib.Font_FromLogFontL.restype=c_void_p
        intPtr = dlllib.Font_FromLogFontL( intPtrlf)
        ret = None if intPtr==None else Font(intPtr)
        return ret


#    @staticmethod
#
#    def FromHdc(hdc:'IntPtr')->'Font':
#        """
#
#        """
#        intPtrhdc:c_void_p = hdc.Ptr
#
#        dlllib.Font_FromHdc.argtypes=[ c_void_p]
#        dlllib.Font_FromHdc.restype=c_void_p
#        intPtr = dlllib.Font_FromHdc( intPtrhdc)
#        ret = None if intPtr==None else Font(intPtr)
#        return ret
#



    def Clone(self)->'SpireObject':
        """

        """
        dlllib.Font_Clone.argtypes=[c_void_p]
        dlllib.Font_Clone.restype=c_void_p
        intPtr = dlllib.Font_Clone(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    def Dispose(self):
        """

        """
        dlllib.Font_Dispose.argtypes=[c_void_p]
        dlllib.Font_Dispose(self.Ptr)

    def GetHashCode(self)->int:
        """

        """
        dlllib.Font_GetHashCode.argtypes=[c_void_p]
        dlllib.Font_GetHashCode.restype=c_int
        ret = dlllib.Font_GetHashCode(self.Ptr)
        return ret

    @property
    def Bold(self)->bool:
        """

        """
        dlllib.Font_get_Bold.argtypes=[c_void_p]
        dlllib.Font_get_Bold.restype=c_bool
        ret = dlllib.Font_get_Bold(self.Ptr)
        return ret

    @property

    def Name(self)->str:
        """

        """
        dlllib.Font_get_Name.argtypes=[c_void_p]
        dlllib.Font_get_Name.restype=c_void_p
        ret = PtrToStr(dlllib.Font_get_Name(self.Ptr))
        return ret


    @property
    def Strikeout(self)->bool:
        """

        """
        dlllib.Font_get_Strikeout.argtypes=[c_void_p]
        dlllib.Font_get_Strikeout.restype=c_bool
        ret = dlllib.Font_get_Strikeout(self.Ptr)
        return ret

    @property
    def Underline(self)->bool:
        """

        """
        dlllib.Font_get_Underline.argtypes=[c_void_p]
        dlllib.Font_get_Underline.restype=c_bool
        ret = dlllib.Font_get_Underline(self.Ptr)
        return ret


    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Font_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Font_Equals.restype=c_bool
        ret = dlllib.Font_Equals(self.Ptr, intPtrobj)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.Font_ToString.argtypes=[c_void_p]
        dlllib.Font_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Font_ToString(self.Ptr))
        return ret


#    @dispatch
#
#    def GetHeight(self ,graphics:'Graphics')->float:
#        """
#
#        """
#        intPtrgraphics:c_void_p = graphics.Ptr
#
#        dlllib.Font_GetHeight.argtypes=[c_void_p ,c_void_p]
#        dlllib.Font_GetHeight.restype=c_float
#        ret = dlllib.Font_GetHeight(self.Ptr, intPtrgraphics)
#        return ret


    @dispatch
    def GetHeight(self)->float:
        """

        """
        dlllib.Font_GetHeight1.argtypes=[c_void_p]
        dlllib.Font_GetHeight1.restype=c_float
        ret = dlllib.Font_GetHeight1(self.Ptr)
        return ret

    @dispatch

    def GetHeight(self ,dpi:float)->float:
        """

        """
        
        dlllib.Font_GetHeightD.argtypes=[c_void_p ,c_float]
        dlllib.Font_GetHeightD.restype=c_float
        ret = dlllib.Font_GetHeightD(self.Ptr, dpi)
        return ret

    @property
    def IsSystemFont(self)->bool:
        """

        """
        dlllib.Font_get_IsSystemFont.argtypes=[c_void_p]
        dlllib.Font_get_IsSystemFont.restype=c_bool
        ret = dlllib.Font_get_IsSystemFont(self.Ptr)
        return ret

    @property

    def SystemFontName(self)->str:
        """

        """
        dlllib.Font_get_SystemFontName.argtypes=[c_void_p]
        dlllib.Font_get_SystemFontName.restype=c_void_p
        ret = PtrToStr(dlllib.Font_get_SystemFontName(self.Ptr))
        return ret


