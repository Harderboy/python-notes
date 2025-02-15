import telnetlib


def telnetDoSomething(IP, user, passwd, command):
    try:
        # 链接服务器
        telnet = telnetlib.Telnet(IP)
        # 设置调试级别
        telnet.set_debuglevel(2)

        # 读取输入用户名信息
        rt = telnet.read_until("Login username:".encode("utf-8"))
        # 写入用户名
        telnet.write((user + "\r\n").encode("utf-8"))

        # 读取输入密码信息
        rt = telnet.read_until("Login password:".encode("utf-8"))
        # 写入密码
        telnet.write((passwd + "\r\n").encode("utf-8"))

        # 读取验证IP
        rt = telnet.read_until("Domain name:".encode("utf-8"))
        # 写入IP
        telnet.write((IP + "\r\n").encode("utf-8"))

        # 登录成功，写指令
        rt = telnet.read_until(">".encode("utf-8"))
        telnet.write((command + "\r\n").encode("utf-8"))

        # 上面命令执行成功，会继续出现">"
        # 上面命令执行失败，一般不会出现">"
        rt = telnet.read_until(">".encode("utf-8"))

        # 断开连接
        telnet.close()
        return True
    except:
        print("error")
        return False


if __name__ == "__main__":
    IP = ""
    user = ""
    passwd = ""
    command = "tasklist"
    telnetDoSomething(IP, user, passwd, command)