#encoding:utf-8

class RfidError(Exception):
    code = 0
    code_name = 'Rfid Runtime Error'
    message = 'Runtime Rfid error occurred.'
#    status = HTTP_BAD_REQUEST

    def __init__(self, message=None, code=None, code_name=None, *args, **kwargs):
        super(RfidError, self).__init__(*args, **kwargs)
        if message:
            self.message = message
        if code is not None:
            self.code = code
        if code_name is not None:
            self.code_name = code_name

    def to_dict(self, *args, **kwargs):
        result = {
            'err_code': self.code,
            'err_name': self.code_name,
            'message': self.message
        }
#        logging.info("Return Error:{0}".format(result))
        return result


# 射频卡反馈错误401xx
class ErrorDataShort(RfidError):
    """
    数据长度过短
    """
    code = 40101
    code_name = 'Data_Too_Short'
    message = 'data to short.'

class ErrorDataLong(RfidError):
    """
    数据长度过长
    """
    code = 40102
    code_name = 'Data_Too_Long'
    message = 'data to long.'


class ErrorWriteNotFind(RfidError):
    """
    写数据失败，找不到卡，或者卡损坏
    """
    code = 40103
    code_name = 'Write_Not_Found_Error'
    message = 'Can not find your card or your card is damaged to write.'


class ErrorWriteFailedUnkown(RfidError):
    """
    写入数据失败时的未知错误
    """
    code = 40104
    code_name = 'Write_Other_Error'
    message = 'Write Error except unknown.'


class ErrorReadNotFind(RfidError):
    """
    读数据失败，找不到卡，或者卡损坏
    """
    code = 40105
    code_name = 'Read_Not_Found_Error'
    message = 'Can not find your card or your card is damaged to read.'


class ErrorReadFailedUnknow(RfidError):
    """
    读入数据失败时的未知错误
    """
    code = 40106
    code_name = 'Read_Other_Error'
    message = 'Read Error except unknown.'


class ErrorScanCardFailed(RfidError):
    """
    未扫描到卡
    """
    code = 40107
    code_name = 'San_Card_Failed'
    message = 'scan card failed.'


class ErrorChangeDataErr(RfidError):
    """
    转换数据格式失败
    """
    code = 40108
    code_name = 'Change_Data_Failed'
    message = 'change data failed.'


class ErrorEvaluteErr(RfidError):
    """
    赋值数据失败
    """
    code = 40109
    code_name = 'Evalute_Data_Err'
    message = 'evalute data Err.'


class ErrorAuthenticationErr(RfidError):
    """
    赋值数据失败
    """
    code = 40110
    code_name = 'Authentication_Err'
    message = 'Authentication Err.'


class ErrorzhcnErr(RfidError):
    """
    返回值为中文
    """
    code = 40111
    code_name = 'zh-cn_Err'
    message = 'zh-cn Err.'
