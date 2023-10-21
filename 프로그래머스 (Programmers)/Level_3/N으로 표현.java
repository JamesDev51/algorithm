import java.util.*;

class Solution {
    public void print(Object o) {
        System.out.println(o);
    }

    static Map<Integer, Integer> dp = new HashMap<>();

    public void dfs(int N, int now, int cnt, int goal) {
        if (cnt > 8 || (cnt > 0 && now == 0))
            return;

        dp.put(now, Math.min(dp.getOrDefault(now, cnt), cnt));

        for (int i = N, iter = 1; i <= 1111111111; i = 10 * i + N, iter++) {
            dfs(N, now + i, cnt + iter, goal);
            dfs(N, now - i, cnt + iter, goal);
            dfs(N, now * i, cnt + iter, goal);
            dfs(N, now / i, cnt + iter, goal);
        }

    }

    public int solution(int N, int number) {

        for (int i = N, cnt = 1; i <= 1111111111; i = 10 * i + N, cnt++) {
            dp.put(i, cnt);
        }

        dfs(N, 0, 0, number);
        int answer = dp.getOrDefault(number, -1);
        return answer;
    }
}