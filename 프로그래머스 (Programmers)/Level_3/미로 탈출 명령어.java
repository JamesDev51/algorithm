import java.util.*;

class Solution {

    class Path {
        String history;
        int distance;
        int x;
        int y;

        Path(String history, int distance, int x, int y) {
            this.history = history;
            this.distance = distance;
            this.x = x;
            this.y = y;
        }
    }

    public int getManhathanDistance(int x1, int y1, int x2, int y2) {
        return Math.abs(x2 - x1) + Math.abs(y2 - y1);
    }

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        PriorityQueue<Path> pq = new PriorityQueue<>((o1, o2) -> {
            return o1.history.compareTo(o2.history);
        });

        int initalManhaThan = getManhathanDistance(r, c, x, y);
        if (k < initalManhaThan)
            return "impossible";
        Path initialPath = new Path("", initalManhaThan, x, y);

        pq.add(initialPath);
        Map<Integer, String> idxToCh = new HashMap<>();
        idxToCh.put(0, "d");
        idxToCh.put(1, "l");
        idxToCh.put(2, "r");
        idxToCh.put(3, "u");

        int[] dx = { 1, 0, 0, -1 };
        int[] dy = { 0, -1, 1, 0 };

        while (!pq.isEmpty()) {
            Path nowPath = pq.poll();
            int steps = nowPath.history.length();
            if (nowPath.x == r && nowPath.y == c) {
                if (steps == k) {
                    return nowPath.history;
                } else if ((k - steps) % 2 == 1) {
                    continue;
                }
            }
            for (int d = 0; d < 4; d++) {
                int nx = nowPath.x + dx[d];
                int ny = nowPath.y + dy[d];
                if (nx < 1 || n < nx || ny < 1 || m < ny)
                    continue;
                int estimation = steps + 1 + getManhathanDistance(r, c, nx, ny);
                if (k < estimation)
                    continue;
                Path newPath = new Path(nowPath.history.concat(idxToCh.get(d)), estimation, nx, ny);
                pq.add(newPath);
                break;
            }

        }
        return "impossible";
    }
}