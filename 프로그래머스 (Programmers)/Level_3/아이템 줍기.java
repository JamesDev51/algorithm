import java.util.*;
class Solution {
    class Coord{
        int x;
        int y;
        int dist;
        public Coord(int x,int y,int dist){
            this.x=x;
            this.y=y;
            this.dist=dist;
        }
    }
    static void print(Object o){
        System.out.println(o);
    }
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        int[][] mat=new int[102][102];
        for(int i=0;i<rectangle.length;i++){
            int x1=rectangle[i][0],y1=rectangle[i][1],x2=rectangle[i][2],y2=rectangle[i][3];
            for(int x=2*x1;x<=2*x2;x++){
                for(int y=2*y1;y<=2*y2;y++){
                    if(x==2*x1 || x==2*x2 || y==2*y1 || y==2*y2){
                        if(mat[x][y]==2)continue;
                        mat[x][y]=1;
                    }else{
                        mat[x][y]=2;   
                    }
                }
            }
        }
        
        int[][] ch=new int[102][102];
        Queue<Coord> que=new LinkedList<>();
        que.add(new Coord(2*characterX,2*characterY,0));
        ch[2*characterX][2*characterY]=1;
        int[] dx={-1,0,1,0},dy={0,1,0,-1};
        while(!que.isEmpty()){
            Coord now=que.poll();
            if(now.x==itemX*2 && now.y==itemY*2){
                answer=(int)now.dist/2;
                break;
            }
            for(int d=0;d<4;d++){
                int nx=now.x+dx[d],ny=now.y+dy[d];
                if(0<=nx && nx<102 && 0<=ny && ny<102 &&ch[nx][ny]==0 && mat[nx][ny]==1){
                    ch[nx][ny]=1;
                    que.add(new Coord(nx,ny,now.dist+1));
                }
            }
        }
        
        return answer;
    }
}