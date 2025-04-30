#include <stdio.h>
#include <string.h>

// Structure for Mnemonics
struct Mnemonic {
    char name[10];
    int length;
} mtable[] = {
    {"L", 4},
    {"A", 4},
    {"ST", 4},
    {"SR", 2},
    {"BNE", 4},
    {"END", 0}
};

// Structure for Symbols
struct Symbol {
    char label[10];
    int address;
} stable[10];
int symCount = 0;

// Structure for each line of code
struct Line {
    char label[10];
    char mnemonic[10];
    char operand[20];
} program[] = {
    {"START", "L", "DATA"},
    {"LOOP", "A", "VALUE"},
    {"-", "ST", "TEMP"},
    {"-", "BNE", "LOOP"},
    {"TEMP", "SR", "AREG"},
    {"-", "END", "-"}
};

// Get the index of a mnemonic in the mnemonic table
int getMnemonicIndex(char *mnemonic) {
    for (int i = 0; i < 6; i++) {
        if (!strcmp(mtable[i].name, mnemonic)) {
            return i;
        }
    }
    return -1;
}

// Add a symbol to the symbol table if it's not a '-'
void addSymbol(char *label, int lc) {
    if (strcmp(label, "-")) {
        strcpy(stable[symCount].label, label);
        stable[symCount++].address = lc;
    }
}

// Generate intermediate code with symbol table population
void generateIntermediateCode() {
    int lc = 0;

    printf("\n--- Intermediate Code ---\n");
    for (int i = 0; i < 6; i++) {
        if (!strcmp(program[i].mnemonic, "END"))
            break;

        addSymbol(program[i].label, lc);
        printf("%d\t%s\t%s\n", lc, program[i].mnemonic, program[i].operand);

        int idx = getMnemonicIndex(program[i].mnemonic);
        if (idx != -1)
            lc += mtable[idx].length;
    }
}

// Main function
int main() {
    // Print Mnemonic Table
    printf("--- Mnemonic Table ---\n");
    for (int i = 0; i < 6; i++) {
        printf("%s\t%d\n", mtable[i].name, mtable[i].length);
    }

    // Generate Intermediate Code
    generateIntermediateCode();

    // Print Symbol Table
    printf("\n--- Symbol Table ---\n");
    for (int i = 0; i < symCount; i++) {
        printf("%s\t%d\n", stable[i].label, stable[i].address);
    }

    return 0;
}