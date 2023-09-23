
# A DevOps team needs to perform 
# a system update on 212 servers. However, 
# they can only update 8 servers per day due to 
# resource restrictions.
# They want to find out how many full 
# days it will take to complete the updates
# and if there will be servers left over on
# the end of final full day.


num_of_servers = 212
limit_per_day = 8

full_days = num_of_servers // limit_per_day
servers_left = num_of_servers % limit_per_day

print(f" days it will take to complete the updates is {full_days} ")
print(f" servers_left is {servers_left} ")



