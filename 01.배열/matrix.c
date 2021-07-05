#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define MAX_TERMS 10 
typedef struct {
	int row;
	int col;
	int value;
} term;
typedef struct SparseMatrix {
	term data[MAX_TERMS];
	int rows; // 행의 개수
	int cols; // 열의 개수
	int terms; // 항의 개수
} SparseMatrix;

void add_normal(int(*arr_1)[9], int(*arr_2)[9], int(*result)[9], int scale) {
	int r, c;
	for (r = 0; r < scale; r++)
		for (c = 0; c < scale; c++)
			result[r][c] = arr_1[r][c] + arr_2[r][c];
}

void multiply_normal(int(*arr_1)[9], int(*arr_2)[9], int(*result)[9], int scale) {
	int r, c;
	for (r = 0; r < scale; r++) {
		for (c = 0; c < scale; c++) {
			result[r][c] = 0;
			for (int i = 0; i < 3; i++)
			{
				result[r][c] += arr_1[r][i] * arr_2[i][c];
			}
		}
	}
}

SparseMatrix add_sparse(SparseMatrix a, SparseMatrix b) {
	SparseMatrix c;
	int ca = 0, cb = 0, cc = 0; // 각 배열의 항목을 가리키는 인덱스
	// 배열 a와 배열 b의 크기가 같은지를 확인
	if (a.rows != b.rows || a.cols != b.cols) {
		fprintf(stderr, "희소행렬 크기에러\n");
		exit(1);
	}
	c.rows = a.rows;
	c.cols = a.cols;
	c.terms = 0;
	while (ca < a.terms && cb < b.terms) {
		// 각 항목의 순차적인 번호를 계산한다.
		int inda = a.data[ca].row * a.cols + a.data[ca].col;
		int indb = b.data[cb].row * b.cols + b.data[cb].col;
		if (inda < indb) {
			// a 배열 항목이 앞에 있으면
			c.data[cc++] = a.data[ca++];
		}
		else if (inda == indb) {
			// a와 b가 같은 위치
			if ((a.data[ca].value + b.data[cb].value) != 0) {
				c.data[cc].row = a.data[ca].row;
				c.data[cc].col = a.data[ca].col;
				c.data[cc++].value = a.data[ca++].value +
					b.data[cb++].value;
			}
			else {
				ca++; cb++;
			}
		}
		else // b 배열 항목이 앞에 있음
			c.data[cc++] = b.data[cb++];
	}
	// 배열 a와 b에 남아 있는 항들을 배열 c로 옮긴다.
	for (; ca < a.terms; )
		c.data[cc++] = a.data[ca++];
	for (; cb < b.terms; )
		c.data[cc++] = b.data[cb++];
	c.terms = cc;
	return c;
}


SparseMatrix multiply_sparse(SparseMatrix m1, SparseMatrix m2) {
	SparseMatrix m3;
	if (m1.rows != m2.rows || m1.cols != m2.cols) {
		fprintf(stderr, "희소행렬 크기에러\n");
		exit(1);
	} //n*n행렬만 받는다 했으므로
	m3.rows = m1.rows;
	m3.cols = m1.cols;
	m3.terms = 0;
	for (int i = 0; i < m1.terms; i++) {//각각 첫번째 항부터 접근하지만
		for (int j = 0; j < m2.terms; j++) {
			if (m1.data[i].col == m2.data[j].row)//m1의 col과 m2의 row가 같은것만 들고와서
			{
				int ind_ab = m1.data[i].row * m1.rows + m2.data[j].col;
				int row = m1.data[i].row;
				int col = m2.data[j].col;
				int value = m1.data[i].value * m2.data[j].value;
				int isbreak = 0;

				for (int p = 0; p < m3.terms; p++) {//자기 자신의 위치를 찾아 갈건데
					if (m3.data[p].row * m3.rows + m3.data[p].col > ind_ab) {//들어갈 위치를 찾으면
						for (int q = m3.terms - 1; q >= p; q--) {//그 뒤의 모든값을 한칸씩 뒤로보내고
							m3.data[q + 1].col = m3.data[q].col;
							m3.data[q + 1].row = m3.data[q].row;
							m3.data[q + 1].value = m3.data[q].value;
						}
						m3.data[p].row = row;
						m3.data[p].col = col;
						m3.data[p].value = value;
						isbreak = 1;//자기자리에 넣고 flag변수에 1을 저장!
						m3.terms += 1;
						break;
					}
					else if (m3.data[p].row * m3.rows + m3.data[p].col == ind_ab) {
						m3.data[p].value += value;
						isbreak = 1;
						break;//똑같은 위치에 넣어야 하면 걍 값만 +=연산 하고 flag변수는 1로!
					}
				}
				if (isbreak == 0) {
					m3.data[m3.terms].row = row;
					m3.data[m3.terms].col = col;
					m3.data[m3.terms++].value = value;
				}//flag변수가 0이면 추가 못했다는거니까 마지막에 추가해주자아아아!
			}
		}
	}
	return m3;
}
int main() {
	int scale;
	int arr_1[9][9];
	int arr_2[9][9];
	int result[9][9];
	SparseMatrix m1, m2, m3, m4;
	int idx = 0;
	int count_1 = 0, count_2 = 0;

	printf("행렬의 규격을 입력하세요.");
	scanf("%d", &scale);
	printf("행렬 1의 데이터를 입력하세요.");
	for (int i = 0; i < scale; i++) {
		for (int j = 0; j < scale; j++) {
			scanf("%d", &arr_1[i][j]);
		}
	}
	printf("행렬 2의 데이터를 입력하세요.");
	for (int i = 0; i < scale; i++) {
		for (int j = 0; j < scale; j++) {
			scanf("%d", &arr_2[i][j]);
		}
	}//저장방법 1은 그저 받음과 동시에 입력하기만 하면 됩니다!
	for (int i = 0; i < scale; i++) {
		for (int j = 0; j < scale; j++) {
			if (arr_1[i][j] != 0) {
				m1.data[idx].row = i;
				m1.data[idx].col = j;
				m1.data[idx++].value = arr_1[i][j];
			}
		}
	}//저장방법 2는 arr[i][j]에 각각 접근하여 0이 아닌 원소를 만나면 바로 저장해버리는식으로 !
	count_1 = idx;
	m1.rows = scale;
	m1.cols = scale;
	m1.terms = count_1;

	idx = 0;
	for (int i = 0; i < scale; i++) {
		for (int j = 0; j < scale; j++) {
			if (arr_2[i][j] != 0) {
				m2.data[idx].row = i;
				m2.data[idx].col = j;
				m2.data[idx++].value = arr_2[i][j];
			}
		}
	}
	count_2 = idx;
	m2.rows = scale;
	m2.cols = scale;
	m2.terms = count_2;
	printf("방식 1:\n");
	printf("행렬 1(%d)\n", scale * scale);

	for (int i = 0; i < scale; i++) {
		printf("                ");
		for (int j = 0; j < scale; j++) {
			printf("%d ", arr_1[i][j]);
		}
		puts("");
	}
	printf("행렬 2(%d)\n", scale * scale);
	for (int i = 0; i < scale; i++) {
		printf("                ");
		for (int j = 0; j < scale; j++) {
			printf("%d ", arr_2[i][j]);
		}
		puts("");
	}
	printf("행렬 1+2(%d)\n", scale * scale);
	add_normal(arr_1, arr_2, result, scale);
	for (int i = 0; i < scale; i++) {
		printf("                ");
		for (int j = 0; j < scale; j++) {
			printf("%d ", result[i][j]);
		}
		puts("");
	}
	printf("행렬 1*2(%d)\n", scale * scale);
	multiply_normal(arr_1, arr_2, result, scale);
	for (int i = 0; i < scale; i++) {
		printf("                ");
		for (int j = 0; j < scale; j++) {
			printf("%d ", result[i][j]);
		}
		puts("");
	}

	printf("방식 2:\n");
	printf("행렬 3 (%d개)\n", m1.terms * 3);
	for (int i = 0; i < m1.terms; i++) {
		printf("                ");
		printf("%d ", m1.data[i].row);
		printf("%d ", m1.data[i].col);
		printf("%d ", m1.data[i].value);
		puts("");
	}
	printf("행렬 4 (%d개)\n", m2.terms * 3);
	for (int i = 0; i < m2.terms; i++) {
		printf("                ");
		printf("%d ", m2.data[i].row);
		printf("%d ", m2.data[i].col);
		printf("%d ", m2.data[i].value);
		puts("");
	}
	m3 = add_sparse(m1, m2);
	printf("행렬 3+4 (%d개)\n", m3.terms * 3);
	for (int i = 0; i < m3.terms; i++) {
		printf("                ");
		printf("%d ", m3.data[i].row);
		printf("%d ", m3.data[i].col);
		printf("%d ", m3.data[i].value);
		puts("");
	}
	m4 = multiply_sparse(m1, m2);
	printf("행렬 3*4 (%d개)\n", m4.terms * 3);
	for (int i = 0; i < m4.terms; i++) {
		printf("                ");
		printf("%d ", m4.data[i].row);
		printf("%d ", m4.data[i].col);
		printf("%d ", m4.data[i].value);
		puts("");
	}
}
