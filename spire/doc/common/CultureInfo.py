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

class CultureInfo (SpireObject) :
    """

    """
    @staticmethod

    def CreateSpecificCulture(name:str)->'CultureInfo':
        """

        """
        
        dlllib.CultureInfo_CreateSpecificCulture.argtypes=[ c_void_p]
        dlllib.CultureInfo_CreateSpecificCulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_CreateSpecificCulture( name)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod

    def get_CurrentCulture()->'CultureInfo':
        """

        """
        #dlllib.CultureInfo_get_CurrentCulture.argtypes=[]
        dlllib.CultureInfo_get_CurrentCulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_CurrentCulture()
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod
    def set_CurrentCulture( value:'CultureInfo'):
        dlllib.CultureInfo_set_CurrentCulture.argtypes=[ c_void_p]
        dlllib.CultureInfo_set_CurrentCulture( value.Ptr)

    @staticmethod

    def get_CurrentUICulture()->'CultureInfo':
        """

        """
        #dlllib.CultureInfo_get_CurrentUICulture.argtypes=[]
        dlllib.CultureInfo_get_CurrentUICulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_CurrentUICulture()
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod
    def set_CurrentUICulture( value:'CultureInfo'):
        dlllib.CultureInfo_set_CurrentUICulture.argtypes=[ c_void_p]
        dlllib.CultureInfo_set_CurrentUICulture( value.Ptr)

    @staticmethod

    def get_InstalledUICulture()->'CultureInfo':
        """

        """
        #dlllib.CultureInfo_get_InstalledUICulture.argtypes=[]
        dlllib.CultureInfo_get_InstalledUICulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_InstalledUICulture()
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod

    def get_DefaultThreadCurrentCulture()->'CultureInfo':
        """

        """
        #dlllib.CultureInfo_get_DefaultThreadCurrentCulture.argtypes=[]
        dlllib.CultureInfo_get_DefaultThreadCurrentCulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_DefaultThreadCurrentCulture()
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod
    def set_DefaultThreadCurrentCulture( value:'CultureInfo'):
        dlllib.CultureInfo_set_DefaultThreadCurrentCulture.argtypes=[ c_void_p]
        dlllib.CultureInfo_set_DefaultThreadCurrentCulture( value.Ptr)

    @staticmethod

    def get_DefaultThreadCurrentUICulture()->'CultureInfo':
        """

        """
        #dlllib.CultureInfo_get_DefaultThreadCurrentUICulture.argtypes=[]
        dlllib.CultureInfo_get_DefaultThreadCurrentUICulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_DefaultThreadCurrentUICulture()
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod
    def set_DefaultThreadCurrentUICulture( value:'CultureInfo'):
        dlllib.CultureInfo_set_DefaultThreadCurrentUICulture.argtypes=[ c_void_p]
        dlllib.CultureInfo_set_DefaultThreadCurrentUICulture( value.Ptr)

    @staticmethod

    def get_InvariantCulture()->'CultureInfo':
        """

        """
        #dlllib.CultureInfo_get_InvariantCulture.argtypes=[]
        dlllib.CultureInfo_get_InvariantCulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_InvariantCulture()
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @property

    def Parent(self)->'CultureInfo':
        """

        """
        dlllib.CultureInfo_get_Parent.argtypes=[c_void_p]
        dlllib.CultureInfo_get_Parent.restype=c_void_p
        intPtr = dlllib.CultureInfo_get_Parent(self.Ptr)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @property
    def LCID(self)->int:
        """

        """
        dlllib.CultureInfo_get_LCID.argtypes=[c_void_p]
        dlllib.CultureInfo_get_LCID.restype=c_int
        ret = dlllib.CultureInfo_get_LCID(self.Ptr)
        return ret

    @property
    def KeyboardLayoutId(self)->int:
        """

        """
        dlllib.CultureInfo_get_KeyboardLayoutId.argtypes=[c_void_p]
        dlllib.CultureInfo_get_KeyboardLayoutId.restype=c_int
        ret = dlllib.CultureInfo_get_KeyboardLayoutId(self.Ptr)
        return ret

#    @staticmethod
#
#    def GetCultures(types:'CultureTypes')->List['CultureInfo']:
#        """
#
#        """
#        enumtypes:c_int = types.value
#
#        dlllib.CultureInfo_GetCultures.argtypes=[ c_int]
#        dlllib.CultureInfo_GetCultures.restype=IntPtrArray
#        intPtrArray = dlllib.CultureInfo_GetCultures( enumtypes)
#        ret = GetObjVectorFromArray(intPtrArray, CultureInfo)
#        return ret


    @property

    def Name(self)->str:
        """

        """
        dlllib.CultureInfo_get_Name.argtypes=[c_void_p]
        dlllib.CultureInfo_get_Name.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_Name(self.Ptr))
        return ret


    @property

    def DisplayName(self)->str:
        """

        """
        dlllib.CultureInfo_get_DisplayName.argtypes=[c_void_p]
        dlllib.CultureInfo_get_DisplayName.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_DisplayName(self.Ptr))
        return ret


    @property

    def NativeName(self)->str:
        """

        """
        dlllib.CultureInfo_get_NativeName.argtypes=[c_void_p]
        dlllib.CultureInfo_get_NativeName.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_NativeName(self.Ptr))
        return ret


    @property

    def EnglishName(self)->str:
        """

        """
        dlllib.CultureInfo_get_EnglishName.argtypes=[c_void_p]
        dlllib.CultureInfo_get_EnglishName.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_EnglishName(self.Ptr))
        return ret


    @property

    def TwoLetterISOLanguageName(self)->str:
        """

        """
        dlllib.CultureInfo_get_TwoLetterISOLanguageName.argtypes=[c_void_p]
        dlllib.CultureInfo_get_TwoLetterISOLanguageName.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_TwoLetterISOLanguageName(self.Ptr))
        return ret


    @property

    def ThreeLetterISOLanguageName(self)->str:
        """

        """
        dlllib.CultureInfo_get_ThreeLetterISOLanguageName.argtypes=[c_void_p]
        dlllib.CultureInfo_get_ThreeLetterISOLanguageName.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_ThreeLetterISOLanguageName(self.Ptr))
        return ret


    @property

    def ThreeLetterWindowsLanguageName(self)->str:
        """

        """
        dlllib.CultureInfo_get_ThreeLetterWindowsLanguageName.argtypes=[c_void_p]
        dlllib.CultureInfo_get_ThreeLetterWindowsLanguageName.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_ThreeLetterWindowsLanguageName(self.Ptr))
        return ret


#    @property
#
#    def CompareInfo(self)->'CompareInfo':
#        """
#
#        """
#        dlllib.CultureInfo_get_CompareInfo.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_CompareInfo.restype=c_void_p
#        intPtr = dlllib.CultureInfo_get_CompareInfo(self.Ptr)
#        ret = None if intPtr==None else CompareInfo(intPtr)
#        return ret
#


#    @property
#
#    def TextInfo(self)->'TextInfo':
#        """
#
#        """
#        dlllib.CultureInfo_get_TextInfo.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_TextInfo.restype=c_void_p
#        intPtr = dlllib.CultureInfo_get_TextInfo(self.Ptr)
#        ret = None if intPtr==None else TextInfo(intPtr)
#        return ret
#



    def Equals(self ,value:'SpireObject')->bool:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.CultureInfo_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.CultureInfo_Equals.restype=c_bool
        ret = dlllib.CultureInfo_Equals(self.Ptr, intPtrvalue)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.CultureInfo_GetHashCode.argtypes=[c_void_p]
        dlllib.CultureInfo_GetHashCode.restype=c_int
        ret = dlllib.CultureInfo_GetHashCode(self.Ptr)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.CultureInfo_ToString.argtypes=[c_void_p]
        dlllib.CultureInfo_ToString.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_ToString(self.Ptr))
        return ret


#
#    def GetFormat(self ,formatType:'Type')->'SpireObject':
#        """
#
#        """
#        intPtrformatType:c_void_p = formatType.Ptr
#
#        dlllib.CultureInfo_GetFormat.argtypes=[c_void_p ,c_void_p]
#        dlllib.CultureInfo_GetFormat.restype=c_void_p
#        intPtr = dlllib.CultureInfo_GetFormat(self.Ptr, intPtrformatType)
#        ret = None if intPtr==None else SpireObject(intPtr)
#        return ret
#


    @property
    def IsNeutralCulture(self)->bool:
        """

        """
        dlllib.CultureInfo_get_IsNeutralCulture.argtypes=[c_void_p]
        dlllib.CultureInfo_get_IsNeutralCulture.restype=c_bool
        ret = dlllib.CultureInfo_get_IsNeutralCulture(self.Ptr)
        return ret

#    @property
#
#    def CultureTypes(self)->'CultureTypes':
#        """
#
#        """
#        dlllib.CultureInfo_get_CultureTypes.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_CultureTypes.restype=c_int
#        ret = dlllib.CultureInfo_get_CultureTypes(self.Ptr)
#        objwraped = CultureTypes(ret)
#        return objwraped


#    @property
#
#    def NumberFormat(self)->'NumberFormatInfo':
#        """
#
#        """
#        dlllib.CultureInfo_get_NumberFormat.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_NumberFormat.restype=c_void_p
#        intPtr = dlllib.CultureInfo_get_NumberFormat(self.Ptr)
#        ret = None if intPtr==None else NumberFormatInfo(intPtr)
#        return ret
#


#    @NumberFormat.setter
#    def NumberFormat(self, value:'NumberFormatInfo'):
#        dlllib.CultureInfo_set_NumberFormat.argtypes=[c_void_p, c_void_p]
#        dlllib.CultureInfo_set_NumberFormat(self.Ptr, value.Ptr)


#    @property
#
#    def DateTimeFormat(self)->'DateTimeFormatInfo':
#        """
#
#        """
#        dlllib.CultureInfo_get_DateTimeFormat.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_DateTimeFormat.restype=c_void_p
#        intPtr = dlllib.CultureInfo_get_DateTimeFormat(self.Ptr)
#        ret = None if intPtr==None else DateTimeFormatInfo(intPtr)
#        return ret
#


#    @DateTimeFormat.setter
#    def DateTimeFormat(self, value:'DateTimeFormatInfo'):
#        dlllib.CultureInfo_set_DateTimeFormat.argtypes=[c_void_p, c_void_p]
#        dlllib.CultureInfo_set_DateTimeFormat(self.Ptr, value.Ptr)


    def ClearCachedData(self):
        """

        """
        dlllib.CultureInfo_ClearCachedData.argtypes=[c_void_p]
        dlllib.CultureInfo_ClearCachedData(self.Ptr)

#    @property
#
#    def Calendar(self)->'Calendar':
#        """
#
#        """
#        dlllib.CultureInfo_get_Calendar.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_Calendar.restype=c_void_p
#        intPtr = dlllib.CultureInfo_get_Calendar(self.Ptr)
#        ret = None if intPtr==None else Calendar(intPtr)
#        return ret
#


#    @property
#
#    def OptionalCalendars(self)->List['Calendar']:
#        """
#
#        """
#        dlllib.CultureInfo_get_OptionalCalendars.argtypes=[c_void_p]
#        dlllib.CultureInfo_get_OptionalCalendars.restype=IntPtrArray
#        intPtrArray = dlllib.CultureInfo_get_OptionalCalendars(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Calendar)
#        return ret


    @property
    def UseUserOverride(self)->bool:
        """

        """
        dlllib.CultureInfo_get_UseUserOverride.argtypes=[c_void_p]
        dlllib.CultureInfo_get_UseUserOverride.restype=c_bool
        ret = dlllib.CultureInfo_get_UseUserOverride(self.Ptr)
        return ret


    def GetConsoleFallbackUICulture(self)->'CultureInfo':
        """

        """
        dlllib.CultureInfo_GetConsoleFallbackUICulture.argtypes=[c_void_p]
        dlllib.CultureInfo_GetConsoleFallbackUICulture.restype=c_void_p
        intPtr = dlllib.CultureInfo_GetConsoleFallbackUICulture(self.Ptr)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret



    def Clone(self)->'SpireObject':
        """

        """
        dlllib.CultureInfo_Clone.argtypes=[c_void_p]
        dlllib.CultureInfo_Clone.restype=c_void_p
        intPtr = dlllib.CultureInfo_Clone(self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    @staticmethod

    def ReadOnly(ci:'CultureInfo')->'CultureInfo':
        """

        """
        intPtrci:c_void_p = ci.Ptr

        dlllib.CultureInfo_ReadOnly.argtypes=[ c_void_p]
        dlllib.CultureInfo_ReadOnly.restype=c_void_p
        intPtr = dlllib.CultureInfo_ReadOnly( intPtrci)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @property
    def IsReadOnly(self)->bool:
        """

        """
        dlllib.CultureInfo_get_IsReadOnly.argtypes=[c_void_p]
        dlllib.CultureInfo_get_IsReadOnly.restype=c_bool
        ret = dlllib.CultureInfo_get_IsReadOnly(self.Ptr)
        return ret

    @staticmethod
    @dispatch

    def GetCultureInfo(culture:int)->'CultureInfo':
        """

        """
        
        dlllib.CultureInfo_GetCultureInfo.argtypes=[ c_int]
        dlllib.CultureInfo_GetCultureInfo.restype=c_void_p
        intPtr = dlllib.CultureInfo_GetCultureInfo( culture)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod
    @dispatch

    def GetCultureInfo(name:str)->'CultureInfo':
        """

        """
        
        dlllib.CultureInfo_GetCultureInfoN.argtypes=[ c_void_p]
        dlllib.CultureInfo_GetCultureInfoN.restype=c_void_p
        intPtr = dlllib.CultureInfo_GetCultureInfoN( name)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @staticmethod
    @dispatch

    def GetCultureInfo(name:str,altName:str)->'CultureInfo':
        """

        """
        
        dlllib.CultureInfo_GetCultureInfoNA.argtypes=[ c_void_p,c_void_p]
        dlllib.CultureInfo_GetCultureInfoNA.restype=c_void_p
        intPtr = dlllib.CultureInfo_GetCultureInfoNA( name,altName)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


    @property

    def IetfLanguageTag(self)->str:
        """

        """
        dlllib.CultureInfo_get_IetfLanguageTag.argtypes=[c_void_p]
        dlllib.CultureInfo_get_IetfLanguageTag.restype=c_void_p
        ret = PtrToStr(dlllib.CultureInfo_get_IetfLanguageTag(self.Ptr))
        return ret


    @staticmethod

    def GetCultureInfoByIetfLanguageTag(name:str)->'CultureInfo':
        """

        """
        
        dlllib.CultureInfo_GetCultureInfoByIetfLanguageTag.argtypes=[ c_void_p]
        dlllib.CultureInfo_GetCultureInfoByIetfLanguageTag.restype=c_void_p
        intPtr = dlllib.CultureInfo_GetCultureInfoByIetfLanguageTag( name)
        ret = None if intPtr==None else CultureInfo(intPtr)
        return ret


