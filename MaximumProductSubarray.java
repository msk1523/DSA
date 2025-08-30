public class MaximumProductSubarray {
    public int Solution(int nums[]){
        if(nums==null || nums.length==0){
            return 0;
        }
        int min=nums[0], max=nums[0];
        for(int i=1; i<nums.length; i++){
            int prevMin = min;
            int prevMax=max;
            min = Math.min(nums[i], Math.min(nums[i]*prevMin , nums[i]*prevMax));
            max = Math.max(nums[i] , Math.max(nums[i]*prevMin, nums[i]*prevMax));
        }
        return max;
    }

    public static void main(String[] args) {
        int arr1[]={5,3,1,-2,0,-5,8,-3};
        System.out.println(new MaximumProductSubarray().Solution(arr1));
    }
}
