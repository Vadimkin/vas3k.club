import mistune


class PlainRenderer(mistune.HTMLRenderer):
    def link(self, link, text=None, title=None):
        return link

    def image(self, src, alt="", title=None):
        return "🖼"

    def emphasis(self, text):
        return text

    def strong(self, text):
        return text

    def codespan(self, text):
        return text

    def linebreak(self):
        return "\n"

    def paragraph(self, text):
        return text + "\n\n"

    def heading(self, text, level):
        return text + "\n\n"

    def newline(self):
        return "\n"

    def block_quote(self, text):
        return text

    def list(self, text, ordered, level, start=None):
        return text

    def list_item(self, text, level):
        return "- " + text