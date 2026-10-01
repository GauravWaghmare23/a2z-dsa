
public class BinarySearch {

    public static int Search(int[] nums, int target) {

        int first = 0;
        int last = nums.length - 1;

        while (first <= last) {

            int mid = first + (last - first) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                first = mid + 1;
            } else {
                last = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {

        int[] nums = {-1, 0, 3, 5, 9, 12};
        int target = 9;

        int result = Search(nums, target);

        System.out.println("Index : " + result);
    }
}
