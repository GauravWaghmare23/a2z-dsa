public class MaxConsecutiveOnes {
    public static void main(String[] args) {
        
        int[] nums = {1,1,0,1,1,1};

        int max = 0;
        int currentMax = 0;

        for(int i=0; i < nums.length; i++){
            if (nums[i]==0) {
                if (currentMax > max) {
                    max = currentMax;
                }
                currentMax = 0;
            }else{
                currentMax += 1;
            }
        }

        if(currentMax > max){
            max = currentMax;
            System.out.println(max);
        }
    }
}
