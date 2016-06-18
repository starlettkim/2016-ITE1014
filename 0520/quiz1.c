#include <stdio.h>

int fac(int n){
	if (n==1) return 1;
	return n * fac(n-1);
}

int main(){
	printf("Number: ");
	int input;
	scanf("%d", &input);
	printf("%d factorial is %d\n", input, fac(input));
	return 0;
}
