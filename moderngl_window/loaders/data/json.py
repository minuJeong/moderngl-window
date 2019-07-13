import json
import logging

from moderngl_window.loaders.base import BaseLoader
from moderngl_window.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)


class Loader(BaseLoader):
    kind = 'json'

    def load(self):
        """Load a file as json"""
        self.meta.resolved_path = self.find_data(self.meta.path)

        if not self.meta.resolved_path:
            raise ImproperlyConfigured("Data file '{}' not found".format(self.meta.path))

        logger.info("Loading: %s", self.meta.path)

        with open(self.meta.resolved_path, 'r') as fd:
            return json.loads(fd.read())
