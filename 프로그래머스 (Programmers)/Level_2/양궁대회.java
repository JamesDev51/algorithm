class Solution {
    static int[] bestArr=new int[11];
    static int maxGap=Integer.MIN_VALUE;
    static int[] answer = {-1};
    
    
    static int calculateScoreGap(int[] lionInfo, int[] apeachInfo){
        int lionScore=0;
        int apeachScore=0;
        for (int i=0;i<11;i++){
            if(lionInfo[i]==0 && apeachInfo[i]==0){
                continue;
            }else if(lionInfo[i]<=apeachInfo[i]){
                apeachScore+=(10-i);
            }else if(lionInfo[i]>apeachInfo[i]){
                lionScore+=(10-i);
            }
        }
        return lionScore-apeachScore;
    }
    
    static void dfs(int l,int left, int[] lionInfo, int[] apeachInfo){
        if(l==11){
            if(0<left){
                lionInfo[10]+=left;
            }
            int scoreGap=calculateScoreGap(lionInfo, apeachInfo);
            if(0<scoreGap){
                if(maxGap<scoreGap){
                    maxGap=scoreGap;
                    answer=lionInfo.clone();
                }else if(maxGap==scoreGap){
                    for(int i=10;0<=i;i--){
                        if(answer[i]<lionInfo[i]){
                            answer=lionInfo.clone();
                            break;
                        }else if(answer[i]>lionInfo[i]){
                            break;
                        }
                    }
                }
                
            }
           
            if(0<left){
                lionInfo[10]-=left;
            }
            
        }else{
            if(bestArr[l]<=left){
                lionInfo[l]=bestArr[l];
                dfs(l+1,left-bestArr[l],lionInfo,apeachInfo);
                lionInfo[l]=0;
            }
            dfs(l+1,left,lionInfo,apeachInfo);
        }
    }
    
    public int[] solution(int n, int[] info) {
        for(int i=0;i<11;i++){
            bestArr[i]=info[i]+1;
        }
        dfs(0,n,new int[11],info);

        return answer;
    }
}