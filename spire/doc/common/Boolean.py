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

class Boolean (SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        dlllib.Boolean_Create.restype = c_void_p
        intPtr = dlllib.Boolean_Create()
        super(String, self).__init__(intPtr)
    @dispatch
    def __init__(self, value:bool):
        dlllib.Boolean_CreateV.argtypes=[ c_bool]
        dlllib.Boolean_CreateV.restype = c_void_p
        intPtr = dlllib.Boolean_CreateV(value)
        super(Boolean, self).__init__(intPtr)

    @property
    def Value(self)->bool:
        """

        """
        dlllib.Boolean_Value.argtypes=[ c_void_p]
        dlllib.Boolean_Value.restype=c_bool
        ret = dlllib.Boolean_Value( self.Ptr)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Boolean_GetHashCode.argtypes=[c_void_p]
        dlllib.Boolean_GetHashCode.restype=c_int
        ret = dlllib.Boolean_GetHashCode(self.Ptr)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Boolean_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Boolean_Equals.restype=c_bool
        ret = dlllib.Boolean_Equals(self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:bool)->bool:
        """

        """
        
        dlllib.Boolean_EqualsO.argtypes=[c_void_p ,c_bool]
        dlllib.Boolean_EqualsO.restype=c_bool
        ret = dlllib.Boolean_EqualsO(self.Ptr, obj)
        return ret

    @dispatch

    def CompareTo(self ,obj:SpireObject)->int:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Boolean_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Boolean_CompareTo.restype=c_int
        ret = dlllib.Boolean_CompareTo(self.Ptr, intPtrobj)
        return ret

    @dispatch

    def CompareTo(self ,value:bool)->int:
        """

        """
        
        dlllib.Boolean_CompareToV.argtypes=[c_void_p ,c_bool]
        dlllib.Boolean_CompareToV.restype=c_int
        ret = dlllib.Boolean_CompareToV(self.Ptr, value)
        return ret

    @staticmethod

    def Parse(value:str)->bool:
        """

        """
        
        dlllib.Boolean_Parse.argtypes=[ c_void_p]
        dlllib.Boolean_Parse.restype=c_bool
        ret = dlllib.Boolean_Parse( value)
        return ret

#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Boolean_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Boolean_GetTypeCode.restype=c_int
#        ret = dlllib.Boolean_GetTypeCode(self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Boolean_ToString.argtypes=[c_void_p]
        dlllib.Boolean_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.Boolean_ToString(self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Boolean_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Boolean_ToStringP.restype=c_wchar_p
#        ret = dlllib.Boolean_ToStringP(self.Ptr, intPtrprovider)
#        return ret
#


#    @staticmethod
#
#    def TryParse(value:str,result:'Boolean&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Boolean_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Boolean_TryParse.restype=c_bool
#        ret = dlllib.Boolean_TryParse( value,intPtrresult)
#        return ret


    @staticmethod

    def TrueString()->str:
        """

        """
        #dlllib.Boolean_TrueString.argtypes=[]
        dlllib.Boolean_TrueString.restype=c_void_p
        ret = PtrToStr(dlllib.Boolean_TrueString())
        return ret


    @staticmethod

    def FalseString()->str:
        """

        """
        #dlllib.Boolean_FalseString.argtypes=[]
        dlllib.Boolean_FalseString.restype=c_void_p
        ret = PtrToStr(dlllib.Boolean_FalseString())
        return ret


