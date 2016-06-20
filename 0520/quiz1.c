#include <stdio.h>

// 팩토리얼을 구하는 함수.
// 삼항연산자: <조건> ? <참일때 실행> : <거짓일때 실행>
// 따라서 아래에서 n이 1 이상이면 조건문이 참이 되어 n! = n * (n-1)! 임을 이용해 n * fac(n - 1)을 리턴하고,
// n이 0이면 0! = 1이므로 1을 리턴한다.
int fac(int n) { return n ? n * fac(n - 1) : 1; }

int main(){
	printf("Number: ");
	// 입력을 받을 변수
	int input;
	scanf("%d", &input);
	// 입력값과 결과값을 출력한다.
	printf("%d factorial is %d\n", input, fac(input));
	return 0;
}
