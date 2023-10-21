import java.util.*;
class Solution {
    public String[] solution(String[] s) {
        int size=s.length;
        
        String[] answer = new String[size];
        
        for(int i=0;i<size;i++){
            String str=s[i];
            int ooz=0;
            int o=0;
            StringBuilder sb = new StringBuilder();
            
            for(int j=0;j<str.length();j++){
                char ch=str.charAt(j);
                if(ch=='1'){
                    o++;
                }else{
                    if(o>=2){
                        ooz++;
                        o-=2;
                    }else{
                        while(0<o){
                            sb.append('1');
                            o--;
                        }
                        sb.append('0');
                    }
                }
            }
            while(0<ooz){
                sb.append("110");
                ooz--;
            }
            while(0<o){
                sb.append('1');
                o--;
            }
            answer[i]=sb.toString();
            
            
        }
        
        
        return answer;
    }
}