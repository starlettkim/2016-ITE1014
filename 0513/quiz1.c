#include <stdio.h>
int main(){
        // i: 줄 번호
        // n: 총 줄의 수
        int i = 0, n;
        printf("line?\n");
        scanf("%d", &n);
        
        // 현재 줄 번호가 총 줄의 수와 같아질때까지 반복
        // (i는 0부터 시작하므로 i = n - 1일때까지 반복)
        while (i < n){
                // 'o'의 개수는 줄 번호와 같으므로, j를 i번 반복시키며 'o' 출력
                int j = i;
                while (j > 0){
                        printf("o");
                        j--;
                }
                // 마지막으로 *를 출력하고 개행
                printf("*\n");
                // 줄 번호 증가
                i++;
        }
        printf("\n");
        return 0;
}
