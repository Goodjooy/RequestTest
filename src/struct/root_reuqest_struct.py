from requests import Session, Request, PreparedRequest
from requests.structures import CaseInsensitiveDict
from wx import TreeCtrl

from .request_body.body import Body

# 请求时的基本请求数据


class RootRequestStruct(object):
    def __init__(self, name: str, target_url: str, session: Session, root, tree: TreeCtrl) -> None:
        self.name = name

        self.target_url = target_url
        # 请求方法
        self.request_method: str = "GET"

        self.session: Session = session
        self.headers = dict(session.headers.copy())
        self.cookies = dict(session.cookies.copy().item())

        self.request_body:Body = ...

        # tree
        self.root = root
        self.tree: TreeCtrl = tree

        self.self_root = ...

        self.header_title_id = ...
        self.headers_id = []
        # 添加头
        self.new_header_id = ...

        self.cookie_title_id = ...
        self.cookies_id = []
        # 添加cookie
        self.new_cookie_id = ...

        self.request_body_title_id = ...

        # 请求操作区
        self.operator_title_id = ...
        self.request_operator = {}

    def append_to_tree(self):
        # 自身依附的节点
        self.self_root = self.tree.AppendItem(
            self.root, f"{self.name}-[{self.request_method}]")

        # 请求头和cookies
        self.header_title_id = self.tree.AppendItem(self.self_root, "请求头")
        self.headers_id.clear()
        for k, v in self.headers.items():
            temp_id = self.tree.AppendItem(self.header_title_id, f"{k}:{v}")
            self.headers_id.append(temp_id)
        self.new_header_id = self.tree.AppendItem(
            self.header_title_id, "添加新的请求头")

        self.cookie_title_id = self.tree.AppendItem(self.self_root, "cookies")
        self.cookies_id.clear()
        for k, v in self.cookies.items():
            temp_id = self.tree.AppendItem(self.cookie_title_id, f"{k}:{v}")
            self.cookies_id.append(temp_id)
        self.new_cookie_id = self.tree.AppendItem(
            self.cookie_title_id, "添加新的cookie")

        # 请求主体的节点
        self.request_body_title_id = self.tree.AppendItem(
            self.self_root, "请求主体")
        self.request_body.append_to_tree(self.request_body_title_id, self.tree)

        # 请求操作
        self.operator_title_id = self.tree.AppendItem(self.self_root, "操作区")

    def edit_header(self, key, value):
        """
        添加或者编辑请求头
        """
        self.headers[key] = value

    def edit_cookie(self, key, value):
        """
        添加或者编辑cookie
        """
        self.cookies[key] = value

    def request_method_change(self, method):
        """
        修改请求方法
        """
        self.request_method = method

    def send(self):
        """
        同步代码，会阻塞
        """
        req = Request()
        prepare: PreparedRequest = self.session.prepare_request(req)

        prepare.prepare_url(self.target_url)
        prepare.prepare_method(self.request_method)
        prepare.prepare_headers(CaseInsensitiveDict(self.headers))
        prepare.prepare_cookies(self.cookies)
        prepare.prepare_body(**self.request_body.send_data())

        return self.session.send(prepare)

