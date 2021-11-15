#include <stdio.h>  
#include <stdlib.h>  
#include <time.h>
#define KEYSIZE 16

void main() {
    long int currentTick, 
    endTick =1523920129+3*60*60*24; 
    
    //choose large date range (assumed to be a day) where the time the key was generated is guaranteed
    //to be found. NOTE: this equation assumes that 1 tick = 1 second although this may vary. One can receive
    //a more accurate estimation using a CLOCKS_PER_SEC macro. It was unnecesssary here since a result was received 
    //in the end which is highly unlikely to be false given the size of the key;

    int i;
	freopen("./data/keysWithin2Hours.txt", "w+", stdout); 
    for(currentTick=1523920129; currentTick <= endTick; currentTick++) {  
        char key[KEYSIZE];
        srand (currentTick);
        for (i = 0; i< KEYSIZE; i++){
            key[i] = rand()%256;
            printf("%.2x", (unsigned char)key[i]);
        }
        printf("\n");
    }

}

