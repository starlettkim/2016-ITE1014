#include <stdio.h>
int gcd(int a, int b){ return b ? gcd(b, a % b) : a; }
int main(){
	printf("Enter two numbers to find GCD: ");
	int input1, input2;
	scanf("%d%d", &input1, &input2);
	printf("GCD of %d and %d is %d\n", input1, input2, gcd(input1, input2));
	return 0;
}
