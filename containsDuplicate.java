import java.util.*;
public class containsDuplicate {
    public boolean ContainsDuplicate(int nums[]){
        if(nums==null || nums.length<=1) return false;
        Set<Integer> check = new HashSet<>();
        for(int num : nums){
            check.add(num);
        }
        if(check.size()!=nums.length) return true;
        return false;
    }
    public static void main(String args[]) {
        int arr[]={1,2,3};
        int arr1[]={1,2,3,1};
        System.out.println(new containsDuplicate().ContainsDuplicate(arr1));
        System.out.println(new containsDuplicate().ContainsDuplicate(arr));
    }
}
