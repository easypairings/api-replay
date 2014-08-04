class BadResponseException(Exception):
    def __init__(self, status_code, body, *args, **kwargs):
        self.status_code = status_code
        self.body = body
        super(BadResponseException, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'Status: {}\n{}'.format(self.status_code, self.body)


class MissingSettingsException(Exception):
    def __init__(self, settings, *args, **kwargs):
        self.settings = settings
        super(MissingSettingsException, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'The following settings are required but missing: {}'.format(
            ', '.join(self.settings),
        )
