#include <stdio.h>
int main(){
	int input;
	printf("Enter the int?\n");
	scanf("%d", &input);
	int n = 1, sum = 0;
	printf("Reverse is [");
	while ((input % 10) != 0){
		printf("%d", input % 10);
		sum += input % 10;
		input = input / 10;
	}
	printf("]\n");
	printf("Sum is [%d]\n", sum);
	return 0;
}
