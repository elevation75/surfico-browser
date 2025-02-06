import json
import os
import logging

# Set up logging
logger = logging.getLogger(__name__)

class BookmarksStorage:
    def __init__(self):
        self.bookmarks_file = os.path.expanduser('~/.surfico/bookmarks.json')
        self._ensure_directory_exists()
        self._load_bookmarks()
        logger.debug("BookmarksStorage initialized with file: %s", self.bookmarks_file)
    
    def _ensure_directory_exists(self):
        directory = os.path.dirname(self.bookmarks_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.debug("Created directory: %s", directory)
        if not os.path.exists(self.bookmarks_file):
            self._save_bookmarks([])
            logger.debug("Created empty bookmarks file")
    
    def _load_bookmarks(self):
        try:
            with open(self.bookmarks_file, 'r') as f:
                self.bookmarks = json.load(f)
                logger.debug("Loaded bookmarks: %s", self.bookmarks)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error("Error loading bookmarks: %s", e)
            self.bookmarks = []
    
    def _save_bookmarks(self, bookmarks):
        try:
            with open(self.bookmarks_file, 'w') as f:
                json.dump(bookmarks, f, indent=2)
                logger.debug("Saved bookmarks: %s", bookmarks)
        except Exception as e:
            logger.error("Error saving bookmarks: %s", e)
    
    def add_bookmark(self, title, url):
        bookmark = {'title': title, 'url': url}
        logger.debug("Adding bookmark: %s", bookmark)
        if bookmark not in self.bookmarks:
            self.bookmarks.append(bookmark)
            self._save_bookmarks(self.bookmarks)
            logger.debug("Bookmark added successfully")
        else:
            logger.debug("Bookmark already exists")