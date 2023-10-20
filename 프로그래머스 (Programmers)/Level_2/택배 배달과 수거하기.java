import java.util.*;

class Solution {
    public void print(Object o) {
        System.out.println(o);
    }

    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int dIdx = n;
        int pIdx = n;
        int dCap, pCap;
        for (int i = n - 1; 0 <= i; i--) {
            if (deliveries[i] == 0)
                dIdx -= 1;
            else {
                break;
            }
        }
        for (int i = n - 1; 0 <= i; i--) {
            if (pickups[i] == 0)
                pIdx -= 1;
            else {
                break;
            }
        }
        print(dIdx);
        print(pIdx);
        while (dIdx > 0 || pIdx > 0) {
            answer += Math.max(dIdx, pIdx) * 2;
            dCap = cap;
            pCap = cap;

            while (dIdx > 0) {
                if (deliveries[dIdx - 1] == 0) {
                    dIdx -= 1;
                    continue;
                }
                if (deliveries[dIdx - 1] <= dCap) {
                    dCap -= deliveries[dIdx - 1];
                    deliveries[dIdx - 1] = 0;
                    dIdx -= 1;
                } else {
                    deliveries[dIdx - 1] -= dCap;
                    break;
                }
            }

            while (pIdx > 0) {
                if (pickups[pIdx - 1] == 0) {
                    pIdx -= 1;
                    continue;
                }
                if (pickups[pIdx - 1] <= pCap) {
                    pCap -= pickups[pIdx - 1];
                    pickups[pIdx - 1] = 0;
                    pIdx -= 1;
                } else {
                    pickups[pIdx - 1] -= pCap;
                    break;
                }
            }
        }
        return answer;
    }
}