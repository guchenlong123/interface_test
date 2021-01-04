from config.Conf import ConfigYaml
from config import Conf
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestUtil import Request
import json
import pytest
from utils.AssertUtil import AssertUtil
import allure
from common import Base


# 1、初始化信息
# 1）.初始化测试用例文件
case_file = os.path.join("../data", ConfigYaml().get_excel_file())

# 2）.测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()

# 3）.获取运行测试用例列表
data_init = Data(case_file,sheet_name)
run_list = data_init.get_run_data()

# 4）.日志
log = my_log()
# 2、测试用例方法，参数化运行


class TestExcel:
# 1）.初始化信息，url,data
    # 1、增加pyest
    @pytest.mark.parametrize("case", run_list)
    # 2、修改方法参数
    def test_run(self,case):
        # 3、重构函数内容
        data_key = ExcelConfig.DataConfig
        # run_list第1个用例，用例key获取values
        url = ConfigYaml().get_conf_url() + case[data_key.url]
        print(url)
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        status_code = case[data_key.status_code]
        db_verify = case[data_key.db_verify]

        # 2）.接口请求
        request = Request()
        # params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        # headers 转义json
        # 验证headers有没有内容
        if len(str(headers).strip()) is not 0:
            headers = json.loads(headers)
        # cookies 转义json
        # 验证cookies有没有内容
        if len(str(cookies).strip()) is not 0:
            cookies = json.loads(cookies)

        # method post/get
        if str(method).lower() == "get":
            res = request.get(url, data=params, headers=headers, cookies=cookies)

        elif str(method).lower() == "post":
            res = request.post(url, data=params, headers=headers, cookies=cookies)

        else:
            res = log.error("错误请求method: %s" % method)
        print(res)

        # allure
        # sheet名称  feature 一级标签
        allure.dynamic.feature(sheet_name)
        # 模块   story 二级标签
        allure.dynamic.story(case_model)
        # 用例ID+接口名称  title
        allure.dynamic.title(case_id + case_name)
        # 请求URL  请求类型 期望结果 实际结果描述
        desc = "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
               "<font color='red'>期望结果: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(url, method, expect_result, res)
        allure.dynamic.description(desc)

        # 断言验证
        # 状态码，返回结果内容，数据库相关的结果的验证
        # 状态码
        assert_util = AssertUtil()
        assert_util.assert_code(res["code"], status_code)

        # 返回结果内容
        assert_util.assert_in_body(str(res["body"]), str(expect_result))


if __name__ == '__main__':
    # pass
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "Test_excel_case.py", "--alluredir", report_path])

    # Base.allure_report(report_path, report_html_path)
    # Base.send_mail(title="ims自动化测试报告结果",content=report_html_path)

