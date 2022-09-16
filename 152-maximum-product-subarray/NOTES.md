This is madified kadane algo
in this problem if there is all positive no or even no of no. element then max is product of all
We left with first case where there is odd negative element
if there is off neg no then there should be a delimiter position whose left of right we can find our max prod
Example: [7,8,-1,5,-1,8,3,**-7**,4,3]
Here our partition or delimiter element is -7 it left  and right we can find our max product.
sice on both side product will be positive
So we can use prfix prod or suffix prod and find the max from it
We have to handle case where 0 is in or arr
as this will make our prefix or siffix as 0
so we do this by checkin this using if condition and if prefix is 0 set it to 1 so that algorithm can run for other elements