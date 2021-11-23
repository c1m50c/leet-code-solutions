impl Solution {
    #[inline]
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut answer: i32 = 0;
        for i in nums.iter() { answer ^= i; }
        return answer;
    }
}