#include <stdio.h>
int main(){
	printf("Enter two numbers to find LCM: ");
	int input1, input2, i;
	scanf("%d%d", &input1, &input2);
	for (i = input1; i % input2; i += input1);
	printf("LCM of %d and %d is %d\n", input1, input2, i);
	return 0;
}
