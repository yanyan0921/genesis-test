import core.log_helper as log_helper
import getopt
import sys
import core.dir_parser as dir_parser
from analyser import Analyser
import re
import os

argv = sys.argv[1:]
test_id_list = []
skip_list = []
retry_count = 0
env = 'staging'
config_name = 'default'
dirParser = dir_parser.DirParser("./testcase/")
log_helper.Logger('runner')
os.chdir('./')
deleteList = []


def get_testcase_name(self, test_id):
    for testcase in self.testlist:
        if testcase["testcaseId"] == test_id:
            return testcase["testcaseName"]
    return test_id


if __name__ == '__main__':
    for filename in os.listdir('./'):
        if filename.endswith('.png'):
            os.unlink(filename)
            deleteList.append(filename)
    try:
        options, args = getopt.getopt(argv, "t:f:c:r:", ["test=", "folder=", "conf=", "retry="])
    except getopt.GetoptError:
        sys.exit()
    for option, value in options:
        if option in ("-f", "--folder"):
            folders = value.split(",")
            test_id_list = dirParser.get_folder_files(folders)
        elif option in ("-t", "--test"):
            test_id_list, skip_list = dirParser.get_files(value.split(","))
        elif option in ("-r", "--retry"):
            if value is not None:
                retry_count = int(re.compile(r'[1-9]\d*').fullmatch(value).string)
        elif option in ("-c", "--conf"):
            if value is not None:
                config_name = value
            else:
                config_name = 'default'

    test = Analyser(test_id_list, retry_count, skip_list, config_name)
    test.run()
