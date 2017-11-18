import requests
from string import ascii_letters, digits


class rpaste:
    def __init__(self):
        self.content = ""
        self.password = ""
        self.language = ""
        self.title = ""
        self.langauge = ""
        self.url = ""
        self.api_url = ""
        self.slug = ""

    def set_content(self, content):
        self.content = content

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

    def get_content(self):
        return self.content

    def get_url(self):
        return self.url

    def get_slug(self):
        return self.slug

    def set_password(self, password):
        self.password = password

    def set_url_slug(self, slug):
        """Set URL or slug."""
        slug = slug[-7:]
        if len(slug) == 7 and \
                slug[0] == "p" and \
                all(x in ascii_letters + digits for x in slug):
            self.slug = slug
            self.url = "https://rpaste.com/" + slug
            self.api_url = "https://rpaste.com/api/paste/view/" + slug
            return
        raise Exception("Invalid slug : " + url)

    def push_paste(self):
        pass

    def pull_paste(self):
        resp = requests.post(self.api_url)
        content = resp.json()
        if 'Error' in content:
            raise Exception(content['Error'])
        self.content = content['body']
        self.title = content['title']
        self.language = content['language']

    def print_info(self):
        print("Title ", self.get_title())
        print("slug ", self.slug)
        print("URL ", self.url)
        print("API URL ", self.api_url)
        print("Language: ", self.get_language())
        print("Body : ", self.get_content())
