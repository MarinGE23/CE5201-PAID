clc; clear; close all;
pkg load image
pkg load video

% Función principal que ejecuta los filtros de mediana modificada sobre un video
function filtros_mediana_modificada()
  V = VideoReader('con_ruido.mp4');  % Leer el video de entrada con ruido
  fr = V.NumberOfFrames;      % Obtener el número de frames (cuadros) en el video
  H = V.Height; W = V.Width;  % Obtener las dimensiones de cada cuadro (altura y anchura)

  Y1 = zeros(H, W, 3, fr);    % Matriz para almacenar el video filtrado con el primer algoritmo
  Y2 = zeros(H, W, 3, fr);    % Matriz para almacenar el video filtrado con el segundo algoritmo

  tic;
  FMFA(V, fr, H, W, Y1);      % Ejecutar el primer algoritmo de filtro de mediana rápida
  time1 = toc

  tic;
  IAMFA_I(V, fr, H, W, Y2);   % Ejecutar el segundo algoritmo de filtro mejorado
  time2 = toc
end

% Algoritmo 1: DP – Aproximación Rápida del Filtro de Mediana
function FMFA(V, fr, H, W, Y1)
  for k = 1:fr
    I = readFrame(V); % Leer el frame k. I es una imagen de tamaño H x W x 3
    I_filtered = I;   % Inicializar la imagen filtrada

    for c = 1:3       % Procesar cada canal por separado
      for i = 2:H-1
        % Calcular la mediana de la primera columna de píxeles
        col1 = median([I(i-1, 1, c), I(i, 1, c), I(i+1, 1, c)]);
        col2 = median([I(i-1, 2, c), I(i, 2, c), I(i+1, 2, c)]);
        for j = 3:W-1
          % Calcular la mediana para la siguiente columna
          col3 = median([I(i-1, j, c), I(i, j, c), I(i+1, j, c)]);
          % Asignar la mediana calculada al píxel filtrado
          I_filtered(i, j, c) = median([col1; col2; col3]);
          % Desplazar las columnas para la siguiente iteración
          col1 = col2;
          col2 = col3;
        end
      end
    end

    % Almacenar el frame filtrado en Y1
    Y1(:,:,:,k) = I_filtered;
  end

  % Crear y guardar el video filtrado con el primer algoritmo
  video = VideoWriter('sin_ruido_alg1.mp4');
  for i = 1:fr
    writeVideo(video, Y1(:,:,:,i));
  end
  close(video);
end

% Función para calcular la Mediana de Decisión de Valor Medio (Mid-Value-Decision Median)
function mvdd = MVDM(P)
    % Ordenar el vector P en orden ascendente
    P_sorted = sort(P);
    P1 = P_sorted(1);
    P2 = P_sorted(2);
    P3 = P_sorted(3);

    % Aplicar las condiciones para la decisión de la mediana
    if (P2 == 255)
        mvdd = P1;
    elseif (P2 > 0 && P2 < 255)
        mvdd = P2;
    else
        mvdd = P3;
    end
end

% Algoritmo 2: Algoritmo Aproximado Mejorado Propuesto - IAMFA-I
function IAMFA_I(V, fr, H, W, Y2)
  for k = 1:fr
    I = readFrame(V); % Leer el frame k. I es una imagen de tamaño H x W x 3
    I_filtered = I;   % Inicializar la imagen filtrada

    for c = 1:3       % Procesar cada canal por separado
      for i = 2:H-1
        % Calcular el valor de decisión mediana usando MVDM para la primera columna de píxeles
        col1 = MVDM([I(i-1, 1, c), I(i, 1, c), I(i+1, 1, c)]);
        col2 = MVDM([I(i-1, 2, c), I(i, 2, c), I(i+1, 2, c)]);
        for j = 3:W-1
            % Calcular MVDM para la siguiente columna
            col3 = MVDM([I(i-1, j, c), I(i, j, c), I(i+1, j, c)]);
            % Asignar el MVDM calculado al píxel filtrado
            I_filtered(i, j, c) = MVDM([col1; col2; col3]);
            % Desplazar las columnas para la siguiente iteración
            col1 = col2;
            col2 = col3;
        end
      end
    end

    % Almacenar el frame filtrado en Y2
    Y2(:,:,:,k) = I_filtered;
  end

  % Crear y guardar el video filtrado con el segundo algoritmo
  video = VideoWriter('sin_ruido_alg2.mp4');
  for i = 1:fr
    writeVideo(video, Y2(:,:,:,i));
  end
  close(video);
end

