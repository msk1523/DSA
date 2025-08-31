public class ContainerWithMostWater {
    public int Solution(int[] height){
        int left=0, right=height.length-1, area=0;
        if(height==null || height.length<2) return 0;

        while(left<right){
            if(height[left]<height[right]){
                area= Math.max(area, height[left]*(right-left));
                left++;
            }else{
                area=Math.max(area, height[right]*(right-left));
                right--;
            }
        }
        return area;
    }

    public static void main(String[] args) {
        int arr1[]={1,8,6,2,5,4,8,3,7};
        System.out.println(new ContainerWithMostWater().Solution(arr1));
    }
}
