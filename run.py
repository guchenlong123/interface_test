import os
import pytest
from common import Base
from config import Conf
from common.Base import init_db

if __name__ == '__main__':

    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["-s", "--alluredir", report_path])

    # 执行SQL还原数据
    conn = init_db("db_1")
    conn.execute("truncate table TB_IMS_REPORTFORMS ")
    conn.execute("truncate table TB_IMS_FORMULA")

    # Base.allure_report(report_path, report_html_path)
    # Base.SendEmail()


