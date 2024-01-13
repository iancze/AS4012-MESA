from as4012_mesa import reader


def test_read_history(history_fname):
    reader.read_history(history_fname)
