
-- https://www.xkcd.com/221/
local planekey = redis.pcall('get',ARGV[1])
if planekey == nil then
    local random = math.random(99)
    while(redis.pcall('get',random)~=nil or redis.pcall('hget', 'allocated_parking', random)~=nil)
    do
       random = math.random(99)
    end
     redis.call('set', ARGV[1], ARGV[1])
     redis.call('set', ARGV[1], random)
     redis.call('set', 'allocated_parking', random, 1)
     planekey = redis.pcall('get',ARGV[1])
 end

 return planekey


-- Being that there are more parking lots than planes,
-- and assuming there's no other system in the process
-- and that the set doesn't fail one might as well simply (and efficiently) do:
redis.call('set', ARGV[1], ARGV[1])
return ARGV[1]
