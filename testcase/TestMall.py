from utils.RequestUtil import Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil


def test_01():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddMonitorIndexFormula"
    data = {"inputs":"{IndexFormulaList:[{OprationType:0,ID:null,'SystemId':1,FormulaName:'配电自动化(1)1设备1：越下限',AnalyzeType:5,SourceName:'',SourceID:1,IndexType:'405',IndexFormula:'YC_20002000=10',FormulaParm:0,IsExeute:1,isPushEAM:0,BounceTime:15,ClassType:0,Ext:'{\"StartTime\":\"00:00:00\",\"EndTime\":\"23:59:59\",\"EndDate\":\"same\"}',Description:'测试告警',UpdateTime:'2020-12-31 10:24:51'}]}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8","Accept-Language":"zh-CN,zh;q=0.9"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'list': [{'DeviceId': 1, 'TableNum': 18, 'SampleId': 20002000}]")
    print(body)


def test_02():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddMonitorIndexFormula"
    data = {"Inputs":"{IndexFormulaList:[{OprationType:0,ID:null,SystemId:1,FormulaName:'配电自动化告警联动',AnalyzeType:6,SourceName:'',SourceID:1,IndexType:302,IndexFormula:'(YC_20004000+1)=10',FormulaParm:0,IsExeute:1,isPushEAM:null,BounceTime:null,ClassType:null,Ext:'',Description:'',UpdateTime:'2020-12-17 18:47:17'}]}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8","Accept-Language":"zh-CN,zh;q=0.9"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "")
    print(body)


def test_03():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/admin/action.ashx?prefix=admin&action=AddMonitorIndexFormula"
    data = {"Inputs":"{IndexFormulaList:[{OprationType:0,ID:null,SystemId:1,FormulaName:'配电自动化系统联动',AnalyzeType:6,SourceName:'',SourceID:1,IndexType:301,IndexFormula:'YC_20002000=30',FormulaParm:0,IsExeute:1,isPushEAM:null,BounceTime:null,ClassType:null,Ext:'',Description:'',UpdateTime:'2020-12-17 18:47:17'}]}"}
    headers = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8","Accept-Language":"zh-CN,zh;q=0.9"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    # AssertUtil().assert_in_body(body, "'IndexName': '告警联动', 'IndexFormula': '(YC_20004000+1)'")
    print(body)


def test_04():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetIndexPageConfChart"
    data = {"Inputs":"{SystemId:1,SystemName:'配电自动化',AnalyzeType:2,AnalyzeTypeName:'设备指标类',IndexType:1,IndexTypeName:'总供冷量(kW)',SourceList:[{devType:'CODE1-13',devTypeName:'智能照明3'}],StartTime:'2021-01-12',EndTime:'2021-01-12',TimeGranule:0,DataType:0,RatioType:0}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'RowUnit': {'RowUnitList': {'对象CODE1-13': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}}")
    print(body)


def test_05():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=GetIndexPageConfChart"
    data ={"Inputs":"{SystemId:1,SystemName:'配电自动化',AnalyzeType:2,AnalyzeTypeName:'设备指标类',IndexType:1,IndexTypeName:'总供冷量(kW)',SourceList:[{devType:'CODE1-13',devTypeName:'智能照明3'}],StartTime:'2021-01-12',EndTime:'2021-01-12',TimeGranule:0,DataType:0,RatioType:0}"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    requests = Request()
    r = requests.post(url, data=data, headers=headers)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'RowUnit': {'RowUnitList': {'对象CODE1-13': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}}")
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







if __name__ == "__main__":
    # test_01()
    # test_02()
    # test_03()
    test_05()


