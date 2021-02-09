import uuid
import os
from appsettings import Settings

class Log:

    def __init__(self, sess):
        self.session = sess
        if self.session.get('id', None) is None:
            sess['id'] = uuid.uuid4().hex
        self.sessionID = sess['id']
        settings = Settings()
        self.sessLogFile = os.path.join(settings.session_file_dir, self.sessionID)
        self.create_log_folder()
        return

    def exec(self, message):
        file = self.logname()
        fp = open(file, 'a')
        fp.write(message + '\n')
        fp.close()
        self.save_session_data()

    def create_log_folder(self):
        if not os.path.exists(self.sessLogFile):
            os.makedirs(self.sessLogFile)
        return

    def logname(self):
        fname = os.path.join(self.sessLogFile, 'log.txt')
        return fname

    def save_session_data(self):
        fname = os.path.join(self.sessLogFile, 'session.txt')
        fp = open(fname, mode='w')
        for s in self.session:
            name = s
            value = self.session[name]
            fp.write('{}={}\n'.format(name, value))
            print(s)
        fp.close()
        return
