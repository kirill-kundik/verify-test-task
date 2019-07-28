from app.client import Client


def test_client(start_time, end_time, resolution, path, timeout, correct_hash):
    client = Client(
        path=path,
        num_processes=1,
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat(),
        resolution=resolution,
        timeout=timeout
    ).prepare()

    assert client.hashes == correct_hash
