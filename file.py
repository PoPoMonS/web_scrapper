def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position,Company,Location,URL\n")

    for job in jobs:
        file.write(
            f"{job['job_title']},{job['company_name']},{job['region']},{job['link']}\n"
        )

    file.close()
