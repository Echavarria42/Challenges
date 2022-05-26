#include <iostream>
#include<vector>
using namespace std;


 void merge(vector<int>&arreglo,int inicio,int mitad,int final)
  {
      int i,j,k;
      int elementosizq= mitad - inicio+1;
      int elementosderec= final - mitad;

      vector<int>izquierda(elementosizq);
      vector<int>derecha(elementosderec);

      for(i=0;i<elementosizq;i++)
      {
          izquierda[i]= arreglo[inicio+i];
      }
      for (int j=0;elementosderec;j++)
      {
          derecha[j]= arreglo[mitad+1+j];
      }
      i=0;
      j=0;
      k=inicio;

      while(i<elementosizq && j<elementosderec)
      {
          if(izquierda[i]<=derecha[j])
          {
              arreglo[k]=izquierda[i];
              i++;
          }
          else
          {
              arreglo[k]=derecha[j];
          j++;
          }
          k++;
      }
      while(j<elementosderec)
      {
          arreglo [k]= derecha[j];
          j++;
          k++;

      }
      while(i<elementosizq)
      {
          arreglo [k]=izquierda[i];
          i++;
          k++;
      }


  }
  
 void mergesort(vector<int>&arreglo,int inicio,int final){
 if(inicio<final){
    int mitad= inicio+(final-inicio)/2;
    mergesort(arreglo,inicio,final);
    mergesort(arreglo,mitad+1,final);
    merge(arreglo,inicio,mitad,final);


 }

 }

void imprimirArreglo(vector<int>arreglo)
{
    for (int i=0;i<arreglo.size();i++)
    {
      cout<<arreglo[i]<<" ";
    }
    cout<<endl;




}
int main(){
    vector<int> prueba1= {12,0,6,2,9,34,1};
    imprimirArreglo(prueba1);
    mergesort(prueba1,0,prueba1.size()-1);
    imprimirArreglo(prueba1);
    return 0;

}