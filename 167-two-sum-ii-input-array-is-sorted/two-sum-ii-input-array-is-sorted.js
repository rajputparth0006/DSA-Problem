/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let n = numbers.length
    let i = 0
    let j = n - 1
    while(i < j){
        const sum = numbers[i] + numbers[j] 
         if (sum > target){
            j--
         }
         else if(sum < target){
            i++
         }
         else{
            return [i + 1,j + 1]
         }
    }
    return []
    
};