from pathlib import Path

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}

MAIN_DOC_URL = 'https://docs.python.org/3/'
BASE_DIR = Path(__file__).parent
LOG_TIMESTAMP_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DISPLAY_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
PEP_URL = 'https://peps.python.org/'
PRETTY_OUTPUT = 'pretty'
FILE_OUTPUT = 'file'
LOG_DIR_NAME = 'logs'
LOG_FILE_NAME = 'parser.log'
OUTPUT_FORMAT_DEFAULT = None
OUTPUT_FORMAT_FILE = 'file'
OUTPUT_FORMAT_PRETTY = 'pretty'
RESULTS_DIR = 'results'
