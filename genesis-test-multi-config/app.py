from flask import Flask, request, abort, jsonify, make_response
import core.log_helper as log_helper
import logging
import runner
import json
import threading
from rest.transport import Transport

app = Flask(__name__)


@app.route('/tasks', methods=['POST'])
def create_task():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        if isinstance(request.json, dict):
            res = request.json
        else:
            res = json.loads(request.json)
        if 'testRunId' not in res:
            return make_response(jsonify({'error': 'field testRunId is missing!'}), 400)
        elif 'testSuits' not in res:
            return make_response(jsonify({'error': 'field testSuits is missing!'}), 400)
        elif res['testRunId'] == '':
            return make_response(jsonify({'error': 'testRunId can not be empty!'}), 400)
        elif res['testSuits'] == '':
            return make_response(jsonify({'error': 'testSuits can not be empty!'}), 400)
        else:
            log_helper.Logger(res['testRunId'])

            task = {
                'status': 'Pending',
                'testRunId': res['testRunId'],
                'testSuits': res['testSuits']
            }

            testsuits = res["testSuits"]
            try:
                threads = []
                thread_count = len(testsuits)
                transport = Transport("https://pyframework-qa.internal.unity3d.com", "5000")
                post_log = lambda: transport.post_test_log(res['testRunId'])
                barrier = threading.Barrier(thread_count, action=post_log)
                for testsuit in testsuits:
                    testlist = testsuit["testcases"]
                    logging.getLogger("main.app")
                    thread_suit = runner.Analyser(testlist, res['testRunId'],
                                                  testsuit["id"], False, barrier)

                    threads.append(thread_suit)

                for i in range(len(threads)):
                    threads[i].start()

            except Exception as e:
                print(e)

            return make_response(jsonify(task), 200)
    else:
        abort(405)


@app.route('/tasks/local', methods=['POST'])
def create_local_task():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        if isinstance(request.json, dict):
            res = request.json
        else:
            res = json.loads(request.json)
        if 'testcases' not in res:
            return make_response(jsonify({'error': 'field testcases is missing!'}), 400)
        else:
            task = {
                'status': 'start',
                'testcases': res['testcases']
            }

            testlist = res['testcases']
            logger = logging.getLogger("main.app")
            thread_a = runner.Analyser(testlist, "",
                                       "", True)
            thread_a.start()
            thread_a.join()

            return make_response(jsonify(task), 200)
    else:
        abort(405)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if len(str(task_id)) == 0:
        abort(404)
    return make_response(jsonify({'task': str(task_id)}), 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=40003)
