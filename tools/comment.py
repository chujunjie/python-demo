# coding=utf-8
import hashlib
import re
import urllib.request
from urllib.parse import unquote

from github import Github


def capture():
    url = 'https://chujunjie.top/sitemap.xml'
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    r = re.compile(r'(chujunjie.top/2018.*?</loc>)')  # 截取sitemap.xml中的所有文章url
    big = re.findall(r, html)
    for i in big:
        str = i[:-6]  # 去掉</loc>标签
        op_sitemap_url = open('sitemap_url.txt', 'a')  # 保存到sitemap_url.txt
        op_sitemap_url.write('%s\n' % str)


def create_issues():
    suffix = ' - 褚俊杰的博客 | MY Blog'  # 标题后缀
    g = Github(login_or_token="xxx")  # 使用token登陆
    repo = g.get_repo("chujunjie/chujunjie.github.io")  # 指定仓库
    # open_issues = repo.get_issues(state='open')  # 获取仓库下open的issues
    for line in open("sitemap_url.xml"):  # 指定生成的sitemap
        line_ = line.rsplit('/', 2)  # 截取url获取标题部分
        title = unquote(line_[1]) + suffix  # unquote url_decode 拼接标题
        body = 'https://' + line  # 拼接https
        label = ['Gitalk', md5_key(line[13:].rstrip("\n"))]  # 标签
        repo.create_issue(title, body=body, labels=label)  # 创建issue


# MD5加密
def md5_key(arg):
    hash = hashlib.md5()
    hash.update(arg.encode("utf8"))
    return hash.hexdigest()


if __name__ == '__main__':
    capture()
    create_issues()
