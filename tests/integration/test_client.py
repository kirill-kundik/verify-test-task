from multiprocessing import Process, cpu_count

from app.client import Client


def test_client(start_time, end_time, resolution, tmpdir, timeout, correct_hash):
    path = tmpdir.mkdir('test')

    client = Client(
        path=path,
        num_processes=max(cpu_count() - 1, 1),
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat(),
        resolution=resolution,
        timeout=timeout
    ).prepare()

    process = Process(target=client.run)
    process.start()
    process.join()

    client2 = Client(
        path=path,
        num_processes=1,
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat(),
        resolution=resolution,
        timeout=timeout
    ).prepare()

    assert client2.hashes == correct_hash
