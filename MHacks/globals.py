
class GroupEnum:
    def __init__(self):
        pass

    HACKER = 'hacker'
    SPONSOR = 'sponsor'
    APP_READER = 'application_reader'
    STATS = 'stats_team'
    ALL = (HACKER, SPONSOR, APP_READER, STATS)

groups = GroupEnum()
