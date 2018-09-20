def binarysearch(array, tails, tailslength, n)
    l, r = 0, tailslength
    while r - l > 1
        mid = (l + r) / 2  
        l = mid if (array[tails[mid]] < n)
        r = mid if (array[tails[mid]] > n)
        break if (array[tails[mid]] == n)
    end
    return r
end
def binary_search(nums, idxs, n, k)
    l, r = 0, n
    while (r-l > 1)
        mid = (l+r)/2
        l = mid if (nums[idxs[mid]] < k) 
        r = mid if (nums[idxs[mid]] > k) 
        break   if (nums[idxs[mid]] == k)
    end
    return r
end

n = gets.strip.to_i
array = []
n.times { array.push(gets.strip.to_i) }
tails = Array.new(n+1) { nil }
tails[0] = 0
tailslength = 1
for x in 1..n-1
    if array[tails[0]] > array[x]
        tails[0] = x
    elsif array[tails[tailslength-1]] < array[x]
        tails[tailslength] = x
        tailslength += 1
    else
        k = binarysearch(array, tails, tailslength, array[x])
        if array[tails[k - 1]] < array[x]
            tails[k] = x
        end
    end    
end

p tailslength
