#include <stdio.h>
int main(){
	int i, j, input;
	printf("Line: ");
	scanf("%d", &input);
	for (i = 1; i <= input; i++){
		for (j = 0; j < input - i; j++) printf(" ");
		for (j = i; j <= i * 2 - 1; j++) printf("%d", j);
		for (j = (i - 1) * 2; j >= i; j--) printf("%d", j);
		printf("\n");
	}
	return 0;
}

