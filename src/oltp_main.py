from oltp_jobs import jobs


# run through jobs (instances of Mappings class) and call etl method
def run():
    for j in jobs:
        j.etl()


if __name__ == "__main__":
    run()
