#include <stdio.h>
#include <string.h>
struct Flower 
{
    char name[20];
    char color[10];
};
struct Bouquet 
{
    struct Flower flowers[10];
    int flower_count;
};
// Function to add a flower to a bouquet
void add_flower(struct Bouquet *bouquet, char *name, char *color) 
    {
    if (bouquet->flower_count < 10) {
        strcpy(bouquet->flowers[bouquet->flower_count].name, name);
        strcpy(bouquet->flowers[bouquet->flower_count].color, color);
        bouquet->flower_count++;
    } else 
	{
        printf("Bouquet is full!\n");
    }
}
// Function to display the bouquet
void display_bouquet(struct Bouquet bouquet) 
{
    printf("Bouquet contains %d flowers:\n", bouquet.flower_count);
    for(int i=0;i<bouquet.flower_count;i++) 
	{
        printf("Flower %d: %s, %s\n", i+1, bouquet.flowers[i].name, bouquet.flowers[i].color);
    }
}
int main()
{
    struct Bouquet myBouquet;
    myBouquet.flower_count = 0;
    add_flower(&myBouquet, "Rose", "Red");
    add_flower(&myBouquet, "Lily", "White");
    add_flower(&myBouquet, "Tulip", "Yellow");

    display_bouquet(myBouquet);

    return 0;
}
