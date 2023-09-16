import java.util.*;
class Solution {
    
    List<List<Integer>> graph = new ArrayList<>();
    
    public int dfs(int[] info,int nowNode, int sheep, int wolf,List<Integer> nodes){
        if(info[nowNode]==0){
            sheep++;
        }else{
            wolf++;
        }
        
        int maxSheep=sheep;
        
        if(sheep<=wolf)return maxSheep;
        
        
        for(int i=0;i<nodes.size();i++){
            int nextNode=nodes.get(i);
            List<Integer> nextNodes = new ArrayList<>(nodes);
            nextNodes.remove((Integer)nextNode);
            nextNodes.addAll(graph.get(nextNode));
            maxSheep=Math.max(maxSheep,dfs(info,nextNode,sheep,wolf,nextNodes));
            
        }
        
        return maxSheep;
    }
    public int solution(int[] info, int[][] edges) {
        int answer = 0;
        int n = info.length;
        for(int i=0;i<n;i++){
            graph.add(new ArrayList<Integer>());
        }
        for(int i=0;i<n-1;i++){
            graph.get(edges[i][0]).add(edges[i][1]);
        }
        List<Integer> nodes = new ArrayList();
        for(int i=0;i<graph.get(0).size();i++){
            nodes.add(graph.get(0).get(i));
        }
        
        answer=dfs(info,0,0,0,nodes);
        
        
        return answer;
    }
    
}