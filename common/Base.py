import subprocess
from utils.LogUtil import my_log
from utils.EmailUtil import SendEmail
from config.Conf import ConfigYaml
log = my_log()


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