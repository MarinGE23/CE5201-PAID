clc; clear; close all;
pkg load image
pkg load video

V = VideoReader('original.mp4');  % Leer el video de entrada 'original.mp4'
fr = V.NumberOfFrames;            % Obtener el número de frames (cuadros) en el video
m = V.Height; n = V.Width;        % Obtener las dimensiones de cada cuadro (altura y anchura)

Y = zeros(m, n, 3, fr);           % Inicializar una matriz para almacenar los frames con ruido

% Leer el video y añadir ruido de tipo 'salt and pepper' a cada frame
for k = 1:fr
    Z = readFrame(V);  % Leer el frame k. Z es una imagen de tamaño m x n x 3
    Y(:,:,1,k) = imnoise(Z(:,:,1), 'salt & pepper', 0.05);  % Ruido al canal rojo
    Y(:,:,2,k) = imnoise(Z(:,:,2), 'salt & pepper', 0.05);  % Ruido al canal verde
    Y(:,:,3,k) = imnoise(Z(:,:,3), 'salt & pepper', 0.05);  % Ruido al canal azul
end

% Crear y guardar un nuevo video a partir de los frames con ruido
video = VideoWriter('con_ruido.mp4');
for i = 1:fr
  writeVideo(video, Y(:,:,:,i));
end
close(video);

