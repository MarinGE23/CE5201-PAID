%Ejemplo de como obtener cuantas entradas de una matriz
%satisfacen una condición boolena

% Crear una matriz aleatoria A de tamaño mxm

clc; clear

m=1000;
A=rand(m); %Esta matriz toma valores
           %aleatorios del intervalo [0,1]
           %siguiendo una distribución uniforme

%Obtener la cantidad de entradas de A
%cuyo valor es mayor a 0.75

% Método 1: Usando doble for
tic
cantidad1=0;
for i=1:m
  for j=1:m
    if A(i,j)>0.75
      cantidad1=cantidad1+1;
    end
  end
end
t1=toc;
display(['Tiempo del Metodo 1 = ' num2str(t1)])

% Método 2: Usando la estructura de GNU Octave
tic
Mascara1=(A>0.75); %Este comando genera una matriz binaria
                   %de tamaño mxm, donde tiene valor de 1 cuando
                   %la entrada es mayor a 0.75 y tiene valor de 0
                   %cuando la entrada es menor o igual a 0.75

cantidad2=sum(sum(Mascara1)); %Realiza la suma de todas las entradas
                              %de la matriz binaria Mascara1, dando
                              %como resultado la cantidad de entradas
                              %mayores a 0.75
t2=toc;
display(['Tiempo del Metodo 2 = ' num2str(t2)])

%Diferencia de las matrices es 0, ya que B1=B2
cantidad1
cantidad2

%Note que tanto el método 1 y el método 2 obtienen el mismo
%resultado, pero la implementación es diferente, y el tiempo
%de ejecución tambíen lo es
