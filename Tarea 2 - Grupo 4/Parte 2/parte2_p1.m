% Script de MATLAB para guardar dos matrices J tales que J^2 = -I_4 y mostrarlas

% Primera matriz con entradas complejas
J1 = [0, -1, 0, 0;
      1, 0, 0, 0;
      0, 0, 0, -1;
      0, 0, 1, 0];

% Segunda matriz con solo entradas reales
J2 = [0, 1, 0, 0;
      -1, 0, 0, 0;
      0, 0, 0, 1;
      0, 0, -1, 0];

% Guardar las matrices en un archivo
save('parte2p1.mat', 'J1', 'J2');

% Mostrar las matrices en la consola
disp('Matriz J1 (compleja):');
disp(J1);

disp('Matriz J2 (real):');
disp(J2);

% Comprobar que J1^2 y J2^2 son iguales a -I4
I4 = eye(4); % Matriz identidad de 4x4
disp('J1^2:');
disp(J1 * J1);

disp('J2^2:');
disp(J2 * J2);

disp('Esperado -I4:');
disp(-I4);

% Verificar que J1^2 y J2^2 son iguales a -I4
if isequal(J1 * J1, -I4) && isequal(J2 * J2, -I4)
    disp('Ambas matrices cumplen que J^2 = -I_4');
else
    disp('Error: Las matrices no cumplen que J^2 = -I_4');
end
