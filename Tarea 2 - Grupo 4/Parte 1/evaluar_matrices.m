% Ejemplo de como cambiar y acceder a valores de una matriz
% sin tener que utilizar un doble for

% Crear una matriz aleatoria A de tamaño mxm

clc; clear

m=1000;
A=rand(m); %Esta matriz toma valores
           %aleatorios del intervalo [0,1]
           %siguiendo una distribución uniforme

% Obtener una matriz B de tamaño mxm, tal que
% B(i,j)=0 si A(i,j)<=0.5
% y
% B(i,j)=1 si A(i,j)>0.5

% Método 1: Usando doble for
tic
B1=zeros(m);
for i=1:m
  for j=1:m
    if A(i,j)<=0.5
      B1(i,j)=0;
    else
      B1(i,j)=1;
    end
  end
end
t1=toc;
display(['Tiempo del Metodo 1 = ' num2str(t1)])

% Método 2: Usando la estructura de GNU Octave
tic
B2=zeros(m);
B2(A<=0.5)=0; %Cambiar las entradas (i,j) de B2
              %por el valor 0 si A(i,j)<=0.5
B2(A>0.5)=1;  %Cambiar las entradas (i,j) de B2
              %por el valor 1 si A(i,j)>0.5
t2=toc;
display(['Tiempo del Metodo 2 = ' num2str(t2)])

%Diferencia de las matrices es 0, ya que B1=B2
diferencia=norm(B1-B2)

%Note que tanto el método 1 y el método 2 obtienen la misma
%matriz, pero la implementación es diferente, y el tiempo
%de ejecución tambíen lo es
