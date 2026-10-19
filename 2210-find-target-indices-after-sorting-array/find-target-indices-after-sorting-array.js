/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) 
{
    
    var number = []
    var arr = nums.sort((a,b) => a-b)
    for(var i = 0 ; i < arr.length ; i++){
        if(arr[i] == target){
            number.push(i)
        }
    
    }
    return number
};