Use two pointer
keep track of max bar if right is max then max water level will be defined by
left bar
if left bar  > right bar the level will be  defind by right bar since it is shortest
also for curr position water height(area) will be calculated by keeping in mind max height of right bar till now .
if curr_height > max_right_till now then no unit can be added just update max_right_till now to current