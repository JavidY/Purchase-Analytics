from oltp_jobs import jobs


def run():
    for j in jobs:
        j.etl()


if __name__ == "__main__":
    run()
