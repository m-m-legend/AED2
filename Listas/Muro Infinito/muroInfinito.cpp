#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <locale.h>

//Lista Circular Duplamente Encadeada
//MURO INFINITO

typedef struct No{
	
	int e;
	No* Prox;
	No* Ant;
	
}No;

void insereValor(No* &L, int valor);
void criarLista(No* &L);
void excluirLista(No* &L);
void imprimeLista(No* L);
int muroInfinito(No* L, No* inicio, int alvo);

int main(){
	setlocale(LC_ALL, "Portuguese");
	No* L1;
	criarLista(L1);
	insereValor(L1, 5);
	insereValor(L1, 3);
	insereValor(L1, 4);
	insereValor(L1, 70);
	insereValor(L1, 12);
	imprimeLista(L1);
	int pos = muroInfinito(L1, L1, 70);
	printf("Posição do alvo: %d\n", pos);
	
	
	
	

	return 0;
}

void criarLista(No* &L){
	L = NULL;
}


void insereValor(No* &L, int valor) { 
    No* novo = (No*)malloc(sizeof(No));
    novo->e = valor;

    if (L == NULL) { 
        novo->Prox = novo; 
        novo->Ant = novo; 
        L = novo; 
    } else { 
        No* ult = L->Ant; 

        novo->Prox = L; 
        novo->Ant = ult; 

        ult->Prox = novo; 
        L->Ant = novo; 

    }
}

void imprimeLista(No* L) {
    if (L == NULL) { 
        printf("Lista vazia.\n");
        return;
    }

    No* Aux = L;
    
    printf("%d\n", Aux->e); 
    Aux = Aux->Prox; 

    while (Aux != L) { 
        printf("%d\n", Aux->e);
        Aux = Aux->Prox;
    }
    printf("\n");
}



void excluirLista(No* &L) {
    if (L == NULL) return; 

    No* atual = L;
    No* proximo;

    while (atual->Prox != L) { 
        proximo = atual->Prox; 
        free(atual); 
        atual = proximo; 
    }
	
    free(atual); 
    L = NULL; 
}

int muroInfinito(No* L, No* inicio, int alvo) {
    if (!inicio || !L){
    	return -1;
	}

    int passo = 1;
    No* esquerda = inicio;
    No* direita = inicio;
    int posEsq = 0, posDir = 0;

    while (true) {
        for (int i = 0; i < passo; i++) {
            if (esquerda->e == alvo) return posEsq;
            if (direita->e == alvo) return posDir;
            
            esquerda = esquerda->Ant;
            direita = direita->Prox;
            posEsq--;
            posDir++;
        }
        passo *= 2; 

        if (esquerda == direita) break; 
    }
    return -1;
}


