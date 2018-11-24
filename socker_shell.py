from multiprocessing import Process
import socket
import re
import subprocess

paths = './templates'  #    创建一个路径


def server_socket(new_socket):
    data = new_socket.recv(1024)    #   接收套接字信息
    data_info = str(data, 'utf-8')

    re_info = re.match(r'\w* (/[^ ]*)', data_info).group(1)
    print(re_info)

    if re_info == '/':
        re_info = '/index.html'

    error_info = '你访问的页面不存在，错误代码404'

    if 'py' in re_info:
        re_obj = re.match(r'\w* (/([^ ]*))', data_info).group(2)
        new_re_obj = 'python ' + re_obj

        obj = subprocess.Popen(new_re_obj, shell=True, stdout=subprocess.PIPE)
        info = obj.stdout.read()
        if not info:
            Response_header = 'GET HTTP/1.1 404 error\r\n'
            Response_info = error_info
        else:
            Response_header = 'GET HTTP/1.1 200 ok\r\n'
            Response_info = str(info, 'utf-8')

        Response_Server = 'Server : Niter\r\n'
        Response = Response_header + Response_Server + '\r\n' + Response_info
        new_socket.send(bytes(Response, 'gbk'))
    else:
        try:
            with open(paths + re_info, 'rb') as file:
                file_name_info = file.read()
            print(file_name_info)
        except:
            print(error_info)
            Response_header = 'GET HTTP/1.1 404 error\r\n'
            Response_info = error_info
        else:
            Response_header = 'GET HTTP/1.1 200 OK\r\n'
            Response_info = file_name_info.decode('utf-8')

        Response_Server = 'Server : Niter\r\n'
        Response = Response_header + Response_Server + '\r\n' + Response_info
        new_socket.send(bytes(Response, 'gbk'))
    new_socket.close()


if __name__ == '__main__':
    server = socket.socket()
    server.bind(("", 9999))
    server.listen(5)

    print('waiting.....')
    while True:
        new_socket, addr = server.accept()
        print(addr)

        p = Process(target=server_socket, args=(new_socket,))
        p.start()
        p.join()
        new_socket.close()
        if not p: break
    server.close()
