# coding=gbk
# -*- coding:uft-8 -*-
# ����ͼ��

import requests
import warnings
import os


def main():
    url = 'https://jstxcj.91job.org.cn/code/upload'
    headers = {'User-Agent': 'joke'}
    files = {'file': open('code.jpg', 'rb')}
    res = requests.post(url, headers=headers, files=files, verify=False, timeout=(20, 20)).text
    code = res[1: -1]
    print('ɨ��ɹ� >>>')
    print(code)
    print('-' * 30)
    url = 'https://jstxcj.91job.org.cn/code/decode'
    data = {
        'code': code,
        'open_id': 'oTL_q5Frr6j3DdyFkHxt2i9XWacc'
    }
    res = requests.post(url, headers=headers, data=data, verify=False, timeout=(20, 20)).text
    token = res[1: -1]
    print(token)
    print('-' * 30)
    headers['Authorization'] = f'Bearer {token}'
    url = 'https://jstxcj.91job.org.cn/v2/camera/upload'
    files = {'file': open('img.jpg', 'rb')}
    res = requests.post(url, headers=headers, files=files, verify=False, timeout=(20, 20)).text
    print('�ϴ��ɹ� >>>')
    print(res)
    print('-' * 30)
    url = 'https://jstxcj.91job.org.cn/v2/camera/crop'
    res = requests.get(url, headers=headers, verify=False, timeout=(20, 20)).text
    print('�ü��ɹ� >>>')
    print(res)


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    os.environ['NO_PROXY'] = 'jstxcj.91job.org.cn'
    print('-' * 30)
    print('��Ҫ׼������jpgͼƬ һ��ͼ�ɶ�ά�� һ���Լ�����Ƭ')
    print('�ֱ�����code.jpg��img.jpg���ҷ��ڱ�����ͬ���ļ���')
    print('����njtech��(��call) BվUP��<��ס��������ͷ>')
    print('���빫�����赣����˽ ���Ե�Bվ��Դ���ʵ��ԭ��')
    print('�����Ҵ���Ƭ ����ʦ��˵� ��ֹ���ڷǷ���; ����Ը�')
    print('���������ѧϰ����ʹ�� �Ͻ�����ӯ�� ����Ը�')
    print('-' * 30)
    try:
        main()
    except Exception as e:
        print('���������� �������ò����Ի���ϵ����: ', e)
    print('-' * 30)
    input('��� >>>')
