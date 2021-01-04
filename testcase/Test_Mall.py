from utils.RequestUtil import Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil


def test_01():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetSampleDeviceAndPoint"
    data = {"Inputs":"{CName:\"\",MCode:0,pageCurrent:1,PageSize:10}"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Page': {'Current': 1, 'Total': 150}")
    print(body)


def test_02():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetSampleDeviceAndPoint"
    data = {"Inputs":"{CName:\"1设备1\",MCode:\"M009\",pageCurrent:1,PageSize:10}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'ActionInfo': {'ErrorCode': 0, 'Success': True, 'ExceptionMsg': '', "
                                      "'ExtendContent': None}, 'Page': {'Current': 1, 'Total': 2}")
    print(body)


def test_03():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetSampleDeviceAndPoint"
    data = {"Inputs":"{CName:\"1设备11\",MCode:\"M014\",pageCurrent:1,PageSize:10}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Page': {'Current': 1, 'Total': 1}")
    print(body)


def test_04():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=ExportDeviceHistoryData"
    data = {"Inputs":"{Unit:1,StartTime:\"2020-09-08 00:00\",EndTime:\"2020-09-08 11:09\",MinutesNum:10,"
                     "DeviceList:[{DeviceId:1,DeviceName:\"1设备1：\",NumList:[{SampleType:18,RecordNo:20002000}]}]}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'status': 'success'")
    print(body)


def test_05():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetDeviceRunInfo"
    data = {"Inputs":"{Start_StopState:0,DeviceType:1,DevName:\"@@@@\",strMcode:0,On_Offline:0,"
                     "RunState:0,pageCurrent:1,PageSize:10,CampusInfo:1001}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Page': {'Current': 1, 'Total': 0}, 'SysId': 0, 'SysName': '全系统'")
    print(body)


def test_06():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetDevStateBySysAndName"
    data = {"Inputs":""}
    # headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'Page': {'Current': 1, 'Total': 0}, 'SysId': 0, 'SysName': '全系统'")
    print(body)


def test_07():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?prefix=admin&action=GetDeviceLimit"
    # data = {"Inputs":"{DateType:0,List:[{TableNum:18,Num:0,RecordNo:null,DeviceId:1}]}"}
    # data = {"Inputs":"{DateType:0,List:[{TableNum:18,Num:1,RecordNo:null,DeviceId:1}]}"}
    data ={"Inputs":"{DateType:1,List:[{TableNum:18,Num:null,RecordNo:20002000,DeviceId:1}]}"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'ResLimitList': {'18_20002000': {'UpperLimit': '2', "
                                      "'LowerLimit': '1', 'DeadZoneValue': '0'}}")
    print(body)


def test_08():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetDeviceBySysAndName"
    # data = {"Inputs":"{DateType:0,List:[{TableNum:18,Num:1,RecordNo:null,DeviceId:1}]}"}
    # data = {"Inputs": "{strMcode:\"M009\",strName:\"\",PageCurrent:1,PageSize:10}"}
    data ={"Inputs": "{strMcode:0,strName:\"@@@@\",PageCurrent:1,PageSize:10}"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Page': {'Current': 1, 'Total': 0}, 'list': []")
    print(body)


def test_09():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetHistoryMonitor"
    data = {"Inputs":"{particle:1,Unit:1,QueryType:\"avg\",StartTime:\"2020-09-09 00:00:00\",EndTime:\"2020-09-09 10:51:59\","
                     "DeviceId:1,SampleType:1,NumList:[\"20002000\"]}"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Items': [{'ItemName': '模拟量点1', 'ItemValue': 10.0, 'Unit': 'V'}]")
    print(body)


def test_10():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=ExportSelectedAlarms"
    data = {"Inputs":"{AlarmIds:['e815175d-3051-4d8e-a52e-c97d498bed7e'],PageSize:10,PageIndex:1,AllAlarm:true,CampusIds:1001}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Success': False, 'ExceptionMsg': '登录超时，请重新登录'")
    print(body)


def test_11():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetAlarms"
    data = {"Inputs":"{ObjName:\"模拟量1\",IsAlarmPage:\"alarm\",StartTime:\"2020-09-14 00:00\","
                     "EndTime:\"2020-09-14 17:21\",PageSize:10,CampusIds:1001,PageIndex:1,SrcType:0,Flag:-1}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    Cookie = {"userid":"admin"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers, cookies=Cookie)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'total': 1, 'current': 1, 'Count': 2")
    print(body)


def test_12():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=ExportSelectedAlarms"
    data = {"Inputs":"{AlarmIds:[\"e815175d-3051-4d8e-a52e-c97d498bed7e\"],PageSize:10,PageIndex:1,"
                     "AllAlarm:true,CampusIds:1001}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    Cookie = {"userid":"admin"}
    requests = Request()
    r = requests.post(url, data=data, headers=None, cookies=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'ErrorCode': 0, 'Success': True")
    print(body)


def test_13():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetDevicePDRData"
    data = {"Inputs":"{alarmId:\"e815175d-3051-4d8e-a52e-c97d498bed7e\"}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    Cookie = {"userid":"admin"}
    requests = Request()
    r = requests.post(url, data=data, headers=None, cookies=Cookie)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'Success': False, 'ExceptionMsg': '没有数据', 'ActionName': '获取告警曲线数据'")
    print(body)


def test_14():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetAlarmsByAlarmCount"
    data = {"Inputs":"{StartTime:\"2020-08-15\",EndTime:\"2020-09-14\",CampusInfo:1001,AlarmClass:0,PageIndex:1,"
                     "PageSize:10,AlarmLevel:3,SysId:1}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    Cookie = {"userid":"admin"}
    requests = Request()
    r = requests.post(url, data=data, headers=None, cookies=Cookie)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'Success': True, 'ExceptionMsg': None, 'ActionName': '获取告警统计弹窗数据'")
    print(body)


def test_15():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetAlarmsByAlarmCount"
    data = {"Inputs":"{StartTime:'2020-08-15',EndTime:'2020-09-14',CampusInfo:1001,AlarmClass:0,PageIndex:1,PageSize:10,AlarmLevel:3,SysId:1}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    Cookie = {"userid":"admin"}
    requests = Request()
    r = requests.post(url, data=data, headers=None, cookies=Cookie)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'DeviceName': '设备2', 'AlarmObjName': '模拟量点1', 'AlarmContent': '模拟量1 置数5成功'")
    print(body)





if __name__ == "__main__":
    # test_01()
    # test_02()
    # test_03()
    # test_04()
    # test_05()
    # test_06()
    # test_07()
    # test_08()
    # test_09()
    test_15()
    # test_11()


