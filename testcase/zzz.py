from utils.RequestUtil import Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from common.Base import init_db


#  删除报表
def test_01():
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path + "/action.ashx?action=DeleteReportInfo"
    data = {"Inputs": "{ID:1}"}
    requests = Request()
    r = requests.post(url, data=data, headers=None)
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    body = r["body"]
    AssertUtil().assert_in_body(body, "'ErrorCode': 0, 'Success': True, 'ExceptionMsg': '删除成功！'")
    print(body)

    conn = init_db("db_1")
    conn.execute("truncate table TB_IMS_REPORTFORMS")
    # res = conn.execute("select campus_code from ioms_role where rolecode = 'administrators'")
    # print(res)


# if __name__ == "__main__":
#     test_01()

