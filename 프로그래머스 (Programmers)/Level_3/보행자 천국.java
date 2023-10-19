class Solution {
    int MOD = 20170805;
    
    public int solution(int m, int n, int[][] cityMap) {
        int answer = 0;
        int[][][] mat= new int[m][n][2];
        mat[0][0][0]=1; //오른쪽
        mat[0][0][1]=1; //아래
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(i==0 && j==0)continue;
                if(cityMap[i][j]==0){
                    if(0<=j-1)mat[i][j][0]+=mat[i][j-1][0]%MOD;
                    if(0<=i-1)mat[i][j][0]+=mat[i-1][j][1]%MOD;
                    mat[i][j][0]%=MOD;
                    mat[i][j][1]=mat[i][j][0];
                }else if(cityMap[i][j]==1){
                    continue;
                }else if(cityMap[i][j]==2){
                    if(0<=j-1)mat[i][j][0]+=mat[i][j-1][0]%MOD;
                    if(0<=i-1)mat[i][j][1]+=mat[i-1][j][1]%MOD;
                }
            }
        }
        answer=Math.max(mat[m-1][n-1][0],mat[m-1][n-1][1]);
        
        return answer;
    }
}