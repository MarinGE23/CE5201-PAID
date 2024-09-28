% MATLAB script to save two matrices J such that J^2 = -I_4 and print them

% First matrix with complex entries
J1 = [0, -1, 0, 0;
      1, 0, 0, 0;
      0, 0, 0, -1;
      0, 0, 1, 0];

% Second matrix with only real entries
J2 = [0, 1, 0, 0;
      -1, 0, 0, 0;
      0, 0, 0, 1;
      0, 0, -1, 0];


%consola
disp('Matriz J1 (compleja):');
disp(J1);

disp('Matriz J2 (real):');
disp(J2);

%  J1^2 y J2^2 = -I_4
I4 = eye(4);
disp('J1^2:');
disp(J1 * J1);

disp('J2^2:');
disp(J2 * J2);

disp('Esperado -I4:');
disp(-I4);
