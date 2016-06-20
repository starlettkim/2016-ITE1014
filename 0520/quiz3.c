#include <stdio.h>

// 계산값을 구하고 그를 리턴하는 함수
int calc(int n, int len){
	// 만약 n이 0이라면 0을 리턴한다.
	if (!n) return 0;
	int i, sum = 1;
	// n의 마지막 자리 숫자를 len번 제곱하여, sum에 저장한다.
	for (i = 0; i < len; i++){
		sum *= (n % 10);
	}
	// n의 마지막 자리 숫자로 계산한 값은 이제 sum에 저장되어 있고,
	// 나머지 자리 숫자도 계산하기 위해서, n에서 마지막 자리 숫자를 제거하여(n/10) calc 함수를 재귀 호출한다.
	return sum + calc(n/10, len);
}

int main(){
	// input: 입력값을 저장
	// len: 입력값의 길이를 저장
	// tmp: 입력값의 길이를 구하기 위한 변수
	int len = 0, input, tmp;
	printf("Number: ");
	scanf("%d", &input);
	// input을 tmp에 대입
	tmp = input;
	// tmp가 0이 될떄까지
	while (tmp){
		// tmp를 10으로 나눠 가면서
		tmp /= 10;
		// tmp의 길이를 더함
		len++;
	}

	// 입력값과 입력값의 길이를 인자로 calc를 호출해 계산값을 구한 뒤 input과 같은지 비교한다.
	if (input == calc(input, len))
		printf("%d is a armstrong number.\n", input);
	else
		printf("%d is not a armstrong number.\n", input);
	return 0;
}
