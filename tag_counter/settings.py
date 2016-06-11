from os.path import dirname, abspath, join


ROOT_DIR = dirname(dirname(abspath(__file__)))
DB_PATH = join(ROOT_DIR, 'tag_counter.db')
