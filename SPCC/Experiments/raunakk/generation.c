#include <stdio.h>
#include <string.h>

#define MAX 20

struct Instruction {
    char result[10];
    char operand1[10];
    char operator[3];
    char operand2[10];
};

struct Instruction ic[MAX];

int main() {
    int n;
    printf("Enter number of intermediate instructions: ");
    scanf("%d", &n);

    printf("Enter intermediate instructions in format: result = operand1 operator operand2\n");
    for (int i = 0; i < n; i++) {
        scanf("%s = %s %s %s", ic[i].result, ic[i].operand1, ic[i].operator, ic[i].operand2);
    }

    printf("\n--- Target Code ---\n");
    for (int i = 0; i < n; i++) {
        printf("MOV R%d, %s\n", i, ic[i].operand1);

        if (strcmp(ic[i].operator, "+") == 0)
            printf("ADD R%d, %s\n", i, ic[i].operand2);
        else if (strcmp(ic[i].operator, "-") == 0)
            printf("SUB R%d, %s\n", i, ic[i].operand2);
        else if (strcmp(ic[i].operator, "*") == 0)
            printf("MUL R%d, %s\n", i, ic[i].operand2);
        else if (strcmp(ic[i].operator, "/") == 0)
            printf("DIV R%d, %s\n", i, ic[i].operand2);

        printf("MOV %s, R%d\n", ic[i].result, i); // Store back result
    }

    return 0;
}



// Enter number of intermediate instructions: 2
// Enter intermediate instructions in format: result = operand1 operator operand2
// t1 = a + b
// t2 = t1 * c


// --- Target Code ---
// MOV R0, a
// ADD R0, b
// MOV t1, R0
// MOV R1, t1
// MUL R1, c
// MOV t2, R1
