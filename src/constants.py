from pathlib import Path

BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DOWNLOAD_HREF = r'.+pdf-a4\.zip$'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
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
LATEST_VERSION_PATTERN = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
MAIN_DOC_URL = 'https://docs.python.org/3/'
PEP_DOC_URL = 'https://peps.python.org/'
TYPE_OF_OUTPUT = ('pretty', 'file')
