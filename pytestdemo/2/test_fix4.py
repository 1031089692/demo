# coding:utf-8

#addfinalizer终结函数
import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com",587,timeout=5)
    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()
        request.addfinalizer(fin)
        return smtp_connection # provide the fixture value