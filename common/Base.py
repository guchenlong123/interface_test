import subprocess
from utils.LogUtil import my_log
from utils.EmailUtil import SendEmail
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from utils.MysqlUtil import Mysql
log = my_log()

#1、定义init_db
def init_db(db_alias):
#2、初始数据化信息，通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    name = db_info["db_name"]
#3、初始化myssql对象
    conn = Mysql(host,user,password,name)
    print(conn)
    return conn

def assert_db(db_name,result,db_verify):
    assert_util =  AssertUtil()
    #sql = init_db("db_1")
    sql = init_db(db_name)
    # 2、查询sql，excel定义好的
    db_res = sql.fetchone(db_verify)
    # 3、数据库的结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        #res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)


def allure_report(report_path, report_html):
    """
    生成allure 报告
    :param report_path:
    :param report_html:
    :return:
    """
    # 执行命令 allure generate...
    allure_cmd ="allure generate %s -o %s --clean"%(report_path, report_html)
    # subprocess.call
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败，请检查测试环境相关配置")
        raise


def send_mail(report_html_path="",content="",title=""):
    """
    发送邮件
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()


# if __name__ =="__main":
    # init_db("db_1")


