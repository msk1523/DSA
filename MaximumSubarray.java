public class MaximumSubarray {
    public int Subarray(int nums[]){
        if(nums==null || nums.length==0) return 0;
        
        int curr = nums[0];
        int max = nums[0];

        for(int i=1; i<nums.length;i++){
            curr = Math.max(nums[i], nums[i]+curr);
            max=Math.max(max, curr);
        }
        
        return max;
    }

    public static void main(String args[]) {
        int arr[]={-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(new MaximumSubarray().Subarray(arr));
    }
}
