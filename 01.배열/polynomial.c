#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define MAX(a,b) (((a)>(b))? (a):(b))
#define MAX_LEN 101

typedef struct Polynomial {
	int degree;
	int coef[MAX_LEN];
}polynomial;

polynomial poly_add1(polynomial A, polynomial B) {
	polynomial C; // 결과 다항식

	int Apos = 0, Bpos = 0, Cpos = 0;// 배열 인덱스 변수
	int degree_a = A.degree;
	int degree_b = B.degree;
	C.degree = MAX(A.degree, B.degree);
	// 결과 다항식 차수
	while (Apos <= A.degree && Bpos <= B.degree) {
		if (degree_a > degree_b) { // A항 > B항
			C.coef[Cpos++] = A.coef[Apos++];
			degree_a--;
		}
		else if (degree_a == degree_b) { // A항 == B항
			C.coef[Cpos++] = A.coef[Apos++] + B.coef[Bpos++];
			degree_a--; degree_b--;
		}
		else {// B항 > A항
			C.coef[Cpos++] = B.coef[Bpos++];
			degree_b--;
		}
	}
	return C;
}
polynomial poly_multiply1(polynomial A, polynomial B) {
	polynomial C;
	C.degree = A.degree + B.degree;

	for (int i = 0; i < C.degree + 1; i++) {
		C.coef[i] = 0;
	}  //모든항을 0으로 초기화 하여 각각의 degree의 값으로 coef
	//의 값을 변화시킬때에는 +=연산을 이용하겠다!

	for (int i = 0; i < A.degree + 1; i++) {
		for (int j = 0; j < B.degree + 1; j++) {
			C.coef[C.degree - ((A.degree - i) + (B.degree - j))] += A.coef[i] * B.coef[j];
		}//a[0]*b[0]은 c[0]으로  a[1]*b[0]은 c[1]로 이동하기 위한 코드
	}
	return C;
}
int poly_cal1(polynomial A, int x) {
	int result = 0;
	for (int i = 0; i < A.degree + 1; i++) {
		result += A.coef[i] * powf(x, A.degree - i);
	}//계수와 차수의 곱을 이용한 반환값 생성
	return result;
}

int main()
{
	int coef_1[6];
	int coef_2[6];
	char str1[30];
	char str2[30];
	int idx_1;
	int idx_2;
	int real_num = 0;
	int choose_equation = 1;
	int input = 1;
	int Idx;

	printf("수식 1을 입력하세요");
	fgets(str1, strlen(str1), stdin);

	idx_1 = 0;
	char* ptr = strtok(str1, " ");
	while (ptr != NULL) {
		if (ptr[strlen(ptr) - 1] == '\n') {
			for (Idx = strlen(ptr) - 2; Idx > 0; Idx--) {
				real_num += powf(10, (strlen(ptr) - 2 - Idx)) * (ptr[Idx] - '0');
			}
			if (ptr[Idx] == '-') {
				real_num *= -1;
			}
			else {
				real_num += powf(10, (strlen(ptr) - 2 - Idx)) * (ptr[Idx] - '0');
			}
		} 
		else { 
			for (Idx = strlen(ptr) - 1; Idx > 0; Idx--) {
				real_num += powf(10, (strlen(ptr) - 1 - Idx)) * (ptr[Idx] - '0');
			}
			if (ptr[Idx] == '-') {
				real_num *= -1;
			}
			else {
				real_num += powf(10, (strlen(ptr) - 1 - Idx)) * (ptr[Idx] - '0');
			}
		}
		coef_1[idx_1++] = real_num;
		real_num = 0;
		ptr = strtok(NULL, " ");
	}
	printf("수식 2를 입력하세요");
	fgets(str2, strlen(str2), stdin);

	idx_2 = 0;
	char* ptr2 = strtok(str2, " ");
	while (ptr2 != NULL) {
		if (ptr2[strlen(ptr2) - 1] == '\n') { //마지막 ptr은 \n을 포함그래서 이부분 제외하고 생각하기위한 코드
			for (Idx = strlen(ptr2) - 2; Idx > 0; Idx--) {
				real_num += powf(10, (strlen(ptr2) - 2 - Idx)) * (ptr2[Idx] - '0');
			}
			if (ptr2[Idx] == '-') { //ptr[0]은 숫자 or 부호로 나오므로 -인경우는 *-1
				real_num *= -1;
			}
			else { // ptr[0]이 숫자인 경우
				real_num += powf(10, (strlen(ptr2) - 2 - Idx)) * (ptr2[Idx] - '0');
			}
		}
		else {
			for (Idx = strlen(ptr2) - 1; Idx > 0; Idx--) {
				real_num += powf(10, (strlen(ptr2) - 1 - Idx)) * (ptr2[Idx] - '0');
			}
			if (ptr2[Idx] == '-') {
				real_num *= -1;
			}
			else {
				real_num += powf(10, (strlen(ptr2) - 1 - Idx)) * (ptr2[Idx] - '0');
			}
		}
		coef_2[idx_2++] = real_num;
		real_num = 0;
		ptr2 = strtok(NULL, " ");
	}


	polynomial num1;
	for (int i = 0; i < idx_1; i++)
		num1.coef[i] = coef_1[i];
	num1.degree = idx_1 - 1;
	//num1의 초기화

	polynomial num2;
	for (int i = 0; i < idx_2; i++)
		num2.coef[i] = coef_2[i];
	num2.degree = idx_2 - 1;
	//num2의 초기화

	polynomial num3;
	num3 = poly_add1(num1, num2);
	printf("수식 1+2는 ");
	for (int i = 0; i < (num3.degree) + 1; i++) {
		printf("%d ", num3.coef[i]);
	}//num3에는 덧셈을

	puts("");
	polynomial num4;
	num4 = poly_multiply1(num1, num2);
	printf("수식 1*2는 ");
	for (int i = 0; i < (num4.degree) + 1; i++) {
		printf("%d ", num4.coef[i]);
	}//num4에는 곱셈을
	puts("");
	while (choose_equation >= 1 && choose_equation <= 4) {
		printf("수식에 값을 넣으세요");
		scanf("%d %d", &choose_equation, &input);
		switch (choose_equation) {
		case 1:
			printf("결과값은 %d\n", poly_cal1(num1, input));
			break;
		case 2:
			printf("결과값은 %d\n", poly_cal1(num2, input));
			break;
		case 3:
			printf("결과값은 %d\n", poly_cal1(num3, input));
			break;
		case 4:
			printf("결과값은 %d\n", poly_cal1(num4, input));
			break;
		}

	}

	return 0;
}
