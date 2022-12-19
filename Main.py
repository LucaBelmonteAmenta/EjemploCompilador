# -*- encoding:utf-8 -*-
from core.Core import Core
from config import APP_PATH

"""
    Main class. Responsible for running the application.
"""
class Main:
    @staticmethod
    def run():
        try:
            print(APP_PATH)
            app = Core.openController("home")
            app.main()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()

    