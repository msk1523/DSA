class BuySellStocks{
    public int buySellStocks(int nums[]){
        int profit=0;
        if(nums==null || nums.length<=1) return 0;
        int buy=nums[0];
        int sell=0;
        for(int i=1; i<nums.length; i++){
            if(nums[i]<buy) buy=nums[i];
            else{
                int currentProfit = nums[i] - buy;
                profit=Math.max(profit, currentProfit);
            }
        }
        return profit;
    }

    public static void main(String[] args) {
        BuySellStocks obj = new BuySellStocks();
        int arr1[] = {7,1,5,3,6,4};
        int arr2[] = {7,6,4,3,1}; // Decreasing prices
        int arr3[] = {1,2,3,4,5}; // Increasing prices
        int arr4[] = null; // Null input
        int arr5[] = {}; // Empty array
        
        System.out.println("Test 1: " + obj.buySellStocks(arr1)); // Should output 5
        System.out.println("Test 2: " + obj.buySellStocks(arr2)); // Should output 0
        System.out.println("Test 3: " + obj.buySellStocks(arr3)); // Should output 4
        System.out.println("Test 4: " + obj.buySellStocks(arr4)); // Should output 0
        System.out.println("Test 5: " + obj.buySellStocks(arr5)); // Should output 0
    }
}