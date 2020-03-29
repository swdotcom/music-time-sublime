'''
This file contains constants

'''
# SoftwareUtil.py
VERSION = '0.9.3'
PLUGIN_ID = 1
DASHBOARD_LABEL_WIDTH = 25
DASHBOARD_VALUE_WIDTH = 25
MARKER_WIDTH = 4

USER_AGENT = 'Music Time Sublime Plugin'

SOFTWARE_API = "https://api.software.com"
SOFTWARE_URL = "https://app.software.com"

SPOTIFY_API = "https://api.spotify.com"
SPOTIFY_REFRESH_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_WEB_PLAYER = "https://open.spotify.com"
SLACK_API = "https://slack.com"

ST3_GITHUB_URL = "https://github.com/swdotcom/music-time-sublime/issues"
FEEDBACK_MAIL_ID = "mailto:cody@software.com"

# Software_headers = {'content-type': 'application/json', 'Authorization': jwt}
# Spotify_headers = {"Authorization": "Bearer {}".format(access_token)}

# SoftwareOffline.py
sessionSummaryData = None
lastDayOfMonth = 0
SERVICE_NOT_AVAIL = "Our service is temporarily unavailable.\n\nPlease try again later.\n"
ONE_MINUTE_IN_SEC = 60
SECONDS_PER_HOUR = 60 * 60
LONG_THRESHOLD_HOURS = 12
SHORT_THRESHOLD_HOURS = 4
NO_TOKEN_THRESHOLD_HOURS = 2
LOGIN_LABEL = "Log in"

# Software.py
DEFAULT_DURATION = 60
PROJECT_DIR = None
check_online_interval_sec = 60 * 10
retry_counter = 0
SOFTWARE_TOP_40 = "6jCkTED0V5NEuM8sKbGG1Z"
# 
