#include <stdio.h>
int main(){
	int i = 0, n;
	printf("line?\n");
	scanf("%d", &n);
	while (i < n){
		int j = i;
		while (j > 0){
			printf("o");
			j--;
		}
		printf("*\n");
		i++;
	}
	printf("\n");
	return 0;
}
