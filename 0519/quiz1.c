#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 들어온 인자를 100, 10, 1의 요소로 분리하는 함수
void calc(int input){
	// input을 100으로 나눠서 100의자리 수를 출력한다.
	printf("100: %d, ", input / 100);
	// input을 10으로 나눈 뒤, 그것을 10으로 나눈 나머지를 이용해 10의 자리수를 구한다.
	printf("10: %d, ", (input / 10) % 10);
	// input을 1로 나눈 뒤(생략), 그것을 10으로 나눈 나머지를 이용해 1의 자리수를 구한다.
	printf("1: %d\n", input % 10);
}

// 랜덤으로 cost를 뽑고 이를 totalCost에 더하는 함수
void randomCost(){
	// static를 사용해서 totalCost가 한 번만 초기화되도록 한다.
	static int totalCost = 0;
	// cost 값을 랜덤으로 뽑는다.
	int cost = rand() % 100 + 1;
	// 이를 totalCost에 더한다.
	totalCost += cost;
	printf("Cost: %d\n", cost);
	printf("Total Cost: %d\n", totalCost);
	// totalCost를 인자로 calc 함수를 호출한다.
	calc(totalCost);
}

int main(){
	// 시간을 랜덤 시드로 사용한다.
	srand((unsigned int)time(NULL));
	// 입력을 저장할 변수
	int input;
	// 입력값이 -1이 들어오면 break
	while (1){
		printf("End: -1 / Continue: Any key.\n>> ");
		scanf("%d", &input);
		// 입력값이 -1이면 break하고
		if (input == -1) break;
		// 그렇지 않으면 randomCost  함수 실행.
		randomCost();
	}
	return 0;
}
