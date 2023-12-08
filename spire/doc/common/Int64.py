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

class Int64 (SpireObject) :
    """

    """
    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Int64_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Int64_CompareTo.restype=c_int
        ret = dlllib.Int64_CompareTo(self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:int)->int:
        """

        """
        
        dlllib.Int64_CompareToV.argtypes=[c_void_p ,c_long]
        dlllib.Int64_CompareToV.restype=c_int
        ret = dlllib.Int64_CompareToV(self.Ptr, value)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Int64_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Int64_Equals.restype=c_bool
        ret = dlllib.Int64_Equals(self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:int)->bool:
        """

        """
        
        dlllib.Int64_EqualsO.argtypes=[c_void_p ,c_long]
        dlllib.Int64_EqualsO.restype=c_bool
        ret = dlllib.Int64_EqualsO(self.Ptr, obj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Int64_GetHashCode.argtypes=[c_void_p]
        dlllib.Int64_GetHashCode.restype=c_int
        ret = dlllib.Int64_GetHashCode(self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Int64_ToString.argtypes=[c_void_p]
        dlllib.Int64_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Int64_ToString(self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int64_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Int64_ToStringP.restype=c_wchar_p
#        ret = dlllib.Int64_ToStringP(self.Ptr, intPtrprovider)
#        return ret
#


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.Int64_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.Int64_ToStringF.restype=c_void_p
        ret = PtrToStr(dlllib.Int64_ToStringF(self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int64_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Int64_ToStringFP.restype=c_wchar_p
#        ret = dlllib.Int64_ToStringFP(self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->int:
        """

        """
        
        dlllib.Int64_Parse.argtypes=[ c_void_p]
        dlllib.Int64_Parse.restype=c_long
        ret = dlllib.Int64_Parse( s)
        return ret

#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->int:
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.Int64_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.Int64_ParseSS.restype=c_long
#        ret = dlllib.Int64_ParseSS( s,enumstyle)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->int:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int64_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.Int64_ParseSP.restype=c_long
#        ret = dlllib.Int64_ParseSP( s,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->int:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Int64_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.Int64_ParseSSP.restype=c_long
#        ret = dlllib.Int64_ParseSSP( s,enumstyle,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'Int64&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Int64_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Int64_TryParse.restype=c_bool
#        ret = dlllib.Int64_TryParse( s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'Int64&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Int64_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.Int64_TryParseSSPR.restype=c_bool
#        ret = dlllib.Int64_TryParseSSPR( s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Int64_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Int64_GetTypeCode.restype=c_int
#        ret = dlllib.Int64_GetTypeCode(self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod
    def MaxValue()->int:
        """

        """
        #dlllib.Int64_MaxValue.argtypes=[]
        dlllib.Int64_MaxValue.restype=c_long
        ret = dlllib.Int64_MaxValue()
        return ret

    @staticmethod
    def MinValue()->int:
        """

        """
        #dlllib.Int64_MinValue.argtypes=[]
        dlllib.Int64_MinValue.restype=c_long
        ret = dlllib.Int64_MinValue()
        return ret

