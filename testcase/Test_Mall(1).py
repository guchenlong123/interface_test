from utils.RequestUtil import Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil


def test_01():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=GetMonitorIndexFormulaList"
    data = {"Inputs":"{FormulaName:\"\",PageSize:10,PageCurrent:1,AnalyzeType:6}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'ClassType': 0, 'Ext': '', 'ID': 3, 'SystemId': 1")
    print(body)


def test_02():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=GetFormulaStation"
    data = {"Inputs":"{PrimaryDeviceNo:\"\",SearchInfo:\"\"}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'StationList': [{'StationId': 0, 'StationName': '管理机厂站'}, "
                                      "{'StationId': 1, 'StationName': '前置厂站1'}]")
    print(body)


def test_03():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddMonitorIndexFormula"
    data = {"Inputs":"{IndexFormulaList:[{OprationType:0,ID:null,SystemId:1,FormulaName:\"配电自动化系统联动5\","
                     "AnalyzeType:6,SourceName:\"\",SourceID:1,IndexType:301,IndexFormula:\"YC_20002000=0\","
                     "FormulaParm:0,IsExeute:1,isPushEAM:null,BounceTime:null,ClassType:null,Ext:\"\",Description:\"\","
                     "UpdateTime:\"2020-12-17 18:47:17\"}]}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'IsSucess': True")
    print(body)

def test_04():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=DeleteMonitorIndexFormula"
    data = {"Inputs":"{IndexFormulaList:[{OprationType:2,ID:19,SystemId:null,FormulaName:null,"
                     "AnalyzeType:null,SourceID:0,IndexType:null,IndexFormula:null,FormulaParm:null,"
                     "IsExeute:1,Description:null}]}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'ExceptionMeg': '删除成功！")
    print(body)


def test_05():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=InsertGateway"
    data = {"Inputs":"{Cname:\"网关5\",Ipaddress:\"192.168.40.95\",Portno:80,Description:111}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Success': True, 'ExceptionMsg': '新增成功！'")
    print(body)


def test_06():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=DeleteGateway"
    data = {"Inputs":"{Id:5}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Success': True, 'ExceptionMsg': '删除成功！'")
    print(body)


def test_07():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/admin/action.ashx?prefix=admin&action=ser-GetDataRange"
    data = {"Inputs":"{ProjectID:1,StationID:1,DeviceID:1,RangeID:18}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "<record label='模拟量点1' tabelID='18' recordID='20002000'/>")
    print(body)


def test_08():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddGroupAddrInfo"
    data = {"Inputs":"[{Id:5,OperaType:\"add\",GateWay:1,AddressType:0,RWRight:0,DataType:1,"
                     "Address:\"1/0/4\",Cname:\"组地址3\",dataSource:{BaseNo:1,PrjID:1,StationID:1,"
                     "DeviceID:1,TableNo:18,FieldNo:10,RecordNo:20002000}}]"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Success': True, 'ExceptionMsg': '操作成功!请重启服务'")
    print(body)

import json
def test_09():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=InsertCamera"
    data = {"Inputs":"{Id:0,Cname:01,Type:0,Description:\"\",Channelnum:0,Limkmode:0,"
                     "Multicastip:\"0.0.0.0\",Ips:[{Code:003,CameraId:0,IP:\"192.168.10.70\",Port:80},"
                     "{Code:004,CameraId:0,IP:\"192.168.10.70\",Port:7000}],"
                     "Username:\"admin\",Password:12345,Videolevel:0,Reserved:\"\",Campus:\"\"}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    data1 = {"inputs":"{Id:0,Cname:01,Type:0,Description:\"\",Channelnum:0,Limkmode:0,Multicastip:\"0.0.0.0\","
                      "Ips:[{Code:\"003\",CameraId:0,IP:\"192.168.10.70\",Port:\"80\"},"
                      "{Code:\"004\",CameraId:0,IP:\"192.168.10.70\",Port:\"7000\"}],"
                      "Username:\"admin\",Password:12345,Videolevel:0,Reserved:\"\",Campus:\"\"}"}
    requests = Request()
    r = requests.post(url, data=data1, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Success': False, 'ExceptionMsg': '摄像头IP出现重复，请重设！'")
    print(body)


def test_10():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=UpdateCamera"
    data = {"inputs":"{Id:15,Cname:\"测试用\",Type:0,Description:\"\",Channelnum:0,Limkmode:0,"
                     "Multicastip:\"0.0.0.0\",Ips:[{Code:\"003\",CameraId:0,IP:\"192.168.10.70\",Port:\"80\"},"
                     "{Code:\"004\",CameraId:15,IP:\"192.168.10.70\",Port:\"7000\"}],"
                     "Username:\"admin\",Password:12345,Videolevel:0,Reserved:\"\",Campus:1001}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "")
    print(body)


"""新增联动场景"""
def test_11():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddLinkageConfig"
    data1 = {"Inputs":"{ID:14,CTime:'2020-12-25T06:01:41.905Z',FORMULAID:3,CName:'测试用',"
                      "DURATIONTIME:15,LinkageEffect:1,IsStart:0,"
                      "LinkageControlItemList:[{ID:15,LinkcontolGroupId:14,"
                      "ControlItem:'{LINKAGEACTIONTYPE:\"CALLAPI\",VALUE:\"1\",TRYTIMES:\"1\","
                      "CALLAPI:{IP:\"192.168.40.180\",APITYPE:\"HK\",PORT:\"8000\",USER:\"admin\","
                      "PASSWORD:\"12345\",CHANNEL:\"1\",CALLBACKCAMERAID:\"3\",CALLBACKCAMERANAME:\"海康2号\"}}'}],"
                      "Ext:'{\"StartTime\":\"00:00:00\",\"EndTime\":\"23:59:59\",\"EndDate\":\"same\"}'}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8","Accept-Language":"zh-CN,zh;q=0.9"}
    requests = Request()
    r = requests.post(url, data=data1, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'ExceptionMeg': '保存成功!'")
    print(body)


def test_12():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=GetMonitorIndexFormulaList"
    data = {"Inputs":"{FormulaName:'@@@',PageSize:10,PageCurrent:1,AnalyzeType:2}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Page': {'Current': 1, 'Total': 0}")
    print(body)


def test_13():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=UpdateLinkageConfig"
    data = {"Inputs":"{ID:14,CTime:'2020-12-25T06:01:41.905Z',FORMULAID:3,CName:'测试用',DURATIONTIME:15,"
                     "LinkageEffect:1,IsStart:0,LinkageControlItemList:[{ID:15,LinkcontolGroupId:14,"
                     "ControlItem:'{LINKAGEACTIONTYPE:\"CALLAPI\",VALUE:\"1\",TRYTIMES:\"1\",CALLAPI:{IP:\"192.168.40.180\","
                     "APITYPE:\"HK\",PORT:\"8000\",USER:\"admin\",PASSWORD:\"12345\",CHANNEL:\"1\",CALLBACKCAMERAID:\"3\","
                     "CALLBACKCAMERANAME:\"海康2号\"}}'}],Ext:'{\"StartTime\":\"00:00:00\",\"EndTime\":\"23:59:59\","
                     "\"EndDate\":\"same\"}'}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8","Accept-Language":"zh-CN,zh;q=0.9"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'ID': 14, 'CName': '测试用', 'LinkageEffective': 1, 'FormulaID': 3, 'FormulaName': '配电自动化系统联动'")
    print(body)


def test_14():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddMonitorIndexFormula"
    data = {"inputs":"{IndexFormulaList:[{OprationType:0,ID:null,'SystemId':1,FormulaName:'配电自动化(1)1设备1：越下限',"
                     "AnalyzeType:5,SourceName:'',SourceID:1,IndexType:'405',IndexFormula:'YC_20002000=10',"
                     "FormulaParm:0,IsExeute:1,isPushEAM:0,BounceTime:15,ClassType:0,"
                     "Ext:'{\"StartTime\":\"00:00:00\",\"EndTime\":\"23:59:59\",\"EndDate\":\"same\"}',Description:'测试告警',"
                     "UpdateTime:'2020-12-31 10:24:51'}]}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8","Accept-Language":"zh-CN,zh;q=0.9"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'IsSucess': True")
    print(body)


def test_15():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=GetLimit"
    data = {"inputs":"{PageCurrent:1,PageSize:20,strName:'@@@'}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'strDataSource': '[我的工程.前置厂站1.模拟量表.VALUE]模拟量点1'")
    print(body)


if __name__ == "__main__":
    test_15()





