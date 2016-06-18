#include <stdio.h>
int main(){
	int input, bit;
	printf("Enter any number: ");
	scanf("%d", &input);
	printf("Enter Nth bit to check (0-31): ");
	scanf("%d", &bit);
	input >> bit;
	printf("The %dth bit is set to %d\n", bit, input % 2);
	return 0;
}
