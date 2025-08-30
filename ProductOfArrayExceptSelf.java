import java.util.*;

public class ProductOfArrayExceptSelf {
    public int[] Solution(int nums[]){
        if(nums==null || nums.length==0) return new int[]{};
        int result[] = new int[nums.length];
        Arrays.fill(result,1);
        int pre=1;
        int post=1;
        for(int i=0; i<nums.length; i++){
            result[i] = pre;
            pre=pre*nums[i];
        }
        for(int i=nums.length-1; i>=0; i--){
            result[i] = post*result[i];
            post=post*nums[i];
        }

        return result;
    }

    public static void main(String[] args) {
    int arr[] = {1, 2, 3, 4};
    int[] result = new ProductOfArrayExceptSelf().Solution(arr);
    System.out.println(Arrays.toString(result));
}
}
