import re
from mkdocs.plugins import BasePlugin


class ContentFilterPlugin(BasePlugin):
    def on_page_markdown(self, in_markdown, **kwargs):
        filtered = re.sub(r'(\w+\s+)---(\s+)', r'\1—\2', in_markdown)
        filtered = re.sub(r'(\w+\s+)--(\s+)', r'\1–\2', filtered)
        return filtered
