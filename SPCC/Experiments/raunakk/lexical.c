#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// List of keywords
char keywords[][10] = {
    "int", "void", "if", "else", "while", "return", "for", "float", "char", "double"
};
int num_keywords = 10;

// Check if a word is a keyword
int i;
int isKeyword(char *word) {
    for ( i = 0; i < num_keywords; i++) {
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    }
    return 0;
}

// Check for operator
int isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%');
}

// Check for assignment or comparison operator
int isComparisonOperator(char ch) {
    return (ch == '=' || ch == '<' || ch == '>' || ch == '!');
}

int main() {
    char input[] = "int add(int a, int b) { printf(\"Sum is = %d\", a + b); return a + b; }";
    char token[100];
    int i = 0, j = 0;

    printf("+-------------------------+-------------------------+\n");
    printf("| Token Type              | Token                   |\n");
    printf("+-------------------------+-------------------------+\n");

    while (input[i] != '\0') {
   
        if (isspace(input[i]) || strchr("(){};,\'", input[i])) {
            i++;
            continue;
        }

        if (input[i] == '\"') {
            j = 0;
            token[j++] = input[i++];
            while (input[i] && input[i] != '\"') {
                token[j++] = input[i++];
            }
            if (input[i] == '\"') {
                token[j++] = input[i++];  // closing quote
            }
            token[j] = '\0';
            printf("| %-23s | %-23s |\n", "String Literal", token);
            continue;
        }

        if (isalpha(input[i]) || input[i] == '_') {
            j = 0;
            while (isalnum(input[i]) || input[i] == '_') {
                token[j++] = input[i++];
            }
            token[j] = '\0';

            if (isKeyword(token))
                printf("| %-23s | %-23s |\n", "Keyword", token);
            else
                printf("| %-23s | %-23s |\n", "Identifier", token);
        }


        else if (isOperator(input[i])) {
            printf("| %-23s | %-23c |\n", "Operator", input[i]);
            i++;
        }

        else if (isComparisonOperator(input[i])) {
            if (input[i+1] == '=') {
                printf("| %-23s | %-23c%c |\n", "Comparison Operator", input[i], input[i+1]);
                i += 2;
            } else {
                printf("| %-23s | %-23c |\n", "Assignment/Comparison", input[i]);
                i++;
            }
        }

        else if (isdigit(input[i])) {
            j = 0;
            while (isdigit(input[i])) {
                token[j++] = input[i++];
            }
            token[j] = '\0';
            printf("| %-23s | %-23s |\n", "Number", token);
        }

        else {
            i++;
        }
    }
    printf("+-------------------------+-------------------------+\n");

    return 0;
}
