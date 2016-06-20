#include <stdio.h>
int main(){
	// 입력값을 받는 변수
	int input;
	// 총합을 저장할 변수
	int sum = 0;
	printf("Enter the int?\n");
	scanf("%d", &input);

	printf("Reverse is [");
	// input 값이 0이 될때까지 반복
	while (input){
		// input의 맨 끝자리 출력
		printf("%d", input % 10);
		// 맨 끝자리를 sum에 더함
		sum += input % 10;
		// input을 10으로 나눠서 맨 끝자리를 버림
		input /= 10;
	}
	printf("]\n");
	printf("Sum is [%d]\n", sum);
	return 0;
}
