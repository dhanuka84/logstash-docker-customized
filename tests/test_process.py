from .fixtures import logstash


def test_process_is_pid_1(logstash):
    assert logstash.process.pid == 1


def test_process_is_running_as_the_correct_user(logstash):
    assert logstash.process.user == 'logstash'
