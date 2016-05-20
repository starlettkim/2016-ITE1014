#include <stdio.h>
int main(){
	int n = 1, sum = 0;
	while (n <= 5){
		int input = -1;
		while (input < 0){
			printf("[%d] number? ", n);
			scanf("%d", &input);
		}
		n++;
		sum += input;
	}
	printf("Total sum is [%d]\n", sum);
	return 0;
}	
