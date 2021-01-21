import os


class Settings:

    def __init__(self):
        self.message = []
        self.ip = self.get_env('APP_IP', '0.0.0.0')
        self.port = self.get_env('APP_PORT', 5000)
        self.api_ip = self.get_env('APP_API_IP', '')
        self.api_port = self.get_env('APP_API_PORT', 'n')
        self.session_secret_key = self.get_env('APP_SECRET_KEY', '')
        self.session_file_dir = self.get_env('APP_SESS_FILE_DIR', '')

        if self.message.__len__() > 0:
            print('Warning:')
            for i in range(self.message.__len__()):
                print(self.message[i])

    def get_env(self, varname, default):
        try:
            value = os.environ.get(varname)
        except:
            value = None
        if value is None:
            value = default
            self.message.append('{} not defined'.format(varname))
        return value

