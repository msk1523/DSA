import java.util.*;
public class LongestIncreasingSubsequence_dp {
    public int Solution(int[] nums){
        int[] dp = new int[nums.length];
        Arrays.fill(dp,1);
        int max=1;
        for(int i=1; i<nums.length;i++){
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    dp[i]=Math.max(dp[i], 1+dp[j]);
                    max=Math.max(max, dp[i]);
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int arr1[]={10,9,2,5,3,7,101,18};
        System.out.println(new LongestIncreasingSubsequence_dp().Solution(arr1));
    }
}
