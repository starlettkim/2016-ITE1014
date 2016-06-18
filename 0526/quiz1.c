#include <stdio.h>
int main(){
	int input;
	printf("Enter the number of prime numbers required: ");
	scanf("%d", &input);
	printf("First %d prime numbers are: \n", input);
	int count = 0, i, j;
	for (i = 2; count < input; i++){
		int chk = 0;
		for (j = 2; j <= i / 2; j++){
			if (!(i % j)){
				chk =1;
				break;
			}
		}
		if (!chk){
			count++;
			printf("%d\n", i);
		}
	}
	return 0;
}
