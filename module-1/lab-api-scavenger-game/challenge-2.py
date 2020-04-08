# 1. Obtain all the commits made in the past week via API, which is a JSON array that contains 
#multiple commit objects.

#GET /repos/:owner/:repo/commits

path_commits = "/repos/ironhack-datalabs/datamad0320/commits"
queryParams = {
    "since":"Apr 01, 2020"
}
commits = get_github(path_commits)

#2. Count how many commit objects are contained in the array.

len(commits)