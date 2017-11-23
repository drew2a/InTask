import java.util.HashMap;

class Solution {

    public int solution(int[] A) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int item : A) {
            Integer count = map.getOrDefault(item, 0);
            map.put(item, count + 1);
        }

        int left = 0;
        for (; left < A.length; left++) {
            Integer count = map.get(A[left]);
            if (count <= 1) {
                break;
            } else {
                map.put(A[left], count - 1);
            }
        }

        int right = A.length - 1;
        for (; right >= 0; right--) {
            Integer count = map.get(A[right]);
            if (count <= 1) {
                break;
            } else {
                map.put(A[right], count - 1);
            }
        }
        return right - left + 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.print(String.valueOf(solution.solution(new int[]{1, 3, 7, 3, 1, 3, 4, 1})) + '\n');
        System.out.print(String.valueOf(solution.solution(new int[]{1})) + '\n');
        System.out.print(String.valueOf(solution.solution(new int[]{1, 1, 1, 1, 1, 1, 1, 1, 1, 2})) + '\n');
        System.out.print(String.valueOf(solution.solution(new int[]{2, 1, 1, 1, 1, 1, 1, 1, 1, 3})) + '\n');
        System.out.print(String.valueOf(solution.solution(new int[]{1, 2, 3, 1, 1})) + '\n');
        System.out.print(String.valueOf(solution.solution(new int[]{4, 2, 1, 3, 3, 1, 2, 2, 4, 3})) + '\n');
    }
}